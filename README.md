🧠🍳 Culinary Assistant AI

**Culinary Assistant AI** is a sophisticated, AI-powered chatbot designed to be your ultimate kitchen companion. It’s more than just a recipe finder—this intelligent assistant helps with meal planning, nutritional guidance, ingredient substitutions, and general culinary knowledge using natural language understanding.

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-0.95%2B-green?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/SciKit--Learn-1.2%2B-orange?style=for-the-badge&logo=scikit-learn" />
</div>

🌟 Key Features

The Culinary Assistant is designed to handle a wide array of food-related tasks and queries:

1. 🍽️ Intelligent Recipe Search
- Contextual Search: Understands natural language for smarter search results.
- Direct Queries: E.g., `"lentil soup"`, `"egyptian flatbread"`
- Ingredient-Based Queries: E.g., `"recipes with carrots and celery"`, `"chickpea recipes"`

2. 🥗 Nutritional & Health-Based Queries
- Plan meals based on health needs and fitness goals.
- Nutrient-Focused: `"high protein meals"`, `"iron rich recipes"`
- Vitamin-Specific: `"vitamin a recipes"`, `"high vitamin c food"`

3. 🧂 Culinary Knowledge & Substitutions
- Helps with mid-recipe adjustments and general culinary tips.
- Substitutions: `"what can I substitute for butter?"`, `"replace egg in a cake"`
- Health Benefits: `"why is turmeric good for you?"`, `"quinoa benefits"`

4. ⚙️ Advanced Filtering & Personalization
- Personalize results based on:
  - Cuisine: `"Indian"`, `"Italian"`, etc.
  - Time Constraints: `"Under 30 min"`
  - Dietary Preferences: `"Vegan"`, `"Gluten-Free"`

🛠️ Tech Stack

| Layer       | Technology |
|-------------|------------|
| Backend | Python |
| API     | FastAPI (asynchronous request handling) |
| Web Server | Uvicorn |
| NLP & Search | Scikit-learn (TF-IDF) |
| Data Handling | Pandas |
| Frontend | HTML + CSS |

🚀 Getting Started

Follow these steps to run the application on your local machine.

🔧 Prerequisites
- Python 3.8+
- Git

📦 Installation

1. Clone the repository:
   git clone https://github.com/sachin22422/culinary_chatbot.git
   cd culinary_chatbot

2. Create and activate a virtual environment:
   On Windows:
   python -m venv venv
   .\venv\Scripts\activate

   On macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate
   
3. Install dependencies:
   pip install fastapi uvicorn python-multipart pandas scikit-learn

> 💡 Tip: Run `pip freeze > requirements.txt` to generate the requirements file for production use.

▶️ Running the Application

From the project root:
uvicorn app:app --reload

You should see:
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [xxxx] using WatchFiles
Total recipes loaded: 118083. The chatbot is ready.

🌐 Access the Application

Open your browser and go to:
http://127.0.0.1:8000


📁 Project Structure (Simplified)

culinary_chatbot/
├── app.py               # FastAPI main app
├── data/                # Recipes dataset
├── utils/               # Utility functions
├── static/              # Frontend assets (HTML/CSS)
└── models/              # TF-IDF model and preprocessing



