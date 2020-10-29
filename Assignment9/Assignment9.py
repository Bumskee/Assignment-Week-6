def replaceDuplicate(string):
    '''This function will check wether the text has any duplicate symbols (mainly : ".", "?", "!")'''
    global sample
    #this will go through all of the character inside the string
    for s in range(len(string)):
        #checks if the character is a "." then will check if subsequent characters are also the same. If it is it will then replace all the symbols with p(number of symbols)
        if string[s] == ".":
            dup = [string[s]]
            if string[s] == string[s + 1]:
                i = 1
                while string[s] == string[s + i]:
                    dup = dup + [string[s + i]]
                    i += 1
                dup = "".join(dup)
                sample = sample.replace(dup, ("p{amount}".format(amount = len(dup))))
                #checks if the character is a "!" then will check if subsequent characters are also the same. If it is it will then replace all the symbols with e(number of symbols)
        if string[s] == "!":
            dup = [string[s]]
            if string[s] == string[s + 1]:
                i = 1
                while string[s] == string[s + i]:
                    dup = dup + [string[s + i]]
                    i += 1
                dup = "".join(dup)
                sample = sample.replace(dup, ("e{amount}".format(amount = len(dup))))
                #checks if the character is a "?" then will check if subsequent characters are also the same. If it is it will then replace all the symbols with q(number of symbols)
        if string[s] == "?":
            dup = [string[s]]
            if string[s] == string[s + 1]:
                i = 1
                while string[s] == string[s + i]:
                    dup = dup + [string[s + i]]
                    i += 1
                dup = "".join(dup)
                sample = sample.replace(dup, ("q{amount}".format(amount = len(dup))))

#would be used later as part of the variable for replacing back all of the character that the programs substitute
i = 0    

#opens the file in read mode
with open("fart.txt", "r", encoding = "utf-8") as f:
    #replaces all of the exception on the split delimiter with unique characters and also remove newlines if there are any
    sample = f.read().replace("\n", "")
    sample = sample.replace("Mr.", "Mr").replace("Ms.", "Ms").replace("Mrs.", "Mrs").replace("Dr.", "Dr").replace("Jr.", "Jr").replace("i.e.", "abr,ie")
    replaceDuplicate(sample)
    #converts the string into a list with ". " as the delimiter
    sample = sample.split(". ")
    #replaces back the substitution with its original form on every single element of the list of sentences
    for i in range(len(sample)):
        sample[i] = sample[i].replace("p3", "...")
        sample[i] = sample[i].replace("q3", "???")
        sample[i] = sample[i].replace("e3", "!!!")
        sample[i] = sample[i].replace("Mr", "Mr.")
        sample[i] = sample[i].replace("Ms", "Ms.")
        sample[i] = sample[i].replace("Mrs", "Mrs.")
        sample[i] = sample[i].replace("Dr", "Dr.")
        sample[i] = sample[i].replace("Jr", "Jr.")
        sample[i] = sample[i].replace("abr,ie", "i.e.")
        i += 1

#prints the result
print(sample)
