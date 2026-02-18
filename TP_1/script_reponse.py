from script import df
print("\nVisualisation du dataset :")
print(df.head())
print("\nLe pourcentage des labels")
print(df["label"].value_counts(normalize=True))
print("\nStatistique descriptives ")
print(df.describe())