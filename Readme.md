Thought for 9 seconds


```markdown
# Calorie Tracker

A **Streamlit**–based calorie tracker that uses OpenAI’s vision-capable GPT model to estimate calories from meal photos.

## 🚀 Features
- **Photo-based Estimation**  
  Upload a meal image and get per-item and total calorie estimates.
- **Meal Logging**  
  Pick a date and meal type (Breakfast, Lunch, Dinner) and record your estimates.
- **Daily Overview**  
  See all meals and daily totals in a simple calendar-style table.

---

## 📂 Project Structure

```

Calorie-tracker/
├── .gitignore
├── README.md
├── requirements.txt
├── .env.example
└── src/
└── calorie\_tracker/
├── **init**.py
├── main.py       # Streamlit app entry point
└── utils.py      # Image handling & API helpers

````

---

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

   Edit `.env` and add your OpenAI API key:

   ```
   OPENAI_API_KEY=sk-...
   ```

5. **Run the app**

   ```bash
   streamlit run src/calorie_tracker/main.py
   ```

   Then open your browser at `http://localhost:8501`.

---

## 📖 Environment Variables

See `.env.example` for all required settings:

```
# .env.example
OPENAI_API_KEY=<your-openai-key>
```

---

> **Tip:** To include a short demo video in your `README.md`, place `demo.mp4` in your repo and add:
>
> ```html

https://github.com/user-attachments/assets/01a04d15-c8fb-4013-9176-9de30e8a57b4


> <video width="640" controls>
>   <source src="demo.mp4" type="video/mp4">
>   Your browser does not support the video tag.
> </video>
> ```

```
```
