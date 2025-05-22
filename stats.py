
def count_words(book_text:str) -> int:
    '''Counts words in book text.'''
    return len(book_text.split())

def count_characters(book_text:str) -> int:
    '''Counts appearance of each character'''
    book_text = book_text.lower()
    character_count ={}
    for b in book_text:
        if b in character_count:
            character_count[b] +=1
        else:
            character_count[b] = 1
    return character_count

def sort_counts(character_count):
    sorted_count = []
    def sort_on(dict):
        return dict["num"]
    for character in character_count:
        count = {"char": character, "num": character_count[character]}
        sorted_count.append(count)
    sorted_count.sort(reverse=True, key=sort_on)

    return sorted_count