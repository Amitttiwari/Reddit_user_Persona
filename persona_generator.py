from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch
from functools import lru_cache

@lru_cache(maxsize=2)
def load_generator(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)
    return generator

def build_prompt(posts, comments):
    sample_texts = ""
    for i, post in enumerate(posts[:3]):
        sample_texts += f"[POST {i+1} from r/{post['subreddit']}]: {post['title']} - {post['selftext']}\n"
    for i, comment in enumerate(comments[:3]):
        sample_texts += f"[COMMENT {i+1} from r/{comment['subreddit']}]: {comment['body']}\n"

    prompt = f"""
You are a persona analyst. Based on the user's Reddit posts and comments below, create a structured and summarized user persona.

Output the following sections:

👤 **Name**: (Estimate a fictional name if not available)
📍 **Location**: (If detectable, else "Unknown")
🎯 **Archetype**: (E.g., The Thinker, The Rebel, The Organizer)
🧠 **Personality Traits**:
- Trait 1: ...
- Trait 2: ...
(Include a brief quote/comment as evidence)

📝 **Writing Style**: Describe their tone and way of speaking

🔥 **Interests**:
- Topic 1: ...
- Topic 2: ...
(Cite Reddit subreddits or sample phrases)

📌 **Frequent Subreddits**:
- r/example1
- r/example2

💬 **User Quote**:
"Pull one powerful or emotional quote from their comment."

Reddit Data:
{sample_texts}
"""


    return prompt.strip()

def generate_persona(prompt, model_name="openchat/openchat-3.5-1210"):
    generator = load_generator(model_name)
    outputs = generator(prompt, max_new_tokens=500, do_sample=True, temperature=0.7)
    raw_output = outputs[0]['generated_text']

     # 🔥 Remove prompt echo from the generated output
    if "Reddit Data:" in raw_output:
        persona_only = raw_output.split("Reddit Data:")[0].strip()
    else:
        persona_only = raw_output.strip()

    return persona_only
