import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
import joblib
import os

# Load dataset
df = pd.read_csv("data/processed/cleaned_students.csv")

# Binary conversion of Target
df["Target"] = df["Target"].apply(lambda x: 0 if x == 0 else 1)

# List of top features
top_features = [
    'Tuition fees up to date', 'Curricular units 2nd sem (approved)',
    'Scholarship holder','Curricular units 2nd sem (enrolled)',
    'Curricular units 1st sem (approved)','Curricular units 2nd sem (evaluations)',
    'Curricular units 1st sem (evaluations)','Debtor','Mother\'s occupation',
    'Curricular units 1st sem (enrolled)','Age at enrollment','Course','GDP',
    'Curricular units 2nd sem (without evaluations)','Previous qualification',
    'Curricular units 1st sem (without evaluations)','Unemployment rate','Application mode',
    'Admission grade','Curricular units 1st sem (grade)'
]

X = df[top_features]
y = df["Target"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Apply SMOTE
smote = SMOTE(random_state=42)
X_train_sm, y_train_sm = smote.fit_resample(X_train, y_train)

# Grid search
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.2],
    'subsample': [0.8, 1.0]
}
model = XGBClassifier(eval_metric='logloss', use_label_encoder=False, random_state=42)
grid_search = GridSearchCV(model, param_grid=param_grid, cv=3, scoring='f1', verbose=1, n_jobs=-1)
grid_search.fit(X_train_sm, y_train_sm)

# Evaluate best model
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

# Results
print("\nBest Model Results:\n", classification_report(y_test, y_pred))

# Save Model
os.makedirs("model", exist_ok=True)
joblib.dump(best_model, "model/optimized_dropout_model.pkl")
print("\nBest Model saved to model/optimized_dropout_model.pkl")
