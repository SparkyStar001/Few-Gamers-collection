import random
import pyttsx3

class VoiceAssistant:
    def __init__(self, rate=180, volume=1.0):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

    def speak(self, text):
        print(text)
        self.engine.say(text)
        self.engine.runAndWait()

class Game:
    def __init__(self, voice: VoiceAssistant):
        self.voice = voice

    def start(self):
        raise NotImplementedError("Game must implement the start method.")

class RockPaperScissors(Game):
    def start(self):
        self.voice.speak("Welcome to Rock Paper Scissors!")
        choices = ["rock", "paper", "scissors"]
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        computer_choice = random.choice(choices)

        self.voice.speak(f"The computer chose {computer_choice}.")
        if user_choice == computer_choice:
            self.voice.speak("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.voice.speak("You win!")
        else:
            self.voice.speak("You lose!")

class GuessTheNumber(Game):
    def start(self):
        self.voice.speak("Welcome to Guess the Number!")
        number = random.randint(1, 100)
        attempts = 0

        while True:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < number:
                self.voice.speak("Too low!")
            elif guess > number:
                self.voice.speak("Too high!")
            else:
                self.voice.speak(f"Correct! You guessed it in {attempts} attempts.")
                break

class HardGuess(Game):
    def start(self):
        self.voice.speak("Welcome to Hard Guess Mode!")
        attempts = 0

        while True:
            number = random.randint(1, 10)
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1

            if guess == number:
                self.voice.speak("Congratulations You did it")
                break
            else:
                self.voice.speak("Try Again !")


class Cricket(Game):
    def start(self):
        self.voice.speak("Welcome to Cricket!")
        player_runs = 0

        while True:
            player_choice = int(input("Enter your run (1-6, 0 to stop): "))
            if player_choice == 0:
                break

            computer_choice = random.randint(1, 6)
            self.voice.speak(f"Computer bowled {computer_choice}")

            if player_choice == computer_choice:
                self.voice.speak(f"You're OUT! Final score: {player_runs}")
                break
            else:
                player_runs += player_choice
                self.voice.speak(f"Your score is now {player_runs}")

class GameManager:
    def __init__(self):
        self.voice = VoiceAssistant()
        self.games = {
            "1": RockPaperScissors(self.voice),
            "2": GuessTheNumber(self.voice),
            "3": HardGuess(self.voice),
            "4": Cricket(self.voice)
        }

    def menu(self):
        while True:
            self.voice.speak("\nChoose a game:")
            print("1. Rock Paper Scissors")
            print("2. Guess the Number")
            print("3. Hard Guess")
            print("4. Cricket")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "5":
                self.voice.speak("Goodbye!")
                break
            elif choice in self.games:
                self.games[choice].start()
            else:
                self.voice.speak("Invalid choice, please try again.")


if __name__ == "__main__":
    gm = GameManager()
    gm.menu()
