from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# SE CARGA EL DATASET DEL VINO
wine = load_wine()
X, y = wine.data, wine.target

#SE DIVIDE LOS DATOS DE ENTRENAMIENTO Y PRUEBA (80% Y 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("-- 1. Entrenar con max_depth = 2 --")
tree_depth2 = DecisionTreeClassifier(max_depth = 2, random_state = 42)
tree_depth2.fit(X_train, y_train)
y_pred2 = tree_depth2.predict(X_test)
acc2 = accuracy_score(y_test, y_pred2)

print(f"Precisión con max_depth=2: {acc2 * 100:.2f}%")
print("Reglas obtenidas")
print(export_text(tree_depth2, feature_names=list(wine.feature_names)))

print("\n" + "="*50 + "\n")

print("--- 2. Prueba variando max_depth ---")
for depth in [1, 2, 3, 4, 5, None]:
    tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
    tree.fit(X_train, y_train)
    y_pred = tree.predict(X_test)
    acc = accuracy_score(y_test, tree.predict(X_test))
    print(f"max_depth: {depth} | Profundidad real: {tree.get_depth()} | Precisión: {acc * 100:.2f}%")

print("\n" + "=" * 50 + "\n")

print("--- 3. Reglas sin limitación de profundidad (max_depth=None) ---")

tree_full = DecisionTreeClassifier(max_depth=None, random_state=42)
tree_full.fit(X_train, y_train)
print(export_text(tree_full, feature_names=list(wine.feature_names)))