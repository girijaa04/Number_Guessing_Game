import random
def NGG(Diff) :
 while True:
     
     if Diff == '1':
         secret_number = random.randint(1, 100)
         print("\n--- Number Guessing Game ---")
         print("I have picked a number between 1 and 100. Can you guess it?")
     elif Diff == '2':
         secret_number = random.randint(1, 50)
         print("\n--- Number Guessing Game ---")
         print("I have picked a number between 1 and 50. Can you guess it?")
     else:
         secret_number = random.randint(1, 10)
         print("\n--- Number Guessing Game ---")
         print("I have picked a number between 1 and 10. Can you guess it?")
     attempts = 0

     while True:
         try :
         
          guess = int(input("Enter your guess: "))
          attempts += 1

          if guess < secret_number:
              print("Too low! Try a higher number.")
          elif guess > secret_number:
              print("Too high! Try a lower number.")
          else:
              print(f"Correct! You guessed it in {attempts} attempts!")
              print("Attempts taken :",attempts)
              break
         except ValueError :
             print("Please enter a valid number ... ")


     play_again = input("Play again? (yes/no): ")
     if play_again.lower() == "no":
         print("Thanks for playing! Bye!")
         break

Diff = int(input(" Pick a difficulty level (1: Hard , 2: Medium, 3: Easy ): "))
NGG(Diff)
