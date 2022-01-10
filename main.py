import csv
import clipboard

count = 0

def search(word):
    try:
        from googlesearch import search
    except ImportError:
        print("Google search failed !")
    text = "what is the meaning of " + word.lower()
    print("Results :")
    print("-"*40)
    for result in search(text, stop=5):
        print(result)
    print("-"*40)
    wait = input()



with open('list.csv', 'r') as f:
    dictionary = csv.reader(f)
    abbr = clipboard.paste().upper()
    print("-"*40)
    for word in dictionary:
        if abbr == word[0]:
            count += 1
            print("{0}) {1}".format(count, word[1]))

    if count == 0:
        print("Not found !")

    print("-"*40)
    decision = input("Options :\n\t1) Google search \n\t0) Exit\n> ")

    if decision == "1":
        search(abbr)

