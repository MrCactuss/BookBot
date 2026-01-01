def count_words(book_text):
    number_of_words = 0
    split_text_list = book_text.split()
    for text in split_text_list:
        number_of_words += 1

    return number_of_words

def count_characters(book_text):
    character_dict = dict()
    number_of_characters = 0
    for character in book_text:
        character = character.lower()
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1

    return character_dict

