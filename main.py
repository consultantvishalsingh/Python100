print("Welcome to Tip Calculator")
# 1st input:
bill =float(input("Please Enter your bill $\n"))
# 2nd input:
tip = float(input("tip you want to give 5,10,15\n"))
# 🚨 Don't change the code above 👆
# 3rd input:
people = int(input("How many people to split the bill?\n"))
final_share = bill*(1+tip/100)
per_head = final_share/people
print(f"Each person should pay {round(per_head,2)}")
