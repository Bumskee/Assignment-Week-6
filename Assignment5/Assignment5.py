#Opens the file in read mode.
with open("Jack Manly.txt", "r") as f:
    #creating a list consisting of all of the words inside the text file replacing all of the symbols that i could think of with an empty string.
    words = list(f.read().lower().replace("\n", " ").replace(".", " ").replace("!", " ").replace("?", " ").replace('"', " ").replace("'", " ").replace(":", " ").replace("(", " ").replace(")", " ").replace(",", "").split(" "))
    #creates an empty list that could be appended later for the final answer.
    hapax = []
    #loop that would go through all the values inside the words list and then counting every reoccurences inside the list.
    for word in words:
        counter = words.count(word)
        #creating a condition when the words only shows once on the text, it will be appended into the empty hapax list.
        if counter == 1:
            hapax.append(word)
    #prints the hapax list as the final answer.
    print(hapax)

