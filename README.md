Culinary Assistant AI
A sophisticated, AI-powered chatbot designed to be your ultimate kitchen companion. This is more than just a recipe finder; it's a culinary expert that understands natural language to help you with everything from meal planning and nutritional queries to ingredient substitutions and cooking knowledge.
![alt text](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)

![alt text](https://img.shields.io/badge/FastAPI-0.95%2B-green?style=for-the-badge&logo=fastapi)

![alt text](https://img.shields.io/badge/SciKit--Learn-1.2%2B-orange?style=for-the-badge&logo=scikit-learn)
This project leverages a powerful backend to parse complex user requests and deliver precise, helpful answers, making your culinary journey easier and more inspiring.
(This is your provided screenshot. For an even better demo, consider recording a short GIF of the interaction and replacing this image.)
🌟 Key Features
The Culinary Assistant is built to handle a wide array of food-related questions. Its core strengths are categorized below:
1. Intelligent Recipe Search
Go beyond simple keywords. The chatbot understands context to find what you're looking for.
Direct Search: "lentil soup", "egyptian flatbread"
Ingredient-Based Search: "recipes with carrots and celery", "chickpea recipes"
2. Nutritional & Health-Based Queries
Plan your meals according to your health goals. The assistant can filter recipes based on detailed nutritional information.
Nutrient-Specific: "high protein meals", "iron rich recipes"
Vitamin-Focused: "vitamin a recipes", "high vitamin c food"
3. Culinary Knowledge & Substitutions
Stuck in the middle of a recipe? Get instant help with substitutions and culinary facts.
Ingredient Substitutions: "what can I substitute for butter?", "replace egg in a cake"
Health Benefits: "what are the benefits of turmeric?", "why is quinoa good for you?"
4. Advanced Filtering & Personalization
Tailor your search results using powerful filters and dietary preferences.
Cuisine & Time: Filter by "Indian", "Italian", or cooking time like "Under 30 min".
Dietary Needs: Set preferences like "Vegan" or "Gluten-Free" for personalized recommendations across all searches.
🛠️ Tech Stack & Architecture
This project uses a modern, efficient tech stack to deliver a fast and responsive user experience.
Backend: Python
API Framework: FastAPI for high-performance asynchronous request handling.
Web Server: Uvicorn as the lightning-fast ASGI server.
Data Processing: Pandas for managing and searching the extensive recipe dataset.
Natural Language Processing: Scikit-learn (TF-IDF Vectorizer) for transforming user queries into a machine-readable format to find the most relevant recipes.
Frontend: A clean and simple interface built with HTML and CSS.
🚀 Getting Started
Follow these instructions to set up and run the Culinary Assistant on your local machine.
Prerequisites
Python 3.8+
Git
Installation & Setup
Clone the repository:
git clone https://github.com/sachin22422/culinary_chatbot.git
cd culinary_chatbot
Create and activate a virtual environment:
On Windows:
python -m venv venv
.\venv\Scripts\activate
On macOS/Linux:
python3 -m venv venv
source venv/bin/activate
Install the required dependencies:
(First, ensure you have a requirements.txt file. If not, create one with pip freeze > requirements.txt after installing the packages below.)
pip install fastapi uvicorn python-multipart pandas scikit-learn
Running the Application
Start the server:
From the root directory of the project, run the following command. The --reload flag will automatically restart the server when you make changes to the code.
uvicorn app:app --reload
You will see a confirmation that the server is running:
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [xxxx] using WatchFiles
Total recipes loaded: 118083. The chatbot is ready.
Open the application:
Open your web browser and navigate to http://127.0.0.1:8000. You can now interact with your Culinary Assistant!
