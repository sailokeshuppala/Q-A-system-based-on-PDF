import streamlit as st
import PyPDF2
import google.generativeai as genai

def fetch_data(pdf):
    with open(pdf, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def main():
    pdf = "paper.pdf"
    model = "gemini-1.5-pro-latest"
    with open(".gemini_api.txt", "r") as file:
        key = file.read()
    genai.configure(api_key=key)
    st.title("""Q/A system based on PDF[leave no context behind--A research paper]""")
    question = st.text_input("Enter your query... ")

    if st.button("Generate"):
            text = fetch_data(pdf)
            context = text + "\n\n" + question
            ai = genai.GenerativeModel(model_name=model)
            response = ai.generate_content(context)  
            st.write(response.text)

if __name__ == "__main__":
    main()