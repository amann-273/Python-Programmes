user_input = str(input("Enter a Phrase: ")) # take input from user
text = user_input.split() # apply spaces between the string
a = " " # space for iterating in loop
for i in text: 
    a = a+str(i[0]).upper() # finding and adding the first letter and printing in upper case
print(text)
print(a) # printing the acronym
