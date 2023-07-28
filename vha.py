import streamlit as st
import pandas as pd
import numpy as np
import anthropic

def ask_assistant(question):
    prompt = (f"{anthropic.HUMAN_PROMPT} Anda adalah asisten jaminan kesehatan virtual untuk BPJS Kesehatan. Tolong beri jawaban dalam Bahasa Indonesia atas pertanyaan terkait BPJS Kesehatan. Gunakan data-data yang nanti akan saya sediakan sebagai sumber jawaban."
            f"{anthropic.AI_PROMPT} Baik! Saya akan berusaha memberi jawaban hanya menggunakan data yang disediakan."
            f"{anthropic.HUMAN_PROMPT} Baik! ingat untuk hanya menggunakan data yang saya dapatkan. Berikut pertanyaannya: {question}")

    c = anthropic.Anthropic(api_key=st.secrets["claude_key"])
    resp = c.completions.create(
        prompt=f"{prompt} {anthropic.AI_PROMPT}",
        stop_sequences=[anthropic.HUMAN_PROMPT],
        model="claude-v1.3-100k",
        max_tokens_to_sample=900,
    )

    print(resp.completion)
    return resp.completion

st.title('test')

with st.container():
    # st.header("Pertanyaan")
    pertanyaan = st.text_input("Silakan masukkan pertanyaan anda...")

    st.write("Klik tombol `Kirim` untuk mengirim pertanyaan")
    if st.button("Kirim"):
        result = ask_assistant(pertanyaan)
        with st.chat_message("user"):
            st.write(result)
