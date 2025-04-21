from stats import count_words, count_chars, sort_dict
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    path = sys.argv[1]

    text = get_book_text("./" + path)
    word_count = count_words(text)
    char_count = count_chars(text)
    sorted_dict = sort_dict(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for char in sorted_dict:
        if char.isalpha() == True:
            print(f"{char}: {sorted_dict[char]}")

    print("============= END ===============")

main()