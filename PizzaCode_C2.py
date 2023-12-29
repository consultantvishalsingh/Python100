print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N\n") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N\n") # Do you want extra cheese? Y or N
# Write your code below this line 👇
peperoni=0
cheese=0
bill=0

if size=="S":
  bill=15
  if add_pepperoni=="Y" and extra_cheese=="Y":
    bill+=3
    print(f"Your final bill with Peproni & Cheese is: ${bill}.")
  elif add_pepperoni=="Y" and extra_cheese=="N":
    bill+=2
    print(f"Your final bill with Peproni is: ${bill}.")
  elif add_pepperoni=="N" and extra_cheese=="Y":
    bill+=1
    print(f"Your final bill with Cheese is: ${bill}.")
  else:
    print(f"Your final bill without peperoni and cheese is: ${bill}.")

if size=="M":
  bill=20
  if add_pepperoni=="Y" and extra_cheese=="Y":
    bill+=4
    print(f"Your final bill with Peproni & Cheese is: ${bill}.")
  elif add_pepperoni=="Y" and extra_cheese=="N":
    bill+=3
    print(f"Your final bill with Peproni is: ${bill}.")
  elif add_pepperoni=="N" and extra_cheese=="Y":
    bill+=1
    print(f"Your final bill with Cheese is: ${bill}.")
  else:
    print(f"Your final bill without peperoni and cheese is: ${bill}.")
if size=="L":
  bill=25
  if add_pepperoni=="Y" and extra_cheese=="Y":
    bill+=4
    print(f"Your final bill with Peproni & Cheese is: ${bill}.")
  elif add_pepperoni=="Y" and extra_cheese=="N":
    bill+=3
    print(f"Your final bill with Peproni is: ${bill}.")
  elif add_pepperoni=="N" and extra_cheese=="Y":
    bill+=1
    print(f"Your final bill with Cheese is: ${bill}.")
  else:
    print(f"Your final bill without peperoni and cheese is: ${bill}.")

else:
  print("Please choose a valid size of Pizza S,M,L. Or You want Just Coke and burgers?")