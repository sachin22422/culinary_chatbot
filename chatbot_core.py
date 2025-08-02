import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

nutrient_map = {
    "vitamin a": ["carrot", "sweet potato", "spinach", "kale", "egg", "butter"],
    "vitamin c": ["orange", "lemon", "lime", "bell pepper", "broccoli", "strawberry", "kiwi"],
    "protein": ["chicken", "lentils", "tofu", "beans", "quinoa", "eggs", "beef", "fish", "shrimp"],
    "fiber": ["oats", "beans", "lentils", "whole wheat", "broccoli", "chickpea"],
    "iron": ["spinach", "red meat", "lentils", "tofu", "pumpkin seeds", "beef"],
    "calcium": ["milk", "cheese", "yogurt", "tofu", "kale"],
}
vitamin_ingredients = []
for key, ingredients in nutrient_map.items():
    if key.startswith("vitamin"):
        vitamin_ingredients.extend(ingredients)
nutrient_map["vitamin"] = list(set(vitamin_ingredients))

ingredient_to_nutrient_map = {}
for nutrient, ingredients in nutrient_map.items():
    for ingredient in ingredients:
        ingredient_to_nutrient_map[ingredient] = nutrient

substitutions = {
    "sugar": ["honey", "maple syrup", "stevia", "dates"],
    "butter": ["olive oil", "coconut oil", "ghee", "applesauce"],
    "cream": ["coconut milk", "greek yogurt", "cashew cream"],
    "egg": ["flaxseed meal", "chia seeds", "applesauce", "banana"],
}
health_benefits_info = {
    "turmeric": "Turmeric is a spice with powerful anti-inflammatory and antioxidant properties.",
    "ginger": "Ginger is known to help with nausea and indigestion.",
    "quinoa": "Quinoa is a complete protein, containing all nine essential amino acids."
}

translations_db = {
    'hi': { 
        'hello': 'नमस्ते', 'recipe': 'रेसिपी', 'thank you': 'धन्यवाद', 'soup': 'सूप', 'chicken': 'चिकन',
        'Here are some recipes I found for you:': 'यहाँ आपके लिए कुछ रेसिपी हैं:',
        "I couldn't find any recipes matching your query. Please try different keywords!": "मुझे आपकी क्वेरी से मेल खाने वाली कोई रेसिपी नहीं मिली। कृपया दूसरे कीवर्ड्स के साथ प्रयास करें!",
        "Time:": "समय:", "Servings:": "सर्विंग्स:"
    },
    'en': { 
        'नमस्ते': 'hello', 'रेसिपी': 'recipe', 'धन्यवाद': 'thank you', 'सूप': 'soup', 'चिकन': 'chicken',
        'चावल': 'rice', 'पनीर': 'paneer', 'दाल': 'lentil', 'मसाला': 'spice'
    }
}


def load_data():
    """
    Loads, merges, and correctly populates the 'Dietary' column for filtering,
    including special handling for a comprehensive set of dietary preferences.
    """
    try:
        base_dir = os.path.dirname(__file__)
        general_path = os.path.join(base_dir, 'RecipeDB_general.csv')
        ingredients_path = os.path.join(base_dir, 'RecipeDB_ingredient_phrase.csv')

        general_df = pd.read_csv(general_path, encoding='utf-8', on_bad_lines='skip', low_memory=False)
        ingredients_df = pd.read_csv(ingredients_path, encoding='utf-8', on_bad_lines='skip')

        general_df.columns = general_df.columns.str.strip().str.lower()
        ingredients_df.columns = ingredients_df.columns.str.strip().str.lower()
        
        diet_cols = {
            'vegan': 'Vegan',
            'ovo_lacto_vegetarian': 'Vegetarian',
            'pescetarian': 'Pescetarian',
            'keto_friendly': 'Keto',
            'gluten_free': 'Gluten-Free',
            'dairy_free': 'Dairy-Free',
            'low_carb': 'Low-Carb',
            'low_fat': 'Low-Fat',
            'nut_free': 'Nut-Free'
        }

        general_df['dietary'] = ''
        for col, tag in diet_cols.items():
            if col in general_df.columns:
                general_df[col] = pd.to_numeric(general_df[col], errors='coerce')
                general_df.loc[general_df[col] == 1, 'dietary'] += tag + ' '
        
        is_vegetarian_type = general_df['dietary'].str.contains('Vegan|Vegetarian|Pescetarian', case=False, na=False)
        general_df.loc[~is_vegetarian_type, 'dietary'] += 'Non-Vegetarian '

        required_cols = ['recipe_id', 'recipe_title', 'total_time', 'servings', 'url', 'region', 'dietary']

        if not all(col in general_df.columns for col in required_cols):
            missing = [col for col in required_cols if col not in general_df.columns]
            raise ValueError(f"Missing required columns in RecipeDB_general.csv: {missing}")

        recipes_df = general_df[required_cols].copy()
        
        recipes_df = recipes_df.rename(columns={
            'recipe_id': 'RecipeID',
            'recipe_title': 'Recipe Name',
            'total_time': 'Total Time',
            'servings': 'Servings',
            'url': 'Recipe URL',
            'region': 'Cuisine',
            'dietary': 'Dietary'
        })

        ingredients_df['ingredient_phrase'] = ingredients_df['ingredient_phrase'].fillna('')
        grouped_ingredients = ingredients_df.groupby('recipe_no')['ingredient_phrase'].apply(lambda x: ', '.join(x))
        grouped_ingredients = grouped_ingredients.rename('Ingredients')
        
        merged_df = pd.merge(recipes_df, grouped_ingredients, left_on='RecipeID', right_on='recipe_no', how='left')
        
        for col in ['Ingredients', 'Cuisine', 'Dietary']:
            merged_df[col] = merged_df[col].fillna('')

        merged_df['Recipe Name'] = merged_df['Recipe Name'].fillna('')

        merged_df['full_text'] = (
            merged_df['Recipe Name'] + ' ' +
            merged_df['Ingredients'] + ' ' +
            merged_df['Cuisine'] + ' ' +
            merged_df['Dietary']
        ).str.lower()
        
        print(f"Total recipes loaded: {len(merged_df)}. The chatbot is ready.")
        return merged_df

    except Exception as e:
        print(f"CRITICAL ERROR during data loading: {e}")
        return pd.DataFrame()
def build_vectorizer(df):
    if df.empty or df['full_text'].str.strip().eq('').all():
        vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
        return vectorizer, vectorizer.fit_transform([])
    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(df['full_text'])
    return vectorizer, tfidf_matrix

def expand_query(query):
    original_query = query.lower()
    expanded_terms = set()
    for key, ingredients in nutrient_map.items():
        if key in original_query:
            expanded_terms.update(ingredients)
    for word in original_query.split():
        if word in ingredient_to_nutrient_map:
            expanded_terms.add(ingredient_to_nutrient_map[word])
    return original_query + " " + " ".join(expanded_terms)

def get_recipe_matches(query, df, vectorizer, tfidf_matrix, user_profile=None, filters=None, top_n=5):
    if df.empty or tfidf_matrix.shape[0] == 0:
        return pd.DataFrame()
    filtered_df = df.copy()

    if user_profile and user_profile.diet:
        if 'Dietary' in filtered_df.columns:
            filtered_df = filtered_df[filtered_df['Dietary'].str.contains(user_profile.diet, case=False, na=False)]

    if filters:
        if filters.cuisine and 'Cuisine' in filtered_df.columns:
            filtered_df = filtered_df[filtered_df['Cuisine'].str.contains(filters.cuisine, case=False, na=False)]
        if filters.cook_time and 'Total Time' in filtered_df.columns:
            filtered_df['Total Time'] = pd.to_numeric(filtered_df['Total Time'], errors='coerce')
            filtered_df = filtered_df.dropna(subset=['Total Time'])
            filtered_df = filtered_df[filtered_df['Total Time'] <= filters.cook_time]

    if filtered_df.empty:
        return pd.DataFrame()

    filtered_indices = filtered_df.index
    filtered_tfidf_matrix = tfidf_matrix[filtered_indices]

    expanded_query = expand_query(query)
    query_vec = vectorizer.transform([expanded_query])
    
    similarities = cosine_similarity(query_vec, filtered_tfidf_matrix).flatten()
    
    if similarities.max() == 0:
        return pd.DataFrame()
        
    top_indices_in_filtered_df = similarities.argsort()[-top_n:][::-1]
    
    return filtered_df.iloc[top_indices_in_filtered_df]

def get_substitution(ingredient):
    return substitutions.get(ingredient.lower(), [])

def get_health_info(query):
    for keyword, info in health_benefits_info.items():
        if keyword in query.lower():
            return info
    return None

def translate_text(text, src_lang, dest_lang):
    if not isinstance(text, str): return text

    translation_map = translations_db.get(dest_lang, {})
    if text in translation_map: return translation_map[text]

    words = text.split()
    translated_words = [translation_map.get(word, word) for word in words]
    
    return " ".join(translated_words)