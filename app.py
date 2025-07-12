from fastapi import FastAPI, Query
# Make sure to import the new get_health_info function
from chatbot_core import load_data, build_vectorizer, get_recipe_matches, get_substitution, get_health_info
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
df = load_data()
vectorizer, tfidf_matrix = build_vectorizer(df)

# Allow cross-origin requests so your index.html can talk to the server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins, you can restrict this in production
    allow_credentials=True,
    allow_methods=["*"], # Allows all HTTP methods
    allow_headers=["*"], # Allows all headers
)

@app.get("/ask")
def ask(query: str = Query(..., description="Ask a food-related question")):
    query_lower = query.lower()

    # --- The Core Logic ---
    # The order of these checks is important to handle user intent correctly.

    # 1. Check for specific health benefit/informational queries first.
    # This catches "what are the benefits of turmeric" before it becomes a recipe search.
    info = get_health_info(query_lower)
    if info:
        return {
            "type": "info",
            "message": info
        }

    # 2. Next, check for substitution queries.
    if "replace" in query_lower or "substitute" in query_lower:
        for word in query_lower.split():
            subs = get_substitution(word)
            if subs:
                return {
                    "type": "substitution",
                    "ingredient": word,
                    "alternatives": subs
                }
        # If the query had "substitute" but no match was found
        return {
            "type": "info", # Use the generic 'info' type for a simple message
            "message": "Sorry, I couldn't find a specific substitution for that. You can try asking for recipes that don't use the ingredient."
        }

    # 3. If neither of the above, default to a recipe search.
    matches = get_recipe_matches(query, df, vectorizer, tfidf_matrix)
    
    # Handle case where no recipes are found
    if matches.empty:
         return {
            "type": "info",
            "message": "I couldn't find any recipes matching your query. Please try different keywords!"
        }

    results = []
    for _, row in matches.iterrows():
        results.append({
            "name": row["Recipe Name"],
            "url": row["Recipe URL"],
            "ingredients": row["Ingredients"],
            "time": row["Total Time"],
            "servings": row["Servings"]
        })
        
    return {
        "type": "recipes",
        "results": results
    }