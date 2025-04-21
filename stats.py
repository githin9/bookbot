def count_words(text):
    words = text.split()
    word_count = len(words)

    return word_count

def count_chars(text):
    char_dict = {}
    text = text.lower()

    for char in text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    
    return char_dict

def sort_dict(char_dict):
    sorted_dict = dict(sorted(char_dict.items(), 
                              key = lambda item: item[1], 
                              reverse=True))
    return sorted_dict