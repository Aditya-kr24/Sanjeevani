import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

data = pd.read_csv("Final_dataset.csv")

data['text'] = data['text'].astype(str).str.lower()
X_train, X_test, y_train, y_test = train_test_split(
    data['text'], data['label'], test_size=0.2, random_state=42, stratify=data['label']
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(
        max_features=5000,
        ngram_range=(1,2),
        stop_words='english'
    )),
    ("clf", LogisticRegression(max_iter=300, class_weight='balanced'))
])
                 
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# 7. Save model
joblib.dump(model, "model.joblib")

print("✅New model saved as model.joblib")