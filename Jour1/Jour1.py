def calculLigne(ligne) -> int :
    somme = 0
    for elem in ligne :
        if elem.isdigit() :
            somme += int(elem)
            break
    for elem in ligne[::-1] :
        if elem.isdigit() :
            print(somme * 10 + int(elem))
            return somme * 10 + int(elem)

f = open("inputDay1", "r")
lines = f.readlines()

somme = 0
for line in lines :
    somme += calculLigne(line)

print(somme)


somme = 0
l = ["1abc2",
"pqr3stu8vwx",
"a1b2c3d4e5f",
"treb7uchet"]

for line in l :
    somme += calculLigne(line)
print(somme)
