'''
things to include:
- keep track of score as user takes quiz
- reveal score at the end of the quiz
- use classes, if statements, loops, etc
- include all questions in question_prompts
'''


question_prompts = [
	"What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
	"What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
	"What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]



def question_answer(message, question_num):

	correct_count = 0 
	incorrect_count = 0 

	if question_num == 1:
		if message.lower() == "a":
			
			correct_count += 1 
			return
		if message.lower() in ["b", "c"]:
			incorrect_count += 1 
			return
		else: 
			print("\nPlease answer with a, b, or c \n")
			question_answer(input("What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n"))

	if question_num == 2:
		if message.lower() == "c":
			correct_count += 1 
			return
		if message.lower() in ["b", "a"]:
			incorrect_count += 1 
			return
		else: 
			print("\nPlease answer with a, b, or c \n")
			question_answer(input("What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n"))

	if question_num == 3:
		if message.lower() == "b":
			correct_count += 1 
			return
		if message.lower() in ["c", "a"]:
			incorrect_count += 1 
			return
		else: 
			print("\nPlease answer with a, b, or c \n")
			question_answer(input("What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"))

	if correct_count > incorrect_count:
			print("You passed the test :) \nYou got", correct_count,"right and", incorrect_count ,"wrong!")

	if correct_count < incorrect_count:
		print("You failed the test :(  \nYou got", correct_count ,"right and", incorrect_count ,"wrong!")



def quiz(): 
	
	if y_n or play_again == "y":
			question_answer(input("\nWhat color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n"), 1)

			question_answer(input("\nWhat color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n"), 2)

			question_answer(input("\nWhat color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"), 3)

			play_again = input("Would you like to play again? (y/n): ")

			if play_again.lower() == "y":
				quiz()
				
			if play_again.lower() == "n":
				print("Maybe another time!")
				return

			while play_again.lower() != ["y", "n"]:
				play_again = input("Please respond with y or n! Would you like to take the test again? (y/n): ")
				


		
y_n = input("Would you like to take a quiz? (y/n): ")
quiz()
			


