# Important des modules
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification


# Génération d'un dataset cybersécurité simulé.
X, y = make_classification(
n_samples=3000,
n_features=12,
n_informative=6,
n_redundant=2,
weights=[0.95, 0.05],
flip_y=0.01,
random_state=42
)
cols = [f"feature_{i}" for i in range(X.shape[1])]
df = pd.DataFrame(X, columns=cols)
df["label"] = y

