stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
import random

chosen_word = word_list[random.randint(0, len(word_list) - 1)]
print(chosen_word)
display = []
for i in chosen_word:
    display += "_"
print(display)
temp = 0;
NoDisplay = False
lives = 6
while not NoDisplay:
    guess = input("guess a letter : ").lower()
    count = 0;
    if guess in chosen_word:
        for letter in chosen_word:
            if letter == guess:
                display[count] = guess
                temp += 1

            count += 1

    else:
        lives -= 1
        print("Error 404")
    print(lives)
    if temp == len(chosen_word):
        print("You have won")
        NoDisplay = True
    elif lives == 0:
        print("Game is over")
        NoDisplay = True
    print(display)
    print(stages[lives])
