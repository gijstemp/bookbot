def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = word_counter(text)

    
    char_count = get_char_count(text)
    print_report(book_path, text, num_words, char_count)

def word_counter(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()
    
def get_char_count(text):
    lower_text = text.lower()
    char_dict= {}
    for i in "abcdefghijklmnopqrstuvwxyz":
        counter = 0
        for j in lower_text:
            if i == j:
                counter += 1
        char_dict[i] = counter
    return char_dict

def print_report(path, text, num_words, char_count):
    print(f"--- Begin report of {path} ---\n{num_words} words found in the document\n")
    for i in char_count:
        print(f"The '{i}' character was found {char_count[i]} times")
    print("--- End report ---")

main()