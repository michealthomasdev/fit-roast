import random
import gradio as gr
import requests

# Dictionary of roasts mapped to score ranges
roasts = {
    "high": [
        "Stepping out in true style. Absolute perfection!",
        "Okay, we see you! The fit is immaculate.",
        "10/10. Leave some drip for the rest of us."
    ],
    "mid": [
        "Not bad, but those shoes are whispering bad choices.",
        "It's giving 'I threw this on while running out the door' energy.",
        "Safe choice. A bit boring, but you won't get arrested for it."
    ],
    "low": [
        "Yikes. Who let you out of the house like this?",
        "This fit is a certified hazard. Absolute disaster.",
        "Negative drip. Pure chaos."
    ]
}

def roast_fit(waist_up_img, waist_down_img):
    voice = random.choice(["am_michael", "am_adam", "af_bella", "af_heart"])
    print(f"Selected Kokoro voice: {voice}")

    if waist_up_img is None or waist_down_img is None:
        return "⚠️ Please upload **both** your waist-up and waist-down selfies to get roasted!", None
    
    # Generate random score
    score = random.randint(1, 10)
    
    # Select critique category based on score
    if score >= 8:
        category = "high"
    elif score >= 5:
        category = "mid"
    else:
        category = "low"
        
    critique = random.choice(roasts[category])
    roast_text = f"🔥 **Fit Rating: {score} / 10**\n\n**Critique:** {critique}"

    response = requests.post(
        "http://localhost:8880/v1/audio/speech",
        json={
            "model": "kokoro",
            "input": roast_text,
            "voice": voice,
            "response_format": "mp3",
        },
        timeout=120,
    )
    response.raise_for_status()
    audio_path = "roast_audio.mp3"
    with open(audio_path, "wb") as audio_file:
        audio_file.write(response.content)

    return roast_text, audio_path

# Build the Gradio Web Interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🔥 Selfie Fit Roaster 🔥")
    gr.Markdown("Upload your two-part selfie (waist-up and waist-down) to get your official fit score and roast.")
    
    with gr.Row():
        waist_up_input = gr.Image(type="numpy", label="Upload Waist-Up Selfie")
        waist_down_input = gr.Image(type="numpy", label="Upload Waist-Down Selfie")
        
    roast_button = gr.Button("Roast My Fit! 🔥", variant="primary")
    output_box = gr.Markdown(label="The Verdict")
    audio_output = gr.Audio(value="roast_audio.mp3", label="Roast Audio")
    
    roast_button.click(
        fn=roast_fit,
        inputs=[waist_up_input, waist_down_input],
        outputs=[output_box, audio_output]
    )

if __name__ == "__main__":
    demo.launch()
    