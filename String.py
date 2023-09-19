#string is defined as set og characters
name_1 = "Monika"
name_2 = 'Karthika'
name_3 = "Monika 'elder sister' is Karthika"
name_4 = 'Karthika "younger sister" is Monika'
print (name_1)
print (name_2)
print (name_3)
print (name_4)
#upper() is a method. 
print (name_1.upper()) #invoking a method
print (name_1.lower())
print (name_3.title())
print (name_1 + name_2)
print (name_1 + " " + name_2) # " " - this double quote is for gap between name_ and name_2
print ("Karthika \n food") # \n - is used for next line
print ("Karthika \t food") # \t - is used for tab space.\- escape sequence
# length of message = name_3
print (len(name_3))
#find a letter
print (name_1.find("i"))
#count a letter
print (name_2.count("a"))
#replace a letter
print (name_1.replace("k","g"))
#check if it is a alphabet
print (name_1.isalpha())
#check if it is a number
print (name_1.isdigit())
#print a word 10 times
print (name_1 *10)
#space in output between  name and another name
print ((name_1+" ")*10)
#multiple assignments
name, age, height = "Monika", 22, 153
print (age)
like = dislike = 100
print (dislike)