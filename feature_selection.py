# feature_selection.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from xgboost import XGBClassifier

# Load dataset
df = pd.read_csv("data/processed/cleaned_students.csv")

# Convert Target: 1 = Dropout, 0 = Not Dropout (combine 0 and 2)
df["Target"] = df["Target"].apply(lambda x: 1 if x == 1 else 0)

# Split features and label
X = df.drop(columns=["Target"])
y = df["Target"]

# Train model
model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
model.fit(X, y)

# Feature importance
importance = model.feature_importances_
features = pd.DataFrame({
    "feature": X.columns,
    "importance": importance
}).sort_values(by="importance", ascending=False)

print("\nTop 20 Most Important Features:\n")
print(features.head(20))

# Optional: Visualize top 20
plt.figure(figsize=(10, 6))
sns.barplot(x="importance", y="feature", data=features.head(20))
plt.title("Top 20 Features Influencing Dropout")
plt.tight_layout()
plt.show()
