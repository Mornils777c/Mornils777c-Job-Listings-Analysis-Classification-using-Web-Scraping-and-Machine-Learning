import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/job_listings.csv")
df.dropna(inplace=True)
df['Category'] = df['Job Title'].apply(lambda x: 'Data Analyst' if 'Analyst' in x else 'Other')

X = df['Summary']
y = df['Category']

vectorizer = CountVectorizer(stop_words='english')
X_vec = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("Accuracy:", round(model.score(X_test, y_test) * 100, 2), "%")
print("\nClassification Report:\n", classification_report(y_test, model.predict(X_test)))

cm = confusion_matrix(y_test, model.predict(X_test))
sns.heatmap(cm, annot=True, fmt='d', cmap='Purples', xticklabels=model.classes_, yticklabels=model.classes_)
plt.title("Confusion Matrix - Logistic Regression")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig("output/confusion_matrix.png")
plt.close()
