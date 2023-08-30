myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
     "Vastu": "Item"
}
print("The options are",myDict.keys())
a = input("Enter the nepali word\n")
# Below line will not display any error when other key are entred
print("The meaning of your word is:",myDict.get(a))