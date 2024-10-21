import streamlit as st
from PyPDF2 import PdfReader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
import os

# Configure the Gemini API
api_key = "YOUR_GOOGLE_API_KEY_HERE"  # Replace with your actual API key
genai.configure(api_key=api_key)

# Function to read text from uploaded PDFs
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Function to split the text into manageable chunks
def get_text_chunks(text, chunk_size=3000, overlap=500):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

# Function to create a vector store from the text chunks using Gemini embeddings
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

# Load a conversational chain for question answering
def get_conversational_chain():
    prompt_template = """
    Use the provided context to answer the question. Focus on bioinformatics aspects like gene functions, disease associations, or pathway involvements. If the answer is not in the context, say "The answer is not available in the context."
    \n\nContext:\n{context}\n
    Question:\n{question}\n
    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

# Function to process the user's question and get a response using the Gemini API
def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    return response.get("output_text", "No output text available")

# Streamlit main function
def main():
    st.set_page_config("Chat with Bioinformatics Research Papers")
    st.header("BioResearchChat: Chat with Bioinformatics Research Papers")

    # Sidebar for uploading PDF files
    with st.sidebar:
        st.title("Upload Research Papers")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on Submit & Process", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)  # Create and save the vector store
                st.success("Processing Complete! You can now ask questions.")

    # Main area for user input and responses
    user_question = st.text_input("Ask a Question from the Research Papers")
    if user_question:
        response = user_input(user_question)  # Get the answer using Gemini
        st.write("Reply:", response)

if __name__ == "__main__":
    main()
