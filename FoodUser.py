#Define a function for donating food
def donate_food():
    #Ask user for name
    name = input("What is your name? ")
    #Ask user for type of food
    food_type = input("What type of food do you want to donate? ")
    #Ask user for quantity
    quantity = input("How much food do you want to donate? ")
    #Ask user for address
    address = input("What is your address? ")
    #Ask user for contact number
    contact_number = input("What is your contact number? ")
    #Print out information
    print("Name:", name)
    print("Food type:", food_type)
    print("Quantity:", quantity)
    print("Address:", address)
    print("Contact number:", contact_number)
    #Confirm donation
    confirmation = input("Do you want to confirm your donation? (Yes/No) ")
    if confirmation == "Yes":
        print("Thank you for donating food!")
    elif confirmation == "No":
        print("Donation cancelled")
    else:
        print("Invalid input, donation cancelled")

#Call the function
donate_food()