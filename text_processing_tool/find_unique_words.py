# text_processing_tool/find_unique_words.py

def find_unique_words(text):
    """Returns a set of unique words in the text."""
    words = text.split()
    unique_words = set(words)
    return unique_words
