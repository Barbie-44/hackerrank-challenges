from collections import Counter


def company_logo(s):

    frequency = Counter(s)
    top_three = frequency.most_common(3)
    for item in top_three:
        print(item[0], item[1])


if __name__ == "__main__":
    s = input()
    company_logo(s)
