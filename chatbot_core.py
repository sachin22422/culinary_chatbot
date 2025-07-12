import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Nutrient to ingredient mapping
nutrient_map = {
    "vitamin c": ["orange", "lemon", "lime", "bell pepper", "broccoli", "strawberry", "kiwi"],
    "protein": ["chicken", "lentils", "tofu", "beans", "quinoa", "eggs"],
    "fiber": ["oats", "beans", "lentils", "whole wheat", "broccoli"],
    "iron": ["spinach", "red meat", "lentils", "tofu", "pumpkin seeds"],
    "calcium": ["milk", "cheese", "yogurt", "tofu", "kale"],
}

# Ingredient substitutions
substitutions = {
    "sugar": ["honey", "maple syrup", "stevia", "dates"],
    "butter": ["olive oil", "coconut oil", "ghee", "applesauce"],
    "cream": ["coconut milk", "greek yogurt", "cashew cream"],
    "egg": ["flaxseed meal", "chia seeds", "applesauce", "banana"],
}

# NEW: Simple knowledge base for health benefits
health_benefits_info = {
    "turmeric": "Turmeric contains curcumin, a compound with powerful anti-inflammatory and antioxidant properties. It's often used in traditional medicine.",
    "cardamom": "Cardamom is rich in antioxidants and may help with digestive problems, lower blood pressure, and fight inflammation.",
    "ginger": "Ginger is well-known for its ability to soothe nausea and indigestion. It also has strong anti-inflammatory and antioxidant effects.",
    "quinoa": "Quinoa is a complete protein, meaning it contains all nine essential amino acids. It's also high in fiber, magnesium, B vitamins, iron, and potassium.",
}

# Load and preprocess recipe data
def load_data():
    # --- Load OLD recipes ---
    recipe_data_path = os.path.join(os.path.dirname(__file__), "recipe_data_2.csv")
    old_df = pd.read_csv(recipe_data_path)
    old_df.dropna(subset=["Ingredients", "Recipe Name"], inplace=True)
    old_df["Recipe URL"] = old_df.get("Recipe URL", "https://example.com")  # fallback if column missing
    old_df["full_text"] = old_df["Recipe Name"] + " " + old_df["Ingredients"]

    # --- Load NEW recipes (merged from general + phrase) ---
    general_df = pd.read_csv("RecipeDB_general.csv")
    phrase_df = pd.read_csv("RecipeDB_ingredient_phrase.csv")

    phrase_df['ingredient_Phrase'] = phrase_df['ingredient_Phrase'].fillna('')
    grouped_ingredients = phrase_df.groupby('recipe_no')['ingredient_Phrase'].apply(lambda x: ', '.join(x)).reset_index()

    merged_df = pd.merge(general_df, grouped_ingredients, left_on='Recipe_id', right_on='recipe_no', how='inner')

    # Standardize column names
    merged_df = merged_df.rename(columns={
        "ingredient_Phrase": "Ingredients",
        "Recipe_id": "RecipeID",
        "servings": "Servings",
        "cook_time": "Total Time"
    })
    merged_df["Recipe Name"] = "Recipe #" + merged_df["RecipeID"].astype(str)
    merged_df["Recipe URL"] = "https://example.com/recipe/" + merged_df["RecipeID"].astype(str)
    merged_df.dropna(subset=["Ingredients"], inplace=True)
    merged_df["full_text"] = merged_df["Recipe Name"] + " " + merged_df["Ingredients"]

    # --- Combine both ---
    common_columns = ["Recipe Name", "Recipe URL", "Ingredients", "Total Time", "Servings", "full_text"]
    combined_df = pd.concat([
        old_df[common_columns],
        merged_df[common_columns]
    ], ignore_index=True)

    return combined_df


# Build TF-IDF vectorizer
def build_vectorizer(df):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df["full_text"])
    return vectorizer, tfidf_matrix

# Expand nutrient queries
def expand_query(query):
    query_lower = query.lower()
    for nutrient, ingredients in nutrient_map.items():
        if nutrient in query_lower:
            return query + " " + " ".join(ingredients)
    return query

# Find recipe matches
def get_recipe_matches(query, df, vectorizer, tfidf_matrix, top_n=3):
    expanded_query = expand_query(query)
    query_vec = vectorizer.transform([expanded_query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = similarities.argsort()[-top_n:][::-1]
    return df.iloc[top_indices]

# Suggest ingredient substitutions
def get_substitution(ingredient):
    return substitutions.get(ingredient.lower(), [])

# NEW: Get information from the knowledge base
def get_health_info(query):
    query_lower = query.lower()
    for keyword, info in health_benefits_info.items():
        if keyword in query_lower:
            return info
    return None