/* ==========================================================================
   AI Sentiment Analyzer — front-end behavior
   The prediction call in `getPrediction()` is a placeholder. Replace it with
   a fetch() to the real Python ML backend when it's ready — nothing else
   in this file needs to change as long as the response shape is preserved:
   { sentiment: "positive" | "negative", confidence: number (0-1) }
   ========================================================================== */

(function () {
  "use strict";

  const form = document.getElementById("analyzer-form");
  const input = document.getElementById("review-input");
  const charCounter = document.getElementById("char-counter");
  const inputError = document.getElementById("input-error");
  const predictBtn = document.getElementById("predict-btn");

  const resultCard = document.getElementById("result-card");
  const resultBadge = document.getElementById("result-badge");
  const resultDetail = document.getElementById("result-detail");
  const iconPositive = document.getElementById("result-icon-positive");
  const iconNegative = document.getElementById("result-icon-negative");
  const confidenceValue = document.getElementById("confidence-value");
  const confidenceFill = document.getElementById("confidence-fill");

  const MAX_LENGTH = 2000;

  /* -------------------------------------------------------------------- */
  /* Character counter                                                     */
  /* -------------------------------------------------------------------- */
  function updateCharCounter() {
    const length = input.value.length;
    charCounter.textContent = `${length} / ${MAX_LENGTH}`;
  }

  input.addEventListener("input", () => {
    updateCharCounter();
    if (input.value.trim().length > 0) {
      inputError.textContent = "";
    }
  });

  /* -------------------------------------------------------------------- */
  /* Validation                                                            */
  /* -------------------------------------------------------------------- */
  function validate() {
    const value = input.value.trim();
    if (value.length === 0) {
      inputError.textContent = "Enter a review before analyzing.";
      input.focus();
      return false;
    }
    if (value.length < 8) {
      inputError.textContent = "Add a bit more detail for an accurate reading.";
      input.focus();
      return false;
    }
    inputError.textContent = "";
    return true;
  }

  /* -------------------------------------------------------------------- */
  /* Button loading state                                                  */
  /* -------------------------------------------------------------------- */
  function setLoading(isLoading) {
    predictBtn.disabled = isLoading;
    predictBtn.classList.toggle("is-loading", isLoading);
  }

  /* -------------------------------------------------------------------- */
  /* Placeholder prediction — swap for a real API call later               */
  /* -------------------------------------------------------------------- */
 async function getPrediction(reviewText) {
  const response = await fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      review: reviewText,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to get prediction from the server.");
  }

  return await response.json();
}
  /* -------------------------------------------------------------------- */
  /* Render result                                                         */
  /* -------------------------------------------------------------------- */
  function renderResult({ sentiment, confidence }) {
    const isPositive = sentiment === "positive";

    resultCard.classList.remove("is-positive", "is-negative", "is-visible");
    // Force reflow so the entrance animation can replay on repeated submits.
    void resultCard.offsetWidth;

    resultCard.classList.add(isPositive ? "is-positive" : "is-negative");
    resultBadge.textContent = isPositive ? "Positive" : "Negative";
    resultDetail.textContent = isPositive
      ? "The model reads this as an enthusiastic review."
      : "The model reads this as a critical review.";

    iconPositive.hidden = !isPositive;
    iconNegative.hidden = isPositive;

    const confidencePercent = Math.round(confidence * 100);
    confidenceValue.textContent = `${confidencePercent}%`;
    confidenceFill.style.width = "0%";

    resultCard.hidden = false;
    requestAnimationFrame(() => {
      resultCard.classList.add("is-visible");
      requestAnimationFrame(() => {
        confidenceFill.style.width = `${confidencePercent}%`;
      });
    });

    resultCard.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }

  /* -------------------------------------------------------------------- */
  /* Submit handler                                                        */
  /* -------------------------------------------------------------------- */
  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    if (!validate()) {
      return;
    }

    setLoading(true);

    try {
      const prediction = await getPrediction(input.value.trim());
      renderResult(prediction);
    } catch (error) {
      inputError.textContent = "Something went wrong. Please try again.";
    } finally {
      setLoading(false);
    }
  });

  updateCharCounter();
})();
