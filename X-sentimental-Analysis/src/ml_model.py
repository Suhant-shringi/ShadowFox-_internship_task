from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_ml_model(df):
    vectorizer = TfidfVectorizer(max_features=5000)

    X = vectorizer.fit_transform(df['clean_text'])
    y = df['sentiment']  

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print(classification_report(y_test, predictions))

    return model, vectorizer