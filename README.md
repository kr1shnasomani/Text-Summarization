# Text Summarizer

This project implements both abstractive and extractive text summarization techniques. It uses PEGASUS for abstractive summarization, generating concise summaries from long texts and TextRank for extractive summarization, selecting key sentences to create a meaningful summary.

## Execution Guide:

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


## Overview:
The repository includes two separate Python scripts for text summarization: one using **Abstractive Summarization** with a pre-trained PEGASUS model and another using **Extractive Summarization** with the **TextRank** algorithm via the SpaCy library. Here's an overview of each script and a comparison to determine which one might be best for different use cases.

1. **Abstractive Summarization (`abstractive.py`)**
   - **Libraries Used**:
     - **PEGASUS**: A pre-trained model from Google's Transformer-based models specifically designed for abstractive summarization.
     - **Transformers**: Hugging Face library to easily load pre-trained models.
   - **Process**:
     1. The script loads the pre-trained **PEGASUS-XSUM** model, which is fine-tuned for generating summaries of documents.
     2. It reads the input text from a file and measures its original length.
     3. The text is tokenized using the PEGASUS tokenizer, ensuring that the input is formatted properly for the model.
     4. The model generates a summary with controlled parameters such as beam search (`num_beams=5`), maximum and minimum summary lengths, and a length penalty to prevent excessively short or long summaries.
     5. The summary is then decoded from token IDs into human-readable text.
     6. The script outputs the summary and the length of the generated summary in characters.
   - **Advantages**:
     - **Abstractive Summarization** means the model generates a new summary in its own words, which tends to provide more coherent and fluent results.
     - It can handle complex documents and condense the content into a more meaningful summary rather than just extracting sentences.
   - **Limitations**:
     - The model is dependent on the pre-trained data it was fine-tuned on (news summarization in the case of XSUM), so it might not perform optimally on all domains.
     - It requires more computational resources due to the size and complexity of the PEGASUS model.

2. **Extractive Summarization (`extractive.py`)**
   - **Libraries Used**:
     - **SpaCy**: An NLP library for processing text and extracting information.
     - **PyTextRank**: A library that implements the TextRank algorithm for extractive summarization.
   - **Process**:
     1. The script uses **SpaCy's** large English model (`en_core_web_lg`), which is pre-trained on a large corpus of English text.
     2. The **TextRank** algorithm is added as a pipeline component to SpaCy. TextRank is a graph-based algorithm that ranks sentences based on their relevance to the overall document.
     3. The input text is read from the file, and its original length is measured.
     4. SpaCy processes the text, and TextRank identifies the most important sentences, which are then used to generate the summary.
     5. The summary is formed by extracting the top-ranked sentence(s) and is outputted along with the length of the summary.
   - **Advantages**:
     - **Extractive Summarization** is faster and simpler than abstractive summarization, as it just selects important sentences from the original text without generating new content.
     - It works well with a wide range of text types, as it does not require domain-specific fine-tuning.
     - It's less computationally intensive since it uses a simpler algorithm compared to PEGASUS.
   - **Limitations**:
     - The summary might not be as coherent or fluent as in abstractive summarization, as it directly extracts sentences from the original text.
     - The extracted sentences may not flow smoothly when put together in a summary.

### Comparison and Best Choice:
- **When to Use Abstractive Summarization (PEGASUS)**:
  - **Complex, lengthy documents** where a concise, fluent summary is needed.
  - Scenarios where coherence and readability are more important than just picking out key sentences (e.g., summarizing research papers, long articles, or creative writing).
  - If you want summaries that paraphrase the input text and focus on delivering the essential meaning in a human-readable format.

- **When to Use Extractive Summarization (TextRank with SpaCy)**:
  - **Shorter, more straightforward documents** where you just need to extract the key points or sentences.
  - Scenarios where you need to quickly get a sense of the main ideas from a document without needing a rephrased summary.
  - If computational resources are limited or if you need to process large amounts of text efficiently.

### Best Option:
- **PEGASUS (Abstractive Summarization)** is generally considered superior when you need **more coherent and fluent summaries** that convey the meaning in a concise form. It is ideal for complex and domain-specific content but requires more computational power.
- **TextRank (Extractive Summarization)** is a good choice for **faster, simpler tasks** or when working with resources where computational efficiency is important, though the summaries might not always be as polished or natural.

For tasks requiring highly fluent and creative summaries, **PEGASUS** would likely be the better choice. However, for simpler, faster extraction of key points from text, **TextRank** offers a more efficient solution.
