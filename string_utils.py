def reverse_string(text):
    return text[::-1]

def count_words(text):
    return len(text.split())

def capitalize_words(text):
    return ' '.join(word.capitalize() for word in text.split())

if __name__ == "__main__":
    test_text = "tere git maailm"
    print("Original:", test_text)
    print("Reversed:", reverse_string(test_text))
    print("Word count:", count_words(test_text))
    print("Capitalized:", capitalize_words(test_text))
