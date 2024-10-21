# BioResearchChat: Interactive Research Paper Analysis for Bioinformatics

BioResearchChat is a Streamlit-based application that allows users to upload bioinformatics research papers, reviews, or genomic data reports in PDF format. The system processes the uploaded documents, creates embeddings using BioBERT, and enables users to interactively ask questions about experimental results, methodologies, or findings.

## Features

- **Upload PDFs:** Upload research papers, reviews, or genomic data reports.
- **Text Processing:** Extracts and processes text from PDF files, splitting it into manageable chunks.
- **BioBERT Embeddings:** Uses BioBERT, a pre-trained language model for biomedical literature, to create embeddings for text chunks.
- **Similarity Search:** Finds the most relevant text chunks related to the user's question using cosine similarity.
- **Question Answering:** Answers user questions based on the retrieved context using a BioBERT-based question-answering model.

## Prerequisites

- **Python 3.7+** is required.
- **Libraries:** The following Python libraries must be installed:
  - `streamlit`
  - `PyPDF2`
  - `transformers`
  - `torch`
  - `numpy`
  - `scikit-learn`
  - `pickle` (part of the standard library)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/BioResearchChat.git
   cd BioResearchChat

## Run the Application 
streamlit run bio_research_chat.py

## Upload PDFs

Go to the sidebar and upload one or more research papers in PDF format.
Click on "Submit & Process" to extract and process the text.

## Ask Questions

Enter your question in the main text input field and get an answer based on the context from the uploaded documents.

## File Structure

bio_research_chat.py: Main application script.
vector_store.pkl: Saved vector store file (generated after processing PDFs).
README.md: Project documentation.
requirements.txt: List of Python libraries needed for the project.

## Example Questions You Can Ask

"What were the main findings in the study?"
"Describe the methodology used for genome sequencing."
"Which genes were associated with the disease in this research?"

## How It Works

Text Extraction: The application reads the content of uploaded PDFs using PyPDF2.
Text Splitting: Text is divided into chunks of 3,000 characters with a 500-character overlap for better context handling.
Embedding Creation: BioBERT generates embeddings (vector representations) for each chunk.
Vector Store: The embeddings and corresponding text chunks are saved in a local vector store for later retrieval.
Question Processing: When a question is asked, the system searches for the most relevant text chunks based on cosine similarity.
Answer Generation: The selected chunks are used as context for a BioBERT-based question-answering pipeline.

## Future Enhancements

Integrate Ontologies: Link to biological ontologies (e.g., Gene Ontology) for enriched responses.
Database Integration: Incorporate external bioinformatics databases (e.g., NCBI, UniProt) for additional context.
Improved Handling of Large Documents: Implement pagination or section-based processing.

## UI

<img width="1470" alt="image" src="https://github.com/user-attachments/assets/1f1a40ba-470e-4401-b4dc-dd7e1b9c0639">

