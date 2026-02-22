# 📊 X Sentiment Analysis Dashboard

A simple Sentiment Analysis Web App built using Python, VADER, and Streamlit.

This application analyzes text input and classifies it as:

- ✅ Positive
- ❌ Negative
- ➖ Neutral

---

## 🧠 About VADER

This project uses VADER (Valence Aware Dictionary and sEntiment Reasoner).

VADER is:
- A rule-based sentiment analysis tool
- Specially designed for social media text
- No training required
- Fast and lightweight

It returns four scores:
- neg (negative score)
- neu (neutral score)
- pos (positive score)
- compound (final sentiment score)

### Compound Score Rule

| Compound Score | Sentiment |
|---------------|-----------|
| >= 0.05       | Positive  |
| <= -0.05      | Negative  |
| Between       | Neutral   |

---

## 🚀 Features

- Real-time sentiment analysis
- Beginner-friendly project structure
- Uses rule-based NLP model
- Clean and simple Streamlit UI
- Displays final sentiment result

---

## 🛠 Technologies Used

- Python
- Streamlit
- vaderSentiment
- matplotlib (optional for graphs)
- pandas (optional for dataset handling)

---

## 📂 Project Structure

X-SENTIMENT-ANALYSIS/
│
├── app/
│   └── streamlit_app.py
│
├── src/
│   ├── __init__.py
│   └── vader_model.py
│
├── data.csv (optional)
└── README.md

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install streamlit
pip install vaderSentiment
pip install matplotlib
pip install pandas
```

OR create a requirements.txt file:

```
streamlit
vaderSentiment
matplotlib
pandas
```

Then run:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

From the project root directory:

```bash
streamlit run app/streamlit_app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## 🔄 How It Works

1. User enters text
2. Clicks Analyze button
3. Text is sent to VADER model
4. VADER calculates sentiment scores
5. Compound score determines final sentiment
6. Result is displayed on screen

---

## 📌 Example

Input:
```
I love this government
```

Output:
```
Sentiment: Positive
Compound Score: 0.63
```

---

## 📈 Future Improvements

- Add sentiment distribution graph
- Add dataset-based analysis
- Add confusion matrix
- Compare with ML models
- Deploy on Streamlit Cloud

---

## 👨‍💻 Author

Developed by Sushant
