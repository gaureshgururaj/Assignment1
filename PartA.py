# O(n) time complexity where n is num of words in the text since each word is only processed once
def tokenize(text_file_path):
    tokens = []
    # Try opening file
    try:
        # Open file
        file = open(text_file_path, 'r')
        for line in file:
            # Split each line into words by the spaces
            words = line.split()
            for word in words:
                # Check if it is an actual alphanumeric token if it is add it to the list
                if word.isalnum():
                    tokens.append(word.lower())
        file.close()
    # If you can't find the file print error
    except FileNotFoundError:
        print(f"=The file was not found.")
        return tokens
    return tokens

# For loop iterates over all tokens once so time complexity is O(n)
def computeWordFrequencies(tokens):
    counts = {}
    # For each token if it is in the dictionary add 1 to the count if not add it to the dictionary with count 1
    for token in tokens:
        if token in counts:
            counts[token] += 1
        else:
            counts[token] = 1
    return counts

#Overall O(nlogn) since sort function is O(nlogn) and it dominates the other steps
def print_counts(counts):
    # Convert the counts dictionary into a list of tuples O(n) time complexity since each token is converted once
    items = list(counts.items())

    # item[1] is the count for the token and item[0] is the word itself
    # This is a helper function that sorts count in a decreasing order and the word alphabetically in increasing order
    def sort_alphabet_and_count(item):
        return -item[1], item[0]

    # Sort the list
    # Built in sorting algorithm has O(nlogn)
    items.sort(key=sort_alphabet_and_count)

    # Print the contents of the sorted list
    # O(n) since you visit each token once to print it
    for token, count in items:
        print(f"{token} -> {count}")