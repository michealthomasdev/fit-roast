# Selfie Fit Roaster

A small Gradio app that accepts waist-up and waist-down photos, assigns a
random fit rating, and generates a spoken roast through a local Kokoro-compatible
text-to-speech server.

## Requirements

- Python 3.10 or newer
- A Kokoro-compatible OpenAI-style speech API listening at
  `http://localhost:8880/v1/audio/speech`

## Setup

Create and activate a virtual environment, then install the dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Start the speech server, then run the app:

```powershell
python app.py
```

Gradio will print the local URL to open in a browser. The uploaded images are
currently accepted by the interface but are not analyzed; ratings and critiques
are selected at random.

## Output

The generated speech is written to `roast_audio.mp3` in the current working
directory. The generated audio file is not tracked in this repository.
