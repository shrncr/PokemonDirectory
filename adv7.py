#Sara Hrnciar
#CSC 101
#Lori
#Pokemon directory!!
#import pandas to hold the dataframe
import pandas as pd

#create your pokemon class with instance variables for its name, abilities, and classification
class Pokemon:
    def __init__ (self, abilities, classification, name):
        self.abilities = abilities
        self.classification = classification
        self.name = name
    @property
    def name(self):
        return self.name
    @name.setter
    def name(self, n):
        self.name = n
    def __repr__(self):
        return repr("My name is " + self.name + ", and my abilities consist of: " + self.abilities + ". I actually am classified as " + self.classification + "!")
        
#Read in your df, rename it and reset its index values
pokesterz = pd.read_csv(r"C:\Users\lovey\Downloads\adv7poke.csv")
pokeSorted = pokesterz.sort_values(by = "name", ascending = True)
pokeSorted = pokeSorted.reset_index()

#empty array to hold your pokemon objects
arrPoke = []

#create your pokemons and fill up the array w/ them
for i in range(0, len(pokeSorted.name)):
    tempAbil = pokeSorted.loc[i, 'abilities']
    tempClass = pokeSorted.loc[i, 'classfication']
    tempName = pokeSorted.loc[i, 'name']
    arrPoke.append(Pokemon(tempAbil, tempClass, tempName))

#user enters pokemons' names until theyre done 
def findingPokemon():
    whichPoke = input("Hey! Welcome to the pokemon database. Enter which pokemon you'd like to find or press Q to quit ")
    if whichPoke.upper() == "Q":
        print("ok, fine")
    else:
        print(whichPoke)
        print(str(binSearch(whichPoke, arrPoke)) + "\n")
        findingPokemon()

#bin search to find the pokemon rhe user asked for
def binSearch(pokeToLookFor, allPokes):
    first = 0
    last = len(allPokes) - 1
    
    while first<=last:
        mid = (first+last)//2
        if allPokes[mid].name == pokeToLookFor:
            return allPokes[mid]
        else:
            if first == last:
                return("Sorry, no pokemon with this name.")
            else:
                if allPokes[mid].name < pokeToLookFor:
                    first = mid + 1
                else:
                    last = mid - 1
findingPokemon()
