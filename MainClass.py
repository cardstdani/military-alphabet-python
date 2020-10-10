wordsList = ["Alfa", "Bravo", "Charli", "Delta", "Eco", "Foxtrot", "Golf", "Hotel", "India", "Julia", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-Ray", "Yankee", "Zulu"]

inputString = input()
outputString = ""

for c in inputString:
    if c.isspace():
        outputString += " "
    else:
        outputString += wordsList[ord(c.lower())-97]+" "

print("\n" + outputString)
