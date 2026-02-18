from script import df

print("\nActivité 3 :\n")
print("Futuré la plus variable ")

stds = df.drop(columns=["label"]).std()
feature_trace = stds.idxmax()
print(feature_trace)
print("Ecart-type : ", stds.max())