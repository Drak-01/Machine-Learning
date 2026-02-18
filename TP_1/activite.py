from script import df
import matplotlib.pyplot as plt
import seaborn as sns


nb_attaques = (df["label"] == 1).sum()
print("Activité 1 :\n")
print("Nombre d'attaques : ", nb_attaques)

print("================================================================================")
print("\nActivité 2 :\n")
attaques = df[df["label"] == 1]
print("Affichage des lignes correspondant à des attaques :")
print(attaques)

print("================================================================================")
print("\nActivité 3 :\n")
print("Futuré la plus variable ")

stds = df.drop(columns=["label"]).std()
feature_trace = stds.idxmax()
print(feature_trace)
print("Ecart-type : ", stds.max())

print("================================================================================")
print("\nActivité 4 :\n")
# Nous allons tracer le feature trouve dans l'activité 3 
plt.figure()
plt.hist(df[feature_trace], bins=30, color="skyblue", edgecolor="black")
plt.title(f"Distribution de {feature_trace}")
plt.xlabel("Valeur")
plt.ylabel("Fréquence")
plt.show()
plt.savefig("activite_4.png")

