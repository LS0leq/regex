import re

with open("hasze.txt", "r", encoding="utf-8") as file:
    content = file.read()

regex = "\#[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]+"

words = re.findall(regex, content)
print("Wczytane hasztagi:")
for word in words:
    print(word)