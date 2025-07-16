import gradio as gr
import os
from reddit_scraper import init_reddit, extract_username_from_url, fetch_user_content
from persona_generator import build_prompt, generate_persona

reddit = init_reddit()

def generate_user_persona(profile_url, model_name):
    try:
        username = extract_username_from_url(profile_url)
        posts, comments = fetch_user_content(username, reddit)
        prompt = build_prompt(posts, comments)
        persona_text = generate_persona(prompt, model_name)

          # 💾 Save the persona as .txt
        save_persona_to_file(username, persona_text)

        # Quote from comment
        user_quote = ""
        for comment in comments:
            sentences = comment['body'].split('.')
            for sentence in sentences:
                if 20 < len(sentence.strip()) < 150:
                    user_quote = sentence.strip() + '.'
                    break
            if user_quote:
                break

        avatar_url = f"https://robohash.org/{username}?size=200x200"

        return avatar_url, username, persona_text, user_quote

    except Exception as e:
        return None, "", f"❌ Error: {str(e)}", ""

with gr.Blocks() as demo:
    gr.Markdown("# Reddit Persona Generator (Hugging Face)")
    with gr.Row():
        profile_url = gr.Textbox(label="Reddit Profile URL", placeholder="https://www.reddit.com/user/example/")
        model_name = gr.Dropdown(choices=["gpt2", "openchat/openchat-3.5-1210"], value="openchat/openchat-3.5-1210", label="Model")
        submit = gr.Button("Generate Persona")

    with gr.Row():
        avatar = gr.Image(label="Avatar", scale=1)
        with gr.Column(scale=3):
            username_display = gr.Markdown()
            persona_display = gr.Markdown()
            quote_display = gr.Markdown()

    submit.click(fn=generate_user_persona,
                 inputs=[profile_url, model_name],
                 outputs=[avatar, username_display, persona_display, quote_display])

def save_persona_to_file(username, persona_text):
    os.makedirs("personas", exist_ok=True)
    filepath = os.path.join("personas", f"{username}.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(persona_text)

if __name__ == "__main__":
    demo.launch(share=True)
