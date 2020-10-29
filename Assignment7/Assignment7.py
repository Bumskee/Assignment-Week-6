#Opens the file in read mode
with open("WreckedOnSpiderIsland.txt", "r") as f:
    #Assigning the words inside the text file in the form of a list called text
    text =list(f.read().lower().replace("\n", " ").replace(".", " ").replace("!", " ").replace("?", " ").replace('"', " ").replace("'", " ").replace(":", " ").replace("(", " ").replace(")", " ").replace(",", "").split(" "))
    #Assigning the length of the text list into a variable called words
    words = len(text)
    #creates a variable called letters that has the initial value of zero that is going to be added by the amount of character inside the text list later
    letters = 0
    #Creates a loop that will go trough all of the words/elements inside the text list and then adding the length of each elements/words to the letters variable
    for i in range(words):
        letters += (len(text[i]))

#calculates the average by dividing letters by words
average = (letters / words)

#prints the value of average to the console.    
print(average)
