# Calorie Tracker

A Streamlit-based calorie tracker using OpenAI's vision-capable GPT model to estimate calories from meal photos.

## Features
- Upload meal images and estimate total calories per meal.
- Select date and meal type (Breakfast, Lunch, Dinner).
- Log calories per meal and display daily totals in a calendar-style table.

## Project Structure
Calorie-tracker/
   ├── .gitignore
   ├── README.md
   ├── requirements.txt
   ├── .env.example
   └── src/
   └── calorie_tracker/
   ├── init.py
   ├── main.py
   └── utils.py
## Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/calorie-tracker.git
   cd calorie-tracker
2.Create and activate a virtual environment:
    python -m venv env
    source env/bin/activate  # or `env\\Scripts\\activate` on Windows
3.Install dependencies:
    pip install -r requirements.txt
4.Copy .env.example to .env and fill in your OpenAI API key:
    cp .env.example .env
5.Run the app:
    streamlit run src/calorie_tracker/main.py
6.Environment Variables
   See .env.example.
