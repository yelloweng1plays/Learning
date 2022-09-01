WeeklyIncome = float(input("Input weekly pocket money: £"))
WeeklyExpendeture = float(input("Input usual spendeture weekly: £"))

WeeklyExpendable = WeeklyIncome - WeeklyExpendeture

print(f"You currently recieve £{WeeklyExpendable*52} per year after what you spend weekly. \n Without a weekly expendeture of £{WeeklyExpendeture} you could have £{WeeklyIncome*52}!")
