""" 
# How To Read Input String using Split
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split()# white space by default
y = txt.split(" ")
z = txt.split(",")
a = txt.split("is")

print(x)
print(y)
print(z)
print(a)

# Converting to Int (for(i=0;i<len(sud_ht);i++)   
total_height,nos = 0,0
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n]) #Same Name List is needed to change to Int else it will give little trouble
   total_height += height
   number_of_students += 1
"""


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
