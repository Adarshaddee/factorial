

print("\t\t<======== Welcome ========>\t\t")

print("\n [01] . Only Value")
print(" [02] . From Value")
print(" [03] . Exit")

user_ch = int(input("\nEnter Your Choice: \nAD4rSH_> "))

if user_ch == 1:
	
	num_ch1 = int(input("\nEnter Your Facrorial Number: \nAD4rSH_> "))
	
	def fact(num):
		if num == 0 or num == 1:
			return 1
			
		else:
			return num * fact(num-1)
			
	print(fact(num_ch1))
	
elif user_ch == 2:
	num_ch2 = int(input("\nEnter your Factorial Number: \nAD4rSH_> "))
			
	fac = 1
	for i in range(1, num_ch2+1):
		fac = fac * i
		print(fac)
				
elif user_ch == 3:
	print("\n Bye - Bye, See You Again")
	while True:
		break
		
else:
	print("\nPlease Enter A Valid Value")