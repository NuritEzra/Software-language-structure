gematria = {
    'א': 1,
    'ב': 2,
    'ג': 3,
    'ד': 4,
    'ה': 5,
    'ו': 6,
    'ז': 7,
    'ח': 8,
    'ט': 9,
    'י': 10,
    'כ': 20,
    'ל': 30,
    'מ': 40,
    'נ': 50,
    'ס': 60,
    'ע': 70,
    'פ': 80,
    'צ': 90,
    'ק': 100,
    'ר': 200,
    'ש': 300,
    'ת': 400,
    # final words
    'ך': 20,
    'ם': 40,
    'ן': 50,
    'ף': 80,
    'ץ': 90
}

def wordGematria(word):
    sum = 0
    for i in range(len(word)):
        if word[i] in gematria:
            sum += gematria[word[i]]
        else:
            return -1
    return sum


def main():
    print("enter word:")
    try:
        word = str(input())
    except ValueError:
        print("invalid input")
        return
    sum=wordGematria(word)
    if sum==-1:
        print("invalid input")
    else:
        print(sum)
if __name__ == "__main__":
    main()
