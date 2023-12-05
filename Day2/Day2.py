def calcLineColor(line : str, maxColors : dict[str:int]) -> int :
    dictColor = {"red" : [], "green" : [], "blue" : []}
    t = [elem.strip(":;,") for elem in line.split()]
    for i in range(3, len(t), 2) :
        dictColor[t[i]].append(int(t[i-1]))

    isUnderMax = True
    for (key, _max) in zip(dictColor, maxColors) :
        isUnderMax &= max(dictColor[key]) <= maxColors[key]
        #print(key, dictColor[key], maxColors[key])
    return int(t[1]) if isUnderMax else 0

def calcLineColorPowerCube(line : str) -> int :
    dictColor = {"red" : [], "green" : [], "blue" : []}
    t = [elem.strip(":;,") for elem in line.split()]
    for i in range(3, len(t), 2) :
        dictColor[t[i]].append(int(t[i-1]))

    maxColors = {"red":0, "green":0, "blue":0}
    for (key, _max) in zip(dictColor, maxColors) :
        maxColors[key] = max(dictColor[key])

    maxArray = [maxColors[value] for value in maxColors.keys()]
    return maxArray[0] * maxArray[1] * maxArray[2]


textInput = open("inputDay2", "r").readlines()
sum = 0
for line in textInput :
    sum += calcLineColorPowerCube(line)
print(sum)