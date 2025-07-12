# Import the new function
from chatbot_core import load_data, build_vectorizer, get_recipe_matches, get_substitution, get_health_info

df = load_data()
vectorizer, tfidf_matrix = build_vectorizer(df)

if __name__ == "__main__":
    print("\n🍽️  Culinary Culture Conversational Assistant")
    print("I can help with recipes, substitutions, and health benefits of ingredients.")
    print("Type 'exit' to quit\n")

    while True:
        query = input("👤 You: ").strip()
        if query.lower() == "exit":
            break

        query_lower = query.lower()

        info = get_health_info(query_lower)
        if info:
            print(f"🤖 {info}\n")
            continue

        if "replace" in query_lower or "substitute" in query_lower:
            found_substitution = False
            for word in query_lower.split():
                subs = get_substitution(word)
                if subs:
                    print(f"🤖 Alternatives for '{word}': {', '.join(subs)}\n")
                    found_substitution = True
                    break
            if not found_substitution:
                print("🤖 Sorry, I don't have a substitution for that.\n")
            continue

        matches = get_recipe_matches(query, df, vectorizer, tfidf_matrix)
        if matches.empty:
            print("🤖 Sorry, I couldn't find any recipes matching your query.\n")
        else:
            print("\n🤖 Here are the top recipe matches I found:")
            for _, row in matches.iterrows():
                print(f"- {row['Recipe Name']}")
                print(f"  🔗 {row['Recipe URL']}\n")
