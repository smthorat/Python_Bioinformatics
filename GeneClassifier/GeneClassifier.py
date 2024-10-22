# Import necessary libraries
import gffutils
from Bio import SeqIO
from intervaltree import IntervalTree
from itertools import islice
import os

# Function to extract gene coordinates from a GTF file and store them in an IntervalTree
def extract_gene_coordinates(gtf_file):
    gene_tree = IntervalTree()
    db = gffutils.create_db(gtf_file, dbfn=':memory:', force=True, keep_order=True)
    
    for feature in db.features_of_type(['gene', 'transcript', 'exon', 'CDS']):
        gene_tree[feature.start:feature.end] = feature.id  # Store gene regions as intervals
    
    return gene_tree

# Function to extract the entire sequence from a FASTA file in a memory-efficient way (streaming)
def extract_sequence_from_fasta(fasta_file):
    fasta_sequences = SeqIO.parse(fasta_file, "fasta")
    for record in fasta_sequences:
        yield str(record.seq)  # Yield the sequence chunk by chunk

# Tokenize a sequence into chunks of specified size in batches for efficiency
def tokenize_sequence_in_batches(sequence, chunk_size=5, batch_size=10000):
    # Process the sequence in batches
    iterator = (sequence[i:i + chunk_size] for i in range(0, len(sequence), chunk_size))
    while True:
        batch = list(islice(iterator, batch_size))
        if not batch:
            break
        yield batch

# Function to classify tokens based on gene intervals
def classify_tokens(tokens, gene_tree, offset=0):
    classified_tokens = []
    for idx, token in enumerate(tokens):
        token_start = offset + idx * len(token) + 1
        token_end = token_start + len(token) - 1

        # Check if the token overlaps with any gene region
        in_gene_region = gene_tree.overlaps(token_start, token_end)

        classification = "gene" if in_gene_region else "non-gene"
        classified_tokens.append((token, classification))
    
    return classified_tokens

# Main function to extract gene coordinates, tokenize the sequence, and classify tokens
def extract_tokenize_and_classify(gtf_file, fasta_file, output_file, chunk_size=5, batch_size=10000):
    # Step 1: Extract gene coordinates from the GTF file
    gene_tree = extract_gene_coordinates(gtf_file)

    # Step 2: Stream the sequence from the FASTA file
    with open(output_file, 'w') as f:
        f.write("Classified Tokens (Token, Classification):\n")

        sequence_generator = extract_sequence_from_fasta(fasta_file)
        offset = 0

        for sequence in sequence_generator:
            for token_batch in tokenize_sequence_in_batches(sequence, chunk_size, batch_size):
                # Step 3: Classify each batch of tokens
                classified_tokens = classify_tokens(token_batch, gene_tree, offset)
                offset += len(token_batch) * chunk_size  # Adjust offset for next batch

                # Step 4: Write the classified tokens to the output file
                for token, classification in classified_tokens:
                    f.write(f"{token}\t{classification}\n")

    print(f"Output saved to {output_file}")

# Check if the files exist before running the function
gtf_file_path = "/Users/swaraj/Downloads/genomic.gtf"
fasta_file_path = "/Users/swaraj/Downloads/GCF_000005845.2_ASM584v2_genomic.fna"
output_file = "/Users/swaraj/Downloads/classified_tokens_output.txt"

if not os.path.exists(gtf_file_path):
    print(f"GTF file not found: {gtf_file_path}")
elif not os.path.exists(fasta_file_path):
    print(f"FASTA file not found: {fasta_file_path}")
else:
    # Run the function to extract, tokenize, and classify
    extract_tokenize_and_classify(gtf_file_path, fasta_file_path, output_file)