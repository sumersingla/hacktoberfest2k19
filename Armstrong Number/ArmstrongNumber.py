number= int(input("Enter a number to check if it is an Armstrong Number: "))
new_number=0
temp=number
while temp > 0:
   digit = temp % 10
   new_number += digit ** 3
   temp //= 10
if number == new_number:
    print("The number is an Armstrong number")
else:
    print("It is not an Armstrong Number")
