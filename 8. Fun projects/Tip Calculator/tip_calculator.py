# Tip Calculator - Split the Bill 
full_amount = float(input("How much is the bill? "))
people = int(input("How many people are splitting the bill? "))
tip_percent = float(input("What percent tip do you want to leave? "))

pay_per_person = round((full_amount * (1 + tip_percent/100))/people, 2)
print(f"Each person should pay: {pay_per_person:.2f}")

