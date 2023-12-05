def calcLineNoLetters(line : str) -> int :
    sum = 0
    for elem in line :
        if elem.isdigit() :
            sum += int(elem)
            break
    for elem in line[::-1] :
        if elem.isdigit() :
            return sum * 10 + int(elem)

def calcLineLetters(line : str) -> int :
    dictNumbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    sum = 0
    numberFound = False
    for i in range(len(line)) :
        if line[i].isdigit():
            sum += int(line[i]) * 10
            break
        for j in range(0, i) :
            if line [j:i+1] in dictNumbers :
                sum += dictNumbers[line[j:i+1]] * 10
                numberFound = True
                break
        if numberFound :
            break

    for i in range(len(line)-1, -1, -1) :
        if line[i].isdigit():
            return sum + int(line[i])
        for j in range(i, -1, -1) :
            if line [j:i + 1] in dictNumbers :
                return sum + dictNumbers[line[j:i + 1]]

f = open("inputDay1", "r")

lines = f.readlines()
sum = 0
for line in lines :
    sum += calcLineNoLetters(line)
print(sum)

sum = 0
for line in lines :
    sum += calcLineLetters(line)
print(sum)
