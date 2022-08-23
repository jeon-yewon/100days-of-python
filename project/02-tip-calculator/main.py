#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
percent_tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?" ))

calc_tip = total_bill * (1 + 0.01 * percent_tip) / people
calc_tip_round = round(calc_tip, 2)
#소수점 2째자리까지 확실하게 표현하기
calc_tip_2f = "{:.2f}".format(calc_tip)

message = f"Each person should pay: ${calc_tip_2f}"
print(message)