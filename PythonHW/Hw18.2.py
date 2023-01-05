#Create a program that will output everything in lowercase whatever the user will input.
# The program should run until the user enters the word “STOP”.

#Exersise1

program = True
while program:
    user_input = input("Type a word ,or STOP to exit\n").lower()
    if user_input == "stop":
       program = False

print("You typed", user_input)


#Exersise2

my_dict = {'Jake': '$100K', 'Anand': '$120K'}
for key,value in my_dict.items():
    print(key, "salary", value, " a year")


#Exersise3

my_tuple = (4, 30, 2017, 2, 27)
print("{} {} {} {} {}".format(my_tuple[3],my_tuple[4],my_tuple[2], my_tuple[0], my_tuple[1]))





