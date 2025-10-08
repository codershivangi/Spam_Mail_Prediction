# Spam Mail Prediction

## Project Overview

Spam Mail Prediction is a machine learning project that classifies emails (or text messages) as either **spam** or **not spam (ham)**. The system is built using Python, and it uses a trained model along with vectorization to process new inputs and predict whether they are spam. The project also includes a simple web interface (Flask) so users can input email text and see predictions.

The repository contains:
- A Jupyter notebook to explore the dataset, preprocess text, train and validate models.
- The serialized model and vectorizer.
- A small Flask app to serve predictions via a web form.
- The dataset used for training/testing.

## Features

- Preprocessing of raw email/text data (tokenization, stop-word removal, lowercasing, etc.)
- Vectorization using techniques like TF-IDF or CountVectorizer
- Training and evaluation of classification model(s) (e.g., Naive Bayes, Logistic Regression)
- Saving and loading the trained model and vectorizer
- Web interface (via Flask) for users to submit input text and receive prediction
- Basic UI/UX to show “Spam” or “Not Spam” result

## Technologies / Tools Used

| Component | Technology / Library |
|-----------|----------------------|
| Programming Language | Python |
| Data Manipulation & Analysis | pandas, NumPy |
| Text Processing / NLP | scikit-learn (CountVectorizer, TfidfVectorizer, etc.), NLTK or similar |
| Machine Learning / Modeling | scikit-learn (e.g. MultinomialNB, LogisticRegression, model selection tools) |
| Serialization (saving model) | pickle |
| Web Framework | Flask |
| Frontend (HTML/CSS) | Basic HTML + CSS (Jinja templates) |
| Hosting / Deployment (optional) | (You can add details if deployed: Heroku, AWS, etc.) |
