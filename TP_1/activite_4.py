from script import df
from activite_3 import feature_trace
import matplotlib.pyplot as plt

print("\nActivité 4 :\n")
# Nous allons tracer le feature trouve dans l'activité 3 
plt.figure()
plt.hist(df[feature_trace], bins=30, color="skyblue", edgecolor="black")
plt.title(f"Distribution de {feature_trace}")
plt.xlabel("Valeur")
plt.ylabel("Fréquence")
plt.show()
plt.savefig("activite_4.png")



