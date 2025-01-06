def read_book(file_path):
    with open(file_path) as file:
        return file.read()
    
def get_number_of_words(text):
    return len(text.split())

def get_character_dictionary(text):
    words = text.split()
    chars = {}
    for word in words:
        for char in word.lower():
            if char.isalpha():
                if char in chars:
                    chars[char] += 1
                else:
                    chars[char] = 1
    return chars

def convert_char_dict_to_sorted_list_by_occurrence(chars):
    sorted = []
    for char in chars.keys():
        sorted.append((char, chars[char]))
    sorted.sort(reverse=True, key=lambda x: x[1])
    return sorted

def main():
    text = read_book("books/frankenstein.txt")
    num_words = get_number_of_words(text)
    chars = get_character_dictionary(text)
    sorted_chars = convert_char_dict_to_sorted_list_by_occurrence(chars)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("\n\n")
    for char, occurrences in sorted_chars:
        print(f"The '{char}' was found {occurrences} times")

    print("--- End report ---")

main()