from sklearn.datasets import load_iris
iris = load_iris(as_frame=True)
species_column = iris.target.replace(dict(enumerate(iris.target_names)))
df = iris.data.assign(species=species_column)
print(df.groupby("species")["petal length (cm)"].mean())