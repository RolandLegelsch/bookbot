def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{countWords(file_contents)} words found in the document")
        print()
        chars = countCharacters(file_contents)
        for char in chars:
            print(f"The '{char["char"]} character was found {char[char["char"]]} times")

        print("--- End report ---")

def countWords(text):
    return len(text.split())

def sort_on(dict):
    return dict[dict["char"]]

def countCharacters(text):
    charDict = {}
    listOfDict = []
    for t in text:
        if t.isalpha():
            c = t.lower()
            if (c not in charDict):
                charDict[c] = 1
            else:
                charDict[c] += 1
    for k in charDict:
        listOfDict.append({k: charDict[k], "char": k})
    
    listOfDict.sort(reverse=True, key=sort_on)
    return listOfDict

main()