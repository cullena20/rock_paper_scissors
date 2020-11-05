import random


class RockPaperScissors:

    def __init__(self):
        self.default_options = ["rock", "paper", "scissors"]
        self.options = list()
        self.user = {'name': None, 'rating': None}

    # checks if user is in rating_sheet. If not, a new entry is created
    # initializes self.user with name and rating in rating_sheet or name and rating of 0
    def identity(self):
        name = input("Enter your name: ")
        print(f"Hello, {name}")
        with open('rating.txt', 'r') as rating_sheet:
            for line in rating_sheet.readlines():
                if line.strip():
                    f_name, rating = line.split()
                    if name == f_name:
                        self.user['name'] = f_name
                        self.user['rating'] = int(rating)
        if self.user['name'] is None:
            self.user['name'] = name
            self.user['rating'] = 0
            with open('rating.txt', 'a') as rating_sheet:
                print(self.user['name'], self.user['rating'], file=rating_sheet)

    # before program is terminated, the score_sheet is updated with the user's current rating
    def update_rating_sheet(self):
        with open('rating.txt', 'r') as rating_sheet:
            lines = rating_sheet.readlines()
        with open('rating.txt', 'w') as rating_sheet:
            for line in lines:
                if line.startswith(self.user['name']):
                    print(self.user['name'], self.user['rating'], sep=" ", end='\n', file=rating_sheet)
                else:
                    print(line, end='', file=rating_sheet)

    def get_options(self):
        options = input("Enter your options: (to play classic rock, paper, scissors just click enter)\n")
        if options == '':
            self.options.extend(self.default_options)
        else:
            self.options.extend(options.split(','))

    def display_results(self, u_choice, c_choice):
        rearranged_options = self.options[self.options.index(u_choice) + 1:]
        rearranged_options += self.options[:self.options.index(u_choice)]
        c_win = rearranged_options[:len(rearranged_options) // 2]
        if c_choice in c_win:
            print(f"Sorry, but the computer chose {c_choice}")
        elif u_choice == c_choice:
            print(f"There is a draw ({c_choice})")
            self.user['rating'] += 50
        else:
            print(f"Well done. The computer chose {c_choice} and failed")
            self.user['rating'] += 100

    def play(self):
        print('''*********************
 ROCK PAPER SCISSORS
*********************\n''')
        self.identity()
        self.get_options()
        print("Okay, let's start")
        while True:
            u_choice = input().casefold()
            if u_choice == "!exit":
                self.update_rating_sheet()
                print("Bye!")
                break
            elif u_choice == "!rating":
                print(f"Your rating: {self.user['rating']}")
                continue
            elif u_choice not in self.options:
                print("Invalid input")
                continue
            else:
                c_choice = random.choice(self.options)
                self.display_results(u_choice, c_choice)


your_game = RockPaperScissors()
your_game.play()
