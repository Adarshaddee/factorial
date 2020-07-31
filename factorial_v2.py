
while True:

	print("\n\t\t<======== Welcome ========>\t\t")

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
			
		print("\nThe factorial of",num_ch1,"is ", fact(num_ch1),"\n\n")
	
	elif user_ch == 2:
		num_ch2 = int(input("\nEnter your Factorial Number: \nAD4rSH_> "))
			
		fac = 1
		print("\n")
		for i in range(1, num_ch2+1):
			fac = fac * i
			print(f"The factorial is   {fac}")
				
	elif user_ch == 3:
		print("\n Bye - Bye, See You Again :-)\n\n")
		break
		
	else:
		print("\nPlease Enter A Valid Value\n\n")

