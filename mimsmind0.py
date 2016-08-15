import random

print('Let\'s play MIMS Mind!')

while True:
	try: 
# generate random number equal in digits to the length specified by the user
		random_length = input("How many digits?: ") #2 #3
# default length is 1 is none entered
		if random_length == '':
			random_length = 1
			break
		elif int(random_length) <= 0:
			print("Sorry, positive whole numbers only please")
			continue
		else:
			break	
	except ValueError:
		print("Sorry, positive whole numbers only please")
		continue
random_number = random.randrange(0, 10**int(random_length)-1)

# prompt for guess, announcing the number of digits expected
count = 0
while True:
# provide feedback based on the guess
	# correct, you guessed X times 
	# higher, next guess
	# lower, next guess	
	try:
		user_guess = int(input("Guess a {} digit number!: ".format(random_length)))
	except ValueError:
		print("Sorry, positive whole numbers only please")
		continue
	if user_guess < random_number:
		count += 1
		print("Guess higher!")
	if user_guess > random_number:
		count += 1
		print("Guess lower!")
	if user_guess == random_number:
		count += 1
		print("Congratulations! You guessed correctly in {} tries!".format(count))
		break
	continue
	


