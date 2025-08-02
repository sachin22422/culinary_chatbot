Culinary Assistant AI
An intelligent, interactive Culinary Assistant designed to help you discover recipes through natural conversation. It provides a seamless experience for finding meals based on ingredients, cuisine, dietary needs, and more, all within a clean and modern web interface.
<br>
<p align="center">
<img src="https://i.imgur.com/qUaP08J.png" alt="Culinary Assistant Interface" width="700"/>
</p>
✨ Key Features
Conversational AI: Utilizes Natural Language Processing to understand and respond to user queries in a human-like manner.
Advanced Search: Find recipes by name, ingredients, cuisine, or cooking time using the intuitive chat interface and filter dropdowns.
Voice-to-Text: Includes a speech recognition option for hands-free interaction.
Modern UI: A clean, responsive user interface with both Light & Dark modes.
Scalable Backend: Built with FastAPI and Uvicorn, ensuring high performance and asynchronous capabilities.
Robust Data Handling: Manages a large dataset of over 100,000 recipes efficiently using Pandas.
🚀 Getting Started
Follow these instructions to set up and run a local instance of the Culinary Assistant.
Prerequisites
Python 3.9+
pip package manager
Installation & Setup
Clone the Repository
Generated sh
git clone https://github.com/sachin22422/culinary_chatbot.git
cd culinary_chatbot
Use code with caution.
Sh
Create and Activate a Virtual Environment
Generated sh
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
Use code with caution.
Sh
Install Dependencies
It is recommended to first create a requirements.txt file. While your virtual environment is active, run: pip freeze > requirements.txt
Then, install the required packages:
Generated sh
pip install -r requirements.txt
Use code with caution.
Sh
Running the Application
Start the Server
Use Uvicorn to run the FastAPI application. The --reload flag enables hot-reloading for development.
Generated sh
uvicorn app:app --reload
Use code with caution.
Sh
Access the Application
Once the server is running, open your web browser and navigate to:
http://127.0.0.1:8000
📖 How to Use the Assistant
The interface is designed to be intuitive. Here’s how to interact with the chatbot:
Ask a Question:
Simply type your food-related question into the input box at the bottom that says "Ask a food question..." and press Enter or click the send icon (▶).
Use Filters for Specific Results:
Cuisine Filter: Use the "All Cuisines" dropdown to narrow your search to a specific cuisine (e.g., Italian, Mexican, Indian).
Time Filter: Use the "Any Time" dropdown to find recipes that can be prepared within a certain timeframe.
Use Your Voice:
Click the microphone icon (🎙️) to activate voice input. Speak your question clearly, and the chatbot will transcribe it for you.
Change the Theme:
Click the sun/moon icon (☀) in the top-right corner to toggle between light and dark modes.
Start a New Conversation:
Click the refresh icon (↺) in the top-right corner to clear the current chat and begin a new conversation.
Example Interactions
General query: "Can you find me a chicken recipe?"
Filtered query: Select "Italian" from the cuisine dropdown and ask, "I'm looking for a vegetarian pasta dish."
Voice query: Click the microphone and say, "Find me a dessert recipe that takes less than 30 minutes."
🧪 Testing
A suite of test cases has been developed to ensure the chatbot's reliability and the API's stability. To run the tests, use your preferred testing framework (e.g., pytest):
Generated sh
# (Example command, adjust as needed)
pytest
