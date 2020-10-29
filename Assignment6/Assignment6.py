#Opens the file in read mode
with open("test.txt", "r", encoding = "utf-8") as f:
    #assigning the lines in the form of a list into the variable called lines
    lines = f.read().split("\n")
    #an empty list called new_lines that would be appended and used as the data to be written into the new file
    new_lines = []
    #variable i as the numering for the line
    i = 1
    #loop that will append the values of the lines list into the new_lines list and giving the numering in the front of the values then incrementing i by 1
    for line in lines:
        new_lines.append((str(i) + ". " +  line))
        i += 1
    #using .join method to convert the list into a string and having newline as the separator for the strings
    new_lines = "\n".join(new_lines)


#Creates a new file called new_file.txt and overwrite it with the value of new_lines
with open("new_file.txt", "w", encoding = "utf-8") as f:
    f.write(new_lines)

