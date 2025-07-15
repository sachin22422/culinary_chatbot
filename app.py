from fastapi import FastAPI
from fastapi.responses import FileResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List

from chatbot_core import (
    load_data, 
    build_vectorizer, 
    get_recipe_matches,
    get_substitution, 
    get_health_info, 
    translate_text
)

class UserProfile(BaseModel):
    name: Optional[str] = None
    diet: Optional[str] = None

class Filters(BaseModel):
    cuisine: Optional[str] = None
    cook_time: Optional[int] = None

class AskRequest(BaseModel):
    query: str
    user_profile: Optional[UserProfile] = None
    filters: Optional[Filters] = None
    language: Optional[str] = 'en'

app = FastAPI()

df = load_data()
vectorizer, tfidf_matrix = build_vectorizer(df)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return Response(status_code=204)

@app.post("/ask")
def ask(request: AskRequest):
    query = request.query
    lang = request.language

    if lang != 'en' and query:
        query = translate_text(query, src_lang=lang, dest_lang='en')

    query_lower = query.lower()
    
    info = get_health_info(query_lower)
    if info:
        if lang != 'en':
            info = translate_text(info, src_lang='en', dest_lang=lang)
        return {"type": "info", "message": info}

    if "replace" in query_lower or "substitute" in query_lower:
        for word in query_lower.split():
            subs = get_substitution(word)
            if subs:
                response = { "type": "substitution", "ingredient": word, "alternatives": subs }
                if lang != 'en':
                    response['alternatives'] = [translate_text(alt, 'en', lang) for alt in subs]
                return response
        message = "Sorry, I couldn't find a specific substitution for that."
        if lang != 'en':
            message = translate_text(message, 'en', lang)
        return {"type": "info", "message": message}

    matches = get_recipe_matches(query_lower, df, vectorizer, tfidf_matrix, request.user_profile, request.filters)
    
    if matches.empty:
        message = "I couldn't find any recipes matching your query. Please try different keywords!"
        if lang != 'en':
            message = translate_text(message, 'en', lang)
        return {"type": "info", "message": message}

    results = []
    for _, row in matches.iterrows():
        name = row["Recipe Name"]
        if lang != 'en':
            name = translate_text(name, 'en', lang)
        
        results.append({
            "name": name,
            "url": row["Recipe URL"],
            "ingredients": row["Ingredients"],
            "time": row["Total Time"],
            "servings": row["Servings"]
        })

    return {"type": "recipes", "results": results}