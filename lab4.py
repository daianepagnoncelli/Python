myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

#print(myFruitList[0]) #substitua por 1,2 e verifique

myFruitList[2] = "orange"
print(myFruitList)

#tupla - lista imutavel

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)         
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0]) #substitua por 1,2 e verifique

#dictionary - lista com posicoes nomeadas
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])