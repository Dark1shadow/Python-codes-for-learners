myDict = {
    "Fast ": "in guick manner",
    "Aayush": "A coder",
    "Marks": [1, 3, 5, 7],
    "anotherdict": {'Aayush': 'player'},
    1: 2
}
print(type(myDict.keys()))  # Prints the keys of the dictionary
print(list(myDict.keys()))
print(myDict.items())
print(myDict)
updateDict = {
    "Aayush Ad": "Freind",
    "Sonica ad": "Freind",
    "Safal bh": "Freind",
}
myDict.update(updateDict)  # update the dictionary by adding the function
print(myDict)

print(myDict.get("Aayush 6")) #Returns none
print(myDict["Aayush"]) #throws error as aayush2 is not present in the dictionary