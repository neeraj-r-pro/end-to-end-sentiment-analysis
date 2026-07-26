# 🎬 End-to-End Movie Sentiment Analysis

An end-to-end machine learning project that predicts whether a movie review is **Positive** or **Negative** using Natural Language Processing (NLP).

The project is built using **Python**, **Flask**, **Scikit-learn**, and **TF-IDF Vectorization**, and provides a simple web interface for real-time sentiment prediction.

---

## 🚀 Features

- Predicts sentiment of movie reviews
- Clean and responsive Flask web interface
- TF-IDF Vectorization for text preprocessing
- Logistic Regression classifier
- End-to-end ML pipeline
- Modular project structure
- Model persistence using Pickle

---

## 🛠️ Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML
- CSS

---

## 📂 Dataset

- IMDB Movie Reviews Dataset
- 50,000 labeled movie reviews
- Binary Classification
  - Positive
  - Negative

---

## 📁 Project Structure

```
end-to-end-sentiment-analysis/
│
├── artifacts/
├── notebook/
├── src/
│   └── sentiment/
│       ├── components/
│       ├── pipeline/
│       ├── utils.py
│       ├── exception.py
│       └── logging.py
│
├── static/
├── templates/
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Workflow

1. Load IMDB dataset
2. Split into training and testing data
3. Transform text using TF-IDF
4. Train Logistic Regression model
5. Save trained model
6. Predict sentiment using Flask application

---

## ▶️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Train the model

```bash
python main.py
```

Run the application

```bash
python app.py
```

---

## 📸 Screenshots

Screenshots will be added soon.

---

## 🔮 Future Improvements

- Deploy on Render or Railway
- Add Docker support
- Improve model performance using Transformer models
- Add user authentication
- Support multiple languages

---

## 👨‍💻 Author

**Neeraj R**

B.Tech Computer Science and Engineering
