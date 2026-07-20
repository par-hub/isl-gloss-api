import os
import gradio as gr
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

MODEL_PATH = "Parth136/isl-text2gloss-mt5"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH, low_cpu_mem_usage=True)

def generate_gloss(sentence, max_length=64):
    inputs = tokenizer("translate to ISL gloss: " + sentence, return_tensors="pt")
    output_ids = model.generate(**inputs, max_length=max_length, num_beams=4)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

demo = gr.Interface(
    fn=generate_gloss,
    inputs=gr.Textbox(label="English/Hindi sentence"),
    outputs=gr.Textbox(label="ISL Gloss"),
    title="ISL Text-to-Gloss",
    description="Translates a sentence into ISL sign order and grammar markers."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
