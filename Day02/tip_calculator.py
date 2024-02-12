# Show a welcome note
print("Welcome to the tip calculator.")
# Ask for the bill
bill = float(input("What was the total bill? $"))
#Ask for the tip
tip = int(input("What percentage tip whould you like to give? 10 or 12 or 15? "))
#calculate the tip number
tip_to_pay = bill * tip/100
#Ask for the number of pepole that split the bill
number_of_people = int(input("How many people to split the bill? "))
#calculate each person's bill
bill_for_each_person = "{:.2f}".format((bill + tip_to_pay) / number_of_people, 2)
#show them how much should pay
print(f"Each person should pay: ${bill_for_each_person}")