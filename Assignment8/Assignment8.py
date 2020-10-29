#Imported the time module because im curious how long the code took to run lol
import time

#Copy the pokemon names in the form of a string into a variable called pokmens
pokmens = "audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"
#convert the string inside the pokmens variable into a list called pokmens
pokmens = pokmens.split(" ")

#make a new dictionary from the data of pokmens string
pokmensDict = {}
#The loop will check if a key being the first character of an element inside the pokmens list is present inside the the dictionary
#If it is not present it will create a new key being the first character and the value inside being the pokemon name itself
#If it is present, it will append the key's value with the pokemon name
for pokmen in pokmens:
    if pokmen[0] not in pokmensDict:
        pokmensDict[pokmen[0]] = [pokmen]
    else:
        pokmensDict[pokmen[0]].append(pokmen)

#global variable that will be appended later in the function to add pokemons into the chain
longestChain = []

def pokmenGen(chain):
    '''A function that generates a chain of pokemon names by taking a pokemon as the argument as the first pokemon name in the generated list.'''
    #use global so that the value of the variable could be modified by the function
    global longestChain

    #checks if the longest_chain is bigger or smaller than the chain that the function will generate 
    #and change the longest_chain into the chain that the function generates if it is smaller than the generated chain
    if len(longestChain) < len(chain):
        longestChain = chain

    #Checks if the first letter of a pokemon is available as a key in the pokemon dictionary
    if chain[-1][-1] in pokmensDict:
        #loop through all of the key being the last letter of the last pokemon inside the chain
        for pokmen in pokmensDict[chain[-1][-1]]:
            #will append the pokemon name if the pokemon name is not yet in the chain
            if pokmen not in chain:
                pokmenGen(chain + [pokmen])

#Start timer and runs the function                
start = time.time()    
for pokmen in pokmens:
    pokmenGen([pokmen])
end = time.time ()

#prints the result and also the time it took for the program to run
print(longestChain)
print("\nThere are", (len(longestChain)), "Pokmens in the chain")
print("This code took", str((end - start)), "to run")