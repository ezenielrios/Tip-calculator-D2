print("Welcome to the tip calculator")

Bill = float(input("what was the total bill? $")) #input to get bill amount saved into a variable and converted into float to allow calculations

tip = int(input("How much tip would you like to give? 10,12,or 15? ")) #input tip info saved into variable and converted string to int for calculations

people = int(input("How many people to split the bill?")) #input people to divide by, data converted and saved into variable

bill_with_tip = tip / 100 * Bill + Bill # tip calculation variable

bill_per_person = bill_with_tip / people # per person calculation variable

Final_amount = round(bill_per_person, 2) #final bill rounded to two decimals

print(f"Each persoin should pay ${Final_amount}") #utilised an f string for readability and simpler formatting 
