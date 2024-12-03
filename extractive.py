# Import the required libraries
import spacy
import pytextrank

# Load SpaCy's large model and add the TextRank pipe
nlp = spacy.load("en_core_web_lg")
nlp.add_pipe("textrank")

# Path to the text file
file_path = r"C:\Users\krish\OneDrive\Desktop\Projects\Text Summarization\text.txt"

# Read text from the file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Measure and print the original document length in characters
original_doc_size = len(text)
print(f"Original Document Size (in characters): {original_doc_size}")

# Process the text using SpaCy and TextRank
doc = nlp(text)

# Generate summary
summary = ""
for sent in doc._.textrank.summary(limit_sentences=1):
    summary = str(sent)  # Ensure the summary is properly converted to a string

# Measure and print the summary length in characters
summary_length = len(summary)

# Print the formatted output
print("\nSummary:")
print(summary)
print(f"Summary Length (in characters): {summary_length}")