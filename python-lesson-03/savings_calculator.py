money_start = (input('Enter starting balance: $'))
saving_years = (input('Enter number of years: '))
interest_rate = (input("What is the % interest rate: "))
money_result = round (float(money_start) * float(interest_rate) * float(saving_years), 2)
print(f"Your savings after {saving_years} years is ${money_result}")
afford_holiday = money_result > 10000
print(f"Will you be able to afford your holiday? {afford_holiday}")