
## Project Overview

This project is a bioinformatics analysis of the **SURF1** gene, which is involved in the assembly of cytochrome c oxidase in mitochondria. Using Biopython, we retrieve SURF1 gene sequences from the NCBI database for various species, perform a multiple sequence alignment (MSA), and use BLAST to identify homologous sequences.

The steps covered in this analysis include:
1. **Data Collection**: Download SURF1 gene sequences from the NCBI database.
2. **Sequence Parsing**: Parse and inspect the downloaded sequences.
3. **Multiple Sequence Alignment (MSA)**: Align the sequences using MAFFT.
4. **BLAST Analysis**: Use BLAST to find homologous sequences for each SURF1 sequence.
5. **Result Interpretation**: Interpret the BLAST results and summarize findings.

## Prerequisites

To replicate this analysis, ensure the following prerequisites are met:

- **Python 3.7+**
- **Biopython** library for handling biological data
- **MAFFT** for multiple sequence alignment (MSA)
- **NCBI API key** (optional but recommended for BLAST requests)
- **Internet connection** for accessing the NCBI database

### Libraries Required

Install the following Python libraries if they aren’t already installed:

```bash
pip install biopython

---
title: "SURF1 Gene Analysis Project"
output: html_document
---

### Files Included

The following files are included in the project:

- `SURF1_sequences.fasta`: FASTA file with SURF1 sequences retrieved from NCBI.
- `SURF1_alignment.aln`: Multiple sequence alignment file generated by MAFFT.
- BLAST XML Files: Individual BLAST results for each sequence (e.g., `NG_008477.2_blast.xml`).
- `parsed_blast_results.csv`: A CSV file summarizing the parsed BLAST results.

## Methodology

### Data Collection

The SURF1 gene sequences were downloaded using the NCBI Entrez API. These sequences were retrieved for multiple species (e.g., Homo sapiens, Bos taurus, Canis lupus) and saved in the `SURF1_sequences.fasta` file.

### Sequence Parsing

The downloaded FASTA file was parsed to extract sequence metadata (ID, description, length) for alignment and BLAST analysis.

### Multiple Sequence Alignment (MSA)

We performed an MSA on the parsed SURF1 sequences using MAFFT, an external alignment tool. The alignment results were saved in `SURF1_alignment.aln` and used to understand the conserved regions in the SURF1 gene across species.


### BLAST Analysis

Each SURF1 sequence was submitted to NCBI's BLAST service to identify homologous sequences. The top hits were saved in separate XML files (e.g., `NG_008477.2_blast.xml`), and relevant data (e.g., hit IDs, descriptions, E-values, and scores) were parsed and saved in `parsed_blast_results.csv`.

#### BLAST Parameters Used

- Program: blastn (nucleotide BLAST)
- Database: nt (nucleotide database)
- Max Hits: Top 5 hits were retrieved for each query sequence.
- E-value Threshold: Filtered results for high-confidence matches with E-values below 1e-10.

### Results Summary

The results of the BLAST analysis showed that:

- **Exact Matches**: For the query sequence NG_008477.2 (SURF1 in Homo sapiens), the top BLAST hit was an exact match (E-value of 0.0), which confirmed its identity as the SURF1 gene.
- **High Similarity Matches**: Additional hits with very low E-values (e.g., 2.19e-13) suggested closely related sequences or highly similar fragments of the SURF1 gene in Homo sapiens.
- **Cross-Species Analysis**: The multiple sequence alignment showed conserved regions of the SURF1 gene, supporting its essential role in cytochrome c oxidase assembly.

## Conclusion

This project successfully demonstrates how to use Biopython for retrieving, aligning, and analyzing gene sequences. The analysis confirms the identity and conservation of the SURF1 gene across species. This workflow can be adapted for other genes or extended with additional analyses, such as phylogenetics or motif discovery.
