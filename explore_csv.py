import pandas as pd

# Load the new recipe files
general_df = pd.read_csv("RecipeDB_general.csv")
flavor_df = pd.read_csv("RecipeDB_ingredient_flavor.csv")
phrase_df = pd.read_csv("RecipeDB_ingredient_phrase.csv")

# Show the first 5 rows of each file
print("\n--- RecipeDB_general.csv ---\n")
print(general_df.head())

print("\n--- RecipeDB_ingredient_flavor.csv ---\n")
print(flavor_df.head())

print("\n--- RecipeDB_ingredient_phrase.csv ---\n")
print(phrase_df.head())
