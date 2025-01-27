import sys
import PartA

#The runtime complexity is O(n1 + n2) where n1 and n2 are the sizes for tokens1 and 2
#This is because converting a list of size n to a set takes O(n) time complexity
def countCommonTokens(tokens1, tokens2):
    #Convert to sets so it's easier to find intersection
    set1 = set(tokens1)
    set2 = set(tokens2)
    #find intersection time complexity is O(min(n1,n2))
    return len(set1 & set2)

def main():
    # Get the file paths from the command-line arguments
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    # Use tokenize to get tokens of both files
    file1_tokens = PartA.tokenize(file1)
    file2_tokens = PartA.tokenize(file2)

    # Find shared tokens using countCommonTokens then print the number
    shared_tokens = countCommonTokens(file1_tokens, file2_tokens)
    print(shared_tokens)

if __name__ == "__main__":
    main()