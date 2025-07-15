culinary_chatbot
An intelligent, AI-powered chatbot for recipe discovery, ingredient substitutions, and nutritional advice. Built with a FastAPI backend, a TF-IDF model for NLP, and a dynamic vanilla JavaScript frontend.
(Note: You should replace the placeholder image link above with a real screenshot of your running application for the best presentation.)
✨ Features
This chatbot is designed to be a lightweight yet powerful kitchen assistant with the following features:
Recipe Discovery: Find recipes from a large dataset by searching for ingredients, recipe names, or cuisine types.
Intelligent Search: Ask for "high protein meals" or "vitamin a rich foods," and the chatbot will automatically expand its search to include relevant ingredients.
Ingredient Substitution: Ask for a substitute for common ingredients like "sugar," "butter," or "eggs."
Health Benefits: Get quick information on the health benefits of key ingredients like "turmeric" or "ginger."
User Personalization: The chatbot remembers your name and dietary preferences (e.g., Vegan, Vegetarian) to tailor recipe results.
Dynamic UI: Includes a Light/Dark mode toggle and a "Reset Profile" option for easy testing.
Voice Commands: Use the microphone button to speak your query directly into the chat.
Multilingual Support: Supports both English and Hindi for queries and responses.
Recipe Filtering: Filter your search by cuisine type or maximum cooking time.
🔧 Tech Stack
Backend: Python 3, FastAPI, Uvicorn
NLP & Data: Scikit-learn (TF-IDF, Cosine Similarity), Pandas
Frontend: HTML5, CSS3, Vanilla JavaScript
APIs: Web Speech API (for voice input)
🚀 Getting Started
Follow these instructions to get a local copy up and running.
Prerequisites
Python 3.10+
Git
Installation
Clone the repository:
Generated sh
git clone https://github.com/sachin22422/culinary_chatbot.git
cd culinary_chatbot
Use code with caution.
Sh
Create a virtual environment:
This keeps the project's dependencies isolated.
On Windows:
Generated sh
python -m venv venv
.\venv\Scripts\activate
Use code with caution.
Sh
On macOS/Linux:
Generated sh
python3 -m venv venv
source venv/bin/activate
Use code with caution.
Sh
Create a requirements.txt file:
Create a new file named requirements.txt in the main project folder.
Copy and paste the following lines into it:
Generated txt
fastapi
uvicorn[standard]
scikit-learn
pandas
python-multipart
Use code with caution.
Txt
Install the dependencies:
Generated sh
pip install -r requirements.txt
Use code with caution.
Sh
Running the Application
Start the FastAPI server:
Generated sh
uvicorn app:app
Use code with caution.
Sh
Do not use the --reload flag for normal use.
Open the chatbot:
Open your web browser and navigate to http://127.0.0.1:8000.
The chatbot interface will load, and you can start interacting with it.
💡 How to Use
Once the chatbot is running in your browser, you can try the following queries:
To find recipes: "chicken and rice", "lentil soup"
For nutrient-based search: "vitamin a rich foods", "high protein meals"
For substitutions: "substitute for butter"
For health info: "benefits of turmeric"
To test filters: Select a cuisine (e.g., "Indian") from the dropdown, then search for a recipe.
To test personalization:
Click the "reset" icon (🔄) in the header.
The page will reload, and a welcome modal will appear.
Enter your name and select a dietary preference like "Vegan".
Search for a general term like "soup recipes". The results will now be filtered.
📂 Project Structure
Generated code
/culinary_chatbot
├── .venv/                  # Virtual environment folder
├── app.py                  # FastAPI application setup and API routes
├── chatbot_core.py         # Core NLP logic, data loading, and search functions
├── index.html              # Frontend UI, styling, and JavaScript logic
├── main.py                 # (Optional) Command-line runner for the bot
├── requirements.txt        # List of Python dependencies
└── *.csv                   # Recipe data files
└── *.json                  # Recipe instruction files
