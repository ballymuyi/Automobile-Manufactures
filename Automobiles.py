# To start a new program question. The program to print car types available and to indicate the leading ones in Germany
# by turning them to capital letter.
print("The program start here!")

Car_list = ["acura", "subaru", "audi", "skoda", "fabia", "bmw","toyota","volkswagen","honda","mercedes-benz","bentley",
            "ford", "vibe", "rolls royce","geely","mitsubishi", "lexus",]
for car in Car_list:
    if car == "bmw":
        print(car.upper())
    elif car == "audi": # It is just like "if" and it can come up as many as we want bcos it acts in a case where you
        # need to use "if" again
        print(car.upper())
    elif car == "mercedes-benz":
        print(car.upper())
    else:
        print(car.title()) # This means to print other cars in title case.

Car_list.extend(["infinity", "mazda", "jaguar", "kia", "tesla", "porsche"]) # The extend command can take more than one
# argument which would be in square bracket, to add to an element of a LIST!.
Car_list.append("gmc") #The command can only take a single element as its argument to be added to our list
print(Car_list)


print("The program ends here!")
print("The program start here for in-cooperating range to just print out 20 cars out of the total number cars!")

for car in range(20): # In-cooperating range to just print out 20 cars out of the total number cars!
    print(Car_list[car]) # To print the car list in range of 20 within the Car_list.



print("The program start here to print all the cars in the list in upper case!")
for car in Car_list:
    print(car.upper())
print(len(Car_list)) # To the length number of the car in our list.



print("The program start here to print all the cars in the list that has the following letters in their spellings!")
print("The cars are:exit")
for car in Car_list:
    if "le" in car:
        print(car)
    elif "m" in car:
        print(car)
    elif "f" in car:
        print(car)
    elif "t" in car:
        print(car)
print("The end" )

