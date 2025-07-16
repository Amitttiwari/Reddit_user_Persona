
# Reddit Persona Generator (Hugging Face Version)

This project generates user personas based on Reddit profiles using open-source language models (via Hugging Face Transformers).

## 🚀 Features
- Input a Reddit profile URL
- Scrape public posts and comments
- Build a sociolinguistic persona using `gpt2` or other LLMs
- Deployable on Hugging Face Spaces with no external API costs

## 📦 Setup Instructions

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Set Environment Variables**:
Create a `.env` or set in terminal:

- `REDDIT_CLIENT_ID`
- `REDDIT_CLIENT_SECRET`

3. **Run Locally**:
```bash
python app.py
```

## 💡 Example Input
```
https://www.reddit.com/user/kojied/
```

## ✨ Output
A detailed persona including:
- Interests
- Personality traits
- Writing tone
- Subreddit habits
- Lifestyle clues
- A quote from their activity

## 🔧 Notes
- Uses GPT-2 (`transformers` pipeline)
- You can switch models (e.g., mistral, falcon) in `persona_generator.py`
- Works entirely offline

---
MIT License
