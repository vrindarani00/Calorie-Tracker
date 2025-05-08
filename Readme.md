
````markdown
# Calorie Tracker

A Streamlit–based app that uses OpenAI’s vision-capable GPT model to estimate calories from meal photos.

## 🚀 Features
- **Photo-based Estimation**  
  Upload a meal image and get per-item and total calorie estimates.
- **Meal Logging**  
  Pick a date and meal type (Breakfast, Lunch, Dinner) and record your estimates.
- **Daily Overview**  
  See all meals and daily totals in a simple calendar-style table.

## 🛠️ Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/calorie-tracker.git
   cd calorie-tracker
````

2. **Create & activate a virtual environment**

   ```bash
   python -m venv env
   # macOS/Linux
   source env/bin/activate
   # Windows
   env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   ```bash
   cp .env.example .env
   ```

   Then add your API key to `.env`:

   ```
   OPENAI_API_KEY=sk-...
   ```

5. **Run the app**

   ```bash
   streamlit run src/calorie_tracker/main.py
   ```

   Open your browser at `http://localhost:8501`.

## 📖 Environment Variables

See `.env.example` for required settings:

```
OPENAI_API_KEY=<your-openai-key>
```

---

Demo:
https://github.com/user-attachments/assets/7a02f6d2-7892-4cc8-b473-1a721abbdf59
```




