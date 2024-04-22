import nltk
from nltk.corpus import stopwords
from pathlib import Path
from collections import Counter

# Download NLTK stop words data
nltk.download('stopwords')

# Load the English stop words
stop_words = set(stopwords.words('english'))

# Function to filter out stop words from a given text
def filter_stop_words(text):
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

# Function to count repeated words in a list of strings
def count_repeated_words(text_list):
    # Combine all paragraphs into a single string
    text = ' '.join(text_list)
    
    # Split the text into words
    words = text.split()
    
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    # Return a dictionary of words repeated more than 10 times
    return {word: count for word, count in word_counts.items() if count > 10}

# Function to write text to a file
def write_text_to_file(text, output_file_path):
    with open(output_file_path, "w") as file:
        file.write(text)

# Function to write word counts to a file
def write_word_counts_to_file(word_counts, output_file_path):
    with open(output_file_path, "w") as file:
        for word, count in word_counts.items():
            file.write(f"'{word}': {count}\n")

# Get the current directory
current_directory = Path(__file__).resolve().parent

# Read the contents of "random_paragraphs.txt"
input_file_path = current_directory / "random_paragraphs.txt"
with open(input_file_path, "r") as file:
    paragraphs = file.readlines()

# Filter out stop words from each paragraph
filtered_paragraphs = [filter_stop_words(paragraph) for paragraph in paragraphs]

# Write the filtered paragraphs to a new file in the same directory
filtered_text_output_file_path = current_directory / "Filtered Text.txt"
write_text_to_file("\n".join(filtered_paragraphs), filtered_text_output_file_path)

print("Stop words filtered successfully. Filtered text saved in 'Filtered Text.txt'.")

# Read the filtered paragraphs from the file
with open(filtered_text_output_file_path, "r") as file:
    filtered_paragraphs = file.readlines()

# Count repeated words
repeated_words = count_repeated_words(filtered_paragraphs)

# Specify the output file path for repeated words
repeated_words_output_file_path = current_directory / "Repeated Words.txt"

# Write repeated words and their counts to a file
write_word_counts_to_file(repeated_words, repeated_words_output_file_path)

print(f"Repeated words and their counts saved to '{repeated_words_output_file_path}'.")

# Print only the repeated words without the filtered words
for word, count in repeated_words.items():
    print(f"'{word}': {count}")
