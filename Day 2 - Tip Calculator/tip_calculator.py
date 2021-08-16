#Demonstrates:
#Primitive data types, Type conversion, Mathematical operators, Number manipulation, F strings 

print("Welcome to the tip calculator!\n")

bill_total = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? " ))

amount_to_be_payed = round(bill_total * (1 + tip_percentage / 100) / number_of_people, 2)
amount_to_be_payed = "{:.2f}".format(amount_to_be_payed)

print(f"Each person should pay: ${amount_to_be_payed}")
