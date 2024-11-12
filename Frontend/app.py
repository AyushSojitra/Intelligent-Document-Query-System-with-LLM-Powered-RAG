import streamlit as st
import requests

st.title("SmartDocQA system")

col1, col2 = st.columns(2)

with col1:
    urlInput = st.text_input("Input your URL")

with col2:
    pdfInput = st.file_uploader("Upload your PDF", type="pdf", accept_multiple_files=False)

but1, but2, but3 = st.columns([1.5,1,1])
with but2:
    processData = st.button("Process Data")

if processData:
    try:
        if urlInput:
            st.success("Processing your URL...:)")
            payload = {'url': urlInput}
            response = requests.post("http://127.0.0.1:5000/url-process", json=payload)
            st.success(response.json()['message'])
        elif pdfInput:
            st.success("Processing your PDF...:)")
            payload = {'pdf': (pdfInput.name, pdfInput.read(), 'application/pdf')}
            response = requests.post("http://127.0.0.1:5000/pdf-process", files=payload)
            st.success(response.json()['message'])
        else:
            st.warning("Oops! Seems like there's no URL or PDF to process :(")
    except Exception as e:
        st.error(f"Error processing the data: {e}")

query = st.text_input("Enter your query")
generateAnswer = st.button("Generate")
if generateAnswer:
    response = requests.post("http://127.0.0.1:5000/get-response", json={'query': query})
    st.write(response.json()['message'])
    # print(response)