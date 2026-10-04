# 🌦️ Rasa Weather Chatbot

A conversational weather chatbot built using **Rasa, Python, and the OpenWeather API**.

The chatbot understands natural-language weather queries, identifies the requested city, stores the city using Rasa slots, connects to the OpenWeather REST API through a custom action, and returns current weather information.

## 🚀 Features

- 💬 Natural-language weather queries
- 🎯 Intent recognition using Rasa NLU
- 🏷️ City entity extraction
- 🧠 Slot filling to store the current city
- 🔄 Conversation context management
- 🔁 Updates the city slot when the user changes the city
- 💾 Session configuration with slot carry-over
- ⚙️ Custom Rasa actions
- 🌐 OpenWeather REST API integration
- 🌡️ Current weather condition, temperature, and feels-like temperature

## 🛠️ Technologies Used

- Python
- Rasa 3.6.21
- Rasa SDK 3.6.2
- Rasa NLU
- OpenWeather API
- REST API
- Requests
- YAML
- Git & GitHub

## 🔄 Project Flow

```text
User Query
     ↓
Rasa NLU
     ↓
Intent & Entity Recognition
     ↓
City Slot
     ↓
Custom Action
     ↓
OpenWeather API
     ↓
Weather Data
     ↓
Bot Response
💬 Example Queries

The chatbot can understand queries such as:

"What is the weather in Mumbai?"
"Tell me the weather of Delhi"
"What's the weather in Chennai?"
"What is the weather in Jammu?"
"What is the weather in Punjab?"
🧠 Slot Filling & Session Persistence

The chatbot uses a city slot to store the city mentioned by the user.

For example:

User: What is the weather in Mumbai?

Bot: Weather information for Mumbai

User: Actually, tell me about Delhi.

Bot: Weather information for Delhi

User: What about Chennai?

Bot: Weather information for Chennai

When the user mentions a new city, the city slot is updated with the new value. This allows the chatbot to maintain the latest city as conversation context.

The project also uses Rasa session configuration:

session_config:
  session_expiration_time: 60
  carry_over_slots_to_new_session: true

This allows slot information to be carried over into a new session according to the configured Rasa session behavior.

⚙️ Custom Action

The chatbot uses a custom Rasa action:

get_weather_update

The custom action:

Gets the city from the city slot.
Sends the city to the weather function.
Calls the OpenWeather API.
Extracts the weather condition.
Extracts the temperature.
Extracts the feels-like temperature.
Sends the weather information back to the user.
🌐 OpenWeather API Integration

The chatbot uses the OpenWeather REST API to retrieve weather information.

The integration follows this flow:

City
 ↓
OpenWeather API
 ↓
JSON Response
 ↓
Python
 ↓
Rasa Custom Action
 ↓
Bot Response

⚠️ Never expose your actual OpenWeather API key in your source code or GitHub repository.

📂 Project Structure
Rasa-weather-chatbot/
│
├── actions/
│   ├── __init__.py
│   ├── actions.py
│   └── weather.py
│
├── data/
│   ├── nlu.yml
│   ├── rules.yml
│   └── stories.yml
│
├── tests/
│   └── test_stories.yml
│
├── config.yml
├── credentials.yml
├── domain.yml
├── endpoints.yml
├── .gitignore
└── README.md
⚙️ Setup
1. Clone the repository
git clone https://github.com/Nishiweb3/Rasa-weather-chatbot.git
cd Rasa-weather-chatbot
2. Create a virtual environment
py -3.10 -m venv venv

Activate it on Windows:

venv\Scripts\activate
3. Install dependencies
pip install rasa==3.6.21
pip install rasa-sdk==3.6.2
pip install requests
4. Configure the OpenWeather API

Add your OpenWeather API key to the weather configuration.

Do not upload your actual API key to GitHub.

5. Train the Rasa model
rasa train
6. Start the action server
rasa run actions
7. Start the chatbot

Open another terminal and run:

rasa shell
🧪 Testing

Try:

What is the weather in Mumbai?

Then change the city:

Actually, tell me about Delhi.

Then:

What about Chennai?

This demonstrates city slot updating and conversation context.

📚 What I Learned

Through this project, I learned how to:

Build a chatbot using Rasa
Create and train intents
Extract entities from user messages
Use slots to store conversation information
Maintain conversation context
Update slot values when the user changes their input
Work with Rasa session configuration
Create custom actions
Connect a chatbot to an external REST API
Process JSON API responses
Manage a project using Git and GitHub
🔮 Future Improvements
🌍 Support for more locations
📅 Weather forecasts
🌧️ Rain probability
🌡️ Minimum and maximum temperature
⚠️ Better API error handling
📍 Location-based weather
🔐 Improved API key management
👩‍💻 Author

Nishita

B.Tech – Blockchain Engineering
CGC University