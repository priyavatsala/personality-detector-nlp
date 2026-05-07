# Personality Detector using NLP

Ever wondered what your writing style says about your personality?

This project is an AI-powered personality detection web app that predicts a user's **MBTI personality type** from text input using **Natural Language Processing (NLP)** and **Machine Learning**.

The idea behind this project was to combine AI with psychology-inspired personality analysis in an interactive and visually engaging way. Users can write naturally about themselves, and the model analyzes their text to predict personality traits and provide meaningful insights.

---

#  What This Project Does

🔹 Predicts MBTI personality type from text  
🔹 Analyzes writing patterns using NLP  
🔹 Provides personality insights and descriptions  
🔹 Displays strengths and weaknesses  
🔹 Suggests suitable career paths  
🔹 Shows famous personalities with similar traits  
🔹 Includes a modern AI-inspired interactive UI  

---

#  Technologies Used

### Frontend
- Streamlit

### Machine Learning & NLP
- Python
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- NLP preprocessing techniques

###  Development Tools
- VS Code
- Jupyter Notebook
- Git & GitHub

---

#  How It Works

The workflow of the project is :

1. The user writes a paragraph describing themselves
2. The text is cleaned and preprocessed using NLP techniques
3. TF-IDF converts the text into numerical features
4. The trained Machine Learning model predicts the MBTI personality type
5. The application displays personality insights and recommendations

---

# Project Structure

```bash
personality-detector-nlp/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── notebooks/
│   └── data_exploration.ipynb
│
├── src/
│   └── predict.py
