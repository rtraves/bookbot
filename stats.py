def get_num_words(text):
    words = text.split()
    number_of_words = len(words)
    return number_of_words

def get_num_characters(text):
    char_counts = {}
    for c in text:
        lower_c = c.lower()
        if lower_c in char_counts:
            char_counts[lower_c] += 1
        else:
            char_counts[lower_c] = 1
    return char_counts

def sort_on(dict):
    return dict["num"]
def sorted_list(d):
    l = [{"char": k, "num": v} for k, v in d.items()]
    l.sort(reverse=True, key=sort_on)
    return l