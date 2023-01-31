print('☆ Welcome to Tip Calculator ☆')
bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
people = int(input('How many people to split the bill? '))

tip_as_percent = tip / 100
tip_amount = bill * tip_as_percent
final_bill = bill + tip_amount
splited_bill = final_bill / people

print(f'Each person should pay: ${round(splited_bill, 2)}')