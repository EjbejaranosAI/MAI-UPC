import pandas as pd
import seaborn as sns

# matplotlib inline
import umap
from sklearn.preprocessing import StandardScaler

sns.set(style='white', context='notebook', rc={'figure.figsize': (14, 10)})

penguins = pd.read_csv(
    "https://github.com/allisonhorst/palmerpenguins/raw/5b5891f01b52ae26ad8cb9755ec93672f49328a8/data/penguins_size.csv")
penguins.head()

penguins = penguins.dropna()
penguins.species_short.value_counts()

sns.pairplot(penguins, hue='species_short')

reducer = umap.UMAP()

penguin_data = penguins[
    [
        "culmen_length_mm",
        "culmen_depth_mm",
        "flipper_length_mm",
        "body_mass_g",
    ]
].values
scaled_penguin_data = StandardScaler().fit_transform(penguin_data)
