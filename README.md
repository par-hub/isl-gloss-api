# ISL Text-to-Gloss API Demo

A small Gradio app that accepts an English/Hindi sentence and generates an Indian Sign Language (ISL) gloss using the Hugging Face model `Parth136/isl-text2gloss-mt5`.

## How it works

- Loads a Transformers tokenizer and sequence-to-sequence model from Hugging Face.
- Prefixes input with `translate to ISL gloss:`.
- Generates a sequence with beam search and displays the decoded gloss in Gradio.

## Requirements

- Python
- Packages listed in `requirements.txt`
- Network access on first run to download the model weights, unless they are already cached

## Run locally

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open the local Gradio URL printed in the terminal (default port: `7860`; the app also respects the `PORT` environment variable).

## Files

- `app.py` — model loading, gloss generation, and Gradio interface
- `requirements.txt` — Transformers, CPU PyTorch, SentencePiece, and Gradio dependencies

## Notes

Model download and inference can require substantial memory and startup time. Evaluate linguistic quality separately; generated gloss should be checked with fluent ISL users before being treated as a reliable translation. Do not expose the demo publicly without considering access controls and resource limits.
