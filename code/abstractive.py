# Import the required libraries
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

# Define model name
model_name = "google/pegasus-xsum"

# Load pretrained model and tokenizer
pegasus_tokenizer = PegasusTokenizer.from_pretrained(model_name)
pegasus_model = PegasusForConditionalGeneration.from_pretrained(model_name)

# Path to the text file
file_path = r"C:\Users\krish\OneDrive\Desktop\Projects\Text Summarization\text.txt"

# Read text from the file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Measure and print the original document length in characters
original_doc_size = len(text)
print(f"Original Document Size (in characters): {original_doc_size}")

# Tokenize the text
tokens = pegasus_tokenizer(text, truncation=True, padding="longest", return_tensors="pt")

# Generate the summary
encoded_summary = pegasus_model.generate(
    **tokens,
    num_beams=5, 
    max_length=150,  
    min_length=30, 
    length_penalty=2.0,  
    early_stopping=True  
)

# Decode the summarized text
decoded_summary = pegasus_tokenizer.decode(encoded_summary[0], skip_special_tokens=True)

# Measure and print the summary length in characters
summary_length = len(decoded_summary)

# Print the formatted output
print("\nSummary:")
print(decoded_summary)
print(f"\nSummary Length (in characters): {summary_length}")