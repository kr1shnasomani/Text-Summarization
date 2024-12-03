# Text Summarization

The project implements abstractive and extractive text summarization by processing input text files to generate concise, character-based summaries.

## How to Run the Code

1. Run the following command lines in the terminal:

   (a) Abstractive Summarization:
     ```
     pip install transformers torch sentencepiece
     ```
   (b) Extractive Summarization:
     ```
     pip install spacy pytextrank
     python -m spacy download en_core_web_lg
     ```

2. Create a `.txt` file with the content whose summary you want

3. Copy the path of the file and paste it in the code

4. Run the code. The output for the `text.txt` file in the repository looks like:

   (a) Abstractive Summarization:

   ![WhatsApp Image 2024-12-03 at 18 09 13_980b5520](https://github.com/user-attachments/assets/d6c46769-433f-4df3-bb24-2bbb55e7f1b3)

   (b) Extractive Summarization:

   ![WhatsApp Image 2024-12-03 at 18 10 32_ae95aa51](https://github.com/user-attachments/assets/bd469487-8500-4817-8783-fd5f1f127651)


## Overview
Abstractive summarization rephrases and generates new sentences, making it suitable for creative and human-like summaries. It is ideal when clarity, context, or brevity is required, such as in news highlights or executive reports. Extractive summarization selects key sentences directly from the text, ensuring factual accuracy and is best for legal, scientific, or technical documents where preserving original phrasing is crucial. Neither is universally superior; the choice depends on the use case. For tasks demanding contextual understanding, abstractive works best, while extractive is reliable for concise, factual extracts. Combining both approaches can often provide optimal results in hybrid scenarios.
