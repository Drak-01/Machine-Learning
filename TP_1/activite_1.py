# Compter les attaques
from script import df
nb_attaques = (df["label"] == 1).sum()
print("Nombre d'attaques : ", nb_attaques)