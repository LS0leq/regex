import re

with open("numery_telefonow.txt", "r", encoding="utf-8") as file:
    content = file.read()

regex = "\+\d+\s+\d+\-\d+\-\d+"

words = re.findall(regex, content)
print("Wczytane numery do telefomu:")
for word in words:
    print(word)