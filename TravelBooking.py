# Task Travel booking

# Define the Function
def ticketprice():
    age = int(input("Enter Age :"))
    adult = 50
    seniorcitizen = 20 * adult / 100
    dis_seniorcitizen = adult - seniorcitizen
    children = 30 * adult / 100
    dis_children = adult - children

# Using conditional statements to calculate ticket price based on age.
    if age >= 18 and age <= 60:
        print("Ticket Price for Adult: ",f"${adult}")
    elif age < 18:
        print("Ticket Price for Chilren : ",f"${dis_children}")
    else:
        print("Ticket Price for SeniorCitizen : ",f"${dis_seniorcitizen}")

# Calling the function
ticketprice()
