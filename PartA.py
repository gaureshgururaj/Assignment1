def tokenize(text_file_path):
    tokens = []
    try:
        file = open(text_file_path, 'r')
        for line in file:
            words = line.split()
            for word in words:
                if word.isalnum():
                    tokens.append(word.lower())
        file.close()
    except FileNotFoundError:
        print(f"=The file was not found.")
        return tokens
    return tokens

def computeWordFrequencies(tokens):
    counts = {}
    for token in tokens:
        if token in counts:
            counts[token] += 1
        else:
            counts[token] = 1
    return counts

def print_counts(counts):
    items = list(counts.items())

    def sort_alphabet_and_count(item):
        return -item[1], item[0]

    items.sort(key=sort_alphabet_and_count)

    for token, count in items:
        print(f"{token} -> {count}")