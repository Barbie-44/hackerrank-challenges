from collections import Counter


def merge_the_tools(string, k):
    # your code goes here
    """
    APPROACH:
        1. Slice the string via a for loop to get n/k substrings of length=k
        2. Check if the values of each substring appear only once
        3. print each result
    """
    substr = []
    for i in range(int(len(string) / k)):
        start = int(i * k)
        substr.append(string[start : start + k])
    for item in substr:
        frequencies = Counter(item)
        new_string = ""
        for value in frequencies.keys():
            new_string += value
        print(new_string)


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
