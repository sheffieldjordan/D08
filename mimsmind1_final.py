import random # imports the 'random' module to we can generate a random number using the randrange function

print('Let\'s play MIMS Mind!') # printed to get he user excited about playing

while True: # loop the below until broken out
	try: # test for an exception
		random_length = input("How many digits?: ") # generate random number equal in digits to the length specified by the user
		if random_length == '': # default length is 3 is none entered
			random_length = 3 
			break # break out of the loop
		elif int(random_length) <= 0: # if you enter '0' as you're length, you'll be corrected. You can't have a number with length 0
			print("Sorry, positive whole numbers only please")
			continue
		else:
			break	
	except ValueError: # Exception for something entered besides integers
		print("Sorry, positive whole numbers only please")
		continue
print("You have {} guesses total.".format(2**int(random_length) + int(random_length))) # prompt for guess, announcing the number of digits expected: 2 to the length-power + the length

random_number = random.randrange(0, 10**int(random_length)-1) # generates the random number between 0 and 10 to the length-power minues one, giving you the correct range of integers.
random_number = str(random_number).zfill(int(random_length)) # pads the random number with zeroes in the front. So if the random number is 43, but the user specified 3 digits, the result here would be 043. 
print(random_number)
tries = 0 # tracks the number of attempts the user makes 
while tries < 2**int(random_length) + int(random_length): # loop below while the number of tries is less than the specified value

# provide feedback based on the guess
	# A matching digit in the correct position will result in a 'bull'
	# a matching digit in the worng position will result in a 'cow'

	try: # throw an exception if user guess is not an integer
		user_guess = int(input("Guess a {} digit number!: ".format(random_length)))
	except ValueError: 
		print("Sorry, positive whole numbers only please")
		continue
	user_guess = str(user_guess).zfill(int(random_length)) # pads the user's guess with extra zeroes so the index check later doesn't throw an error. If you don't .zfill here and input 043, the variable will store only 43. 
	idx = 0 # sets the index for the upcoming digit check
	tries += 1 # increases the tries counter for every guess
	if str(user_guess) == random_number: # checks first if your guess is correct!
			print("Congratulations! You guessed correctly in {} tries!".format(tries))
			break #breaks when correct
	while idx <= len(str(random_number))-1: # execute the loop below while the index to be checked is less than or equal to the length of the random number 
		bull = 0 # sets bull and cow equal to zero, ready to count
		cow = 0
		for digit in str(random_number): # loops through each digit in random_number 
			if str((str(random_number)[idx])) == str((str(user_guess)[idx])): # if the numbers at an index are equal,
				bull += 1 # Bull + 1!
			elif str(random_number)[idx] != str(user_guess)[idx] and str(random_number)[idx] in str(user_guess): # if the numbers at an index are not equal AND the number is in user's guess,
				cow += 1
			else:
				cow += 0
				bull += 0
			idx += 1 # increase idx so we can check all the indices 
		continue
	
	print("{} bull(s), {} cow(s). Try again: ".format(bull, cow))	
	continue
if tries == 2**int(random_length) + int(random_length) and user_guess != random_number:
	print("Sorry! You've exceedeed your maximum attempts for MIMS Mind1!")	
print("The number was", random_number, "all along.")

