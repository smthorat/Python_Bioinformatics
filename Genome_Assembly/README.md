# Genome_Assembly

# Genome Assembly Using De Bruijn Graphs

# Objective
The objective of this project is to simulate the process of genome assembly from short reads using a De Bruijn graph and Eulerian path algorithm. This project demonstrates a fundamental problem in bioinformatics—reconstructing a genome sequence from short, overlapping DNA reads, which is essential for analyzing sequencing data in genomics.

# Project Overview
Genome assembly is a key task in bioinformatics where we aim to reconstruct the original DNA sequence from short reads produced by sequencing machines. This project generates random DNA sequences, simulates sequencing reads from those sequences, constructs k-mers, and builds a De Bruijn graph. It then finds an Eulerian path in the graph, allowing the reconstruction of the original sequence.

This project covers:
- Simulating a random DNA sequence.
- Generating short sequencing reads.
- Creating overlapping k-mers from the reads.
- Constructing a De Bruijn graph from k-mers.
- Finding an Eulerian path to reconstruct the genome.

# Features
- Generates a random DNA sequence of any specified length.
- Simulates sequencing reads of given length and quantity.
- Assembles the genome using k-mers and a De Bruijn graph.
- Finds an Eulerian path to reconstruct the original DNA sequence.
- Provides detailed graph information including nodes, edges, in-degrees, and out-degrees.
- Compares the original DNA sequence with the reconstructed sequence to verify the assembly success.

# Installation and Setup
# Prerequisites
- Python 3 installed on your system.
- Required libraries: netwrokx, random, collections

To install the necessary Python libraries, run:
bash
pip install networkx

# Detail Explaination 
Visit my website: https://aiinbioinformatics.com/understanding-genome-assembly-using-de-bruijn-graphs-from-concepts-to-code/

This is just a random visualization. 
You can also do a K-mers visualization

<img width="817" alt="Screenshot 2024-09-22 at 6 00 09 PM" src="https://github.com/user-attachments/assets/fb559f33-cb0c-43fa-bb65-016084059359">

  
