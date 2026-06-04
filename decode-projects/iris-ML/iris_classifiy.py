import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

iris = load_iris()
X = iris.data                
y = iris.target               
feature_names = iris.feature_names
class_names = list(iris.target_names)


df = pd.DataFrame(X, columns=feature_names)
df["species"] = [class_names[i] for i in y]

print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)
print(f"Samples : {X.shape[0]}")
print(f"Features: {X.shape[1]}  -> {feature_names}")
print(f"Classes : {class_names}")
print("\nFirst 5 rows:")
print(df.head())
print("\nClass balance:")
print(df["species"].value_counts())


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


X_temp, X_test, y_temp, y_test = train_test_split(
    X_scaled, y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp,
    test_size=0.25,        
    random_state=42,
    stratify=y_temp,
)

print("\n" + "=" * 50)
print("TRAIN / VALIDATION / TEST SPLIT")
print("=" * 50)
print(f"Training samples  : {X_train.shape[0]}   (60%)")
print(f"Validation samples: {X_val.shape[0]}   (20%)")
print(f"Testing samples   : {X_test.shape[0]}   (20%)")


k_range = range(1, 21)
error_rates = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    val_preds = knn.predict(X_val)
    error_rates.append(1 - accuracy_score(y_val, val_preds))

min_error = min(error_rates)
best_k = max(k for k, err in zip(k_range, error_rates) if err == min_error)
print(f"\nBest K (chosen on validation set): {best_k}")

plt.figure(figsize=(8, 4))
plt.plot(list(k_range), error_rates, marker="o", color="#1f4e79")
plt.axvline(best_k, color="#d9480f", linestyle="--", label=f"Best K = {best_k}")
plt.xlabel("K (number of neighbors)")
plt.ylabel("Validation error rate")
plt.title("Choosing K — Tuned on the Validation Set")
plt.xticks(list(k_range))
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("elbow_plot.png", dpi=120)
plt.close()


X_final = np.vstack([X_train, X_val])
y_final = np.concatenate([y_train, y_val])

model = KNeighborsClassifier(n_neighbors=best_k)
model.fit(X_final, y_final)
predictions = model.predict(X_test)


acc = accuracy_score(y_test, predictions)
f1 = f1_score(y_test, predictions, average="weighted")
cm = confusion_matrix(y_test, predictions)

print("\n" + "=" * 50)
print("RESULTS")
print("=" * 50)
print(f"Accuracy : {acc:.4f}")
print(f"F1 score : {f1:.4f}  (weighted)")
print("\nFull classification report:")
print(classification_report(y_test, predictions, target_names=class_names))

print("Confusion matrix (rows = actual, columns = predicted):")
print(pd.DataFrame(cm, index=class_names, columns=class_names))

plt.figure(figsize=(6, 5))
sns.heatmap(
    cm, annot=True, fmt="d", cmap="Blues",
    xticklabels=class_names, yticklabels=class_names,
    cbar=False,
)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title(f"Confusion Matrix  (K = {best_k})")
plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=120)
plt.close()


sample = np.array([[5.1, 3.5, 1.4, 0.2]])      
sample_scaled = scaler.transform(sample)
predicted_class = class_names[model.predict(sample_scaled)[0]]

print("\n" + "=" * 50)
print("PREDICTING A NEW FLOWER")
print("=" * 50)
print(f"Measurements: {sample.tolist()[0]}")
print(f"Predicted species: {predicted_class}")

print("\nDone. Plots saved as 'elbow_plot.png' and 'confusion_matrix.png'.")
