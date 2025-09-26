from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
iris = load_iris(as_frame=True)
species_column = iris.target.replace(dict(enumerate(iris.target_names)))
df = iris.data.assign(species=species_column)
print(df.groupby("species")["petal length (cm)"].mean())
df.hist(column="sepal length (cm)", by = "species", bins=20, sharex=False, sharey=False, layout = (1,3))
plt.suptitle("Sepal Length Distribution by Species")
plt.tight_layout()
plt.show()