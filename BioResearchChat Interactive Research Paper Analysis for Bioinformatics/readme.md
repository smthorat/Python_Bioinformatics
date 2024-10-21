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
