# text_processing_tool/count_words.py

def count_words(text):
    """Returns the number of words in a given text."""
    words = text.split()
    return len(words)
