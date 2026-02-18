# Affichage des attaques 
from script import df
attaques = df[df["label"] == 1]
print("Affichage des lignes correspondant à des attaques :")
print(attaques)
