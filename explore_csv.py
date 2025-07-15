import pandas as pd

general_df = pd.read_csv("RecipeDB_general.csv")
flavor_df = pd.read_csv("RecipeDB_ingredient_flavor.csv")
phrase_df = pd.read_csv("RecipeDB_ingredient_phrase.csv")

print("\n--- RecipeDB_general.csv ---\n")
print(general_df.head())

print("\n--- RecipeDB_ingredient_flavor.csv ---\n")
print(flavor_df.head())

print("\n--- RecipeDB_ingredient_phrase.csv ---\n")
print(phrase_df.head())
