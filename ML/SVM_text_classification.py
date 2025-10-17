#SIMPLE SVM PROGRAM for text classification
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# 1. Load Data
# Define the small dataset
# We will classify texts as tech(0) or finance(1)
data = [
    "Apple launched a new iPhone with better neural engine.",  # tech
    "The stock market saw huge gains after the quarterly report.", # finance
    "Google's machine learning model achieved 90% accuracy.",  # tech
    "Investors are worried about rising interest rates and inflation.", # finance
    "Python libraries like scikit-learn are great for ML.", # tech
    "Bonds and treasury yields are highly volatile this week." # finance
]
labels = [0,1,0,1,0,1]
target_names = ['tech', 'finance']

# 2. Split Data
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# 3. Feature Extraction (TF-IDF)
vectorizer = TfidfVectorizer(stop_words='english')

# Convert training data
X_train_v = vectorizer.fit_transform(X_train)

# Convert testing data
X_test_v= vectorizer.transform(X_test)

# 4. Initialize and Train the SVM
svm = SVC(kernel='linear')
svm.fit(X_train_v, y_train)

# 5. Predict and Evaluate
y_pred = svm.predict(X_test_v)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")


# 6. Simple Prediction
new_text = input('Enter a text: ')
new_text_v = vectorizer.transform([new_text])
prediction = svm.predict(new_text_v)
print(f'Prediction: {target_names[prediction[0]]}')
