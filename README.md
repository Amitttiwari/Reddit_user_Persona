# 🧠 Reddit Persona Generator using Hugging Face Transformers

Welcome to the **Reddit Persona Generator** — a project where we turn public Reddit profiles into detailed, personality-rich user personas using artificial intelligence!

This project scrapes Reddit comments/posts from any user and analyzes them to generate a stylized **persona profile**, including:

✅ Interests  
✅ Personality Traits  
✅ Writing Style  
✅ Subreddits They Engage With  
✅ Real Quotes from their activity  
✅ Avatar & Summary Display  
✅ Saved Output in Text Files  

---

## 📌 What is a "User Persona"?

A **user persona** is a fictional but realistic representation of someone based on their behavior, interests, tone, and preferences. It’s widely used in:

- 🛍️ Marketing (customer profiling)
- 🧑‍💻 UX/UI Design (target audience)
- 🤖 NLP and AI analysis

In this case, we’re using **Reddit activity** as the data source and an AI model to understand the person behind the username.

---

## 🧰 Project Features

| Feature | Description |
|--------|-------------|
| 🧾 Input | Reddit user profile URL (e.g., `https://reddit.com/user/kojied`) |
| 🔍 Scraper | Fetches recent posts & comments using the Reddit API |
| 🧠 LLM | Generates persona using Hugging Face's `transformers` models |
| 📦 Output | Saves persona as a `.txt` file for every user |
| 🎨 UI | Clean Gradio interface with avatars, model selector, quote, and card layout |
| 📷 Avatar | Auto-generated with RoboHash (based on username) |
| 📄 Quote | Pulls a real quote from user’s comments |

---

## 💡 Why Use Hugging Face Transformers Instead of OpenAI API?

Great question! Here’s a simple comparison 👇

| Feature | OpenAI (e.g., GPT-4) | Hugging Face Transformers |
|--------|----------------------|----------------------------|
| ✅ Easy to Use | Yes | Yes |
| 💰 Free | ❌ No (paid API) | ✅ Yes (with open models) |
| 🔌 Works Offline | ❌ No | ✅ Yes |
| 🔐 API Keys Needed | ✅ Yes | ✅ (token-based or none if local) |
| 🎯 Instruction-following | ✅ Best with GPT-4 | ✅ With Mistral, Falcon, OpenChat |

**In This Project:**  
We chose **Hugging Face** to make it **open-source, free to use, and portable** — no API limits, no cost, and easy to deploy anywhere (including Hugging Face Spaces!).

---

## 📂 Folder Structure
```
reddit-user-persona/
│
├── app.py # Gradio interface
├── reddit_scraper.py # Reddit data fetching
├── persona_generator.py # LLM logic for persona generation
├── personas/ # Generated persona files (.txt)
├── requirements.txt # Python dependencies
├── .env # (Optional) Store Reddit API keys
└── README.md # This file!

```
---

## ⚙️ How to Run Locally

### 1. Clone the repository
```
git clone https://github.com/Amitttiwari/reddit-user-persona.git
cd reddit-user-persona
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Set up your Reddit credentials
Go to https://www.reddit.com/prefs/apps

Create a script-type app

Copy your client_id and client_secret

Option A: Use .env file (Recommended)
Create a file called .env:

```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
```
Option B: Set in terminal
```
export REDDIT_CLIENT_ID=your_client_id
export REDDIT_CLIENT_SECRET=your_client_secret
```
4. Run the app
```
python app.py
```
🧪 Example Usage
Paste this into the app:

```
https://www.reddit.com/user/Hungry-Move-6603/
Choose a model like gpt2 or falcon-7b-instruct, click Generate, and see the user's persona come to life!
```
📁 Output Sample
personas/Hungry-Move-6603.txt

```
👤 Name: Raj Malhotra
📍 Location: Possibly India (r/lucknow, r/IndiaUnfiltered)

🧠 Personality Traits:
- Analytical and detail-oriented
- Politically curious

💬 Quote:
“Malls are a thing of the past in LKO — rents are rising but demand is dead.”

🔥 Interests:
- Local politics
- Public behavior
- Society trends

📌 Subreddits:
- r/lucknow
- r/nagpur
- r/IndiaUnfiltered
```
🌐 Deployment on Hugging Face Spaces
Want to host it online? Use these steps:
```
Go to: https://huggingface.co/spaces

Create a new Space → Select Gradio + Python

Upload all project files

In Settings > Secrets, add:

REDDIT_CLIENT_ID

REDDIT_CLIENT_SECRET

✅ Done!
```

❤️ Contributing
Pull requests and ideas are welcome!
If you'd like to enhance the UI, try new models, or add PDF export — feel free to contribute.
