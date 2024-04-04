def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        letters = letter_count(file_contents)
        list_of_pairs = sorted_dict(letters)
        for pair in list_of_pairs:
            print(f"The '{pair[0]}' character was found {pair[1]} times")
        print("--- End report ---")

def word_count(text):
    word_list = text.split()
    return len(word_list)

def letter_count(text):
    lower_text = text.lower()
    letter_dict = {}
    for letter in lower_text:
        if letter.isalpha():
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
    return letter_dict

def sorted_dict(unsorted_dict):
    dict_items = unsorted_dict.items()
    list_of_pairs = []
    for item in dict_items:
        list_of_pairs.append(item)
    sorted_list_of_pairs = sorted(list_of_pairs, key = lambda item: item[1], reverse=True)
    return sorted_list_of_pairs




main()
