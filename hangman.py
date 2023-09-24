import random

attempts = 8
won = False
answer = list(random.choice(['python', 'java', 'swift', 'javascript']))
answered = list('-' * len(answer))
history = set()

games_won = 0
games_lost = 0

def check_letter(ch):
    global attempts
    global history
    if len(ch) != 1:
        print('Please, input a single letter.')
        return
    if not ch.islower():
        print('Please, enter a lowercase letter from the English alphabet.')
        return
    if ch in history:
        print("You've already guessed this letter.")
        return
    if ch in answered:
        attempts -= 1
        print('No improvements.')
        return
    if ch not in answer:
        attempts -= 1
        print("That letter doesn't appear in the word")
        return
    for i, c in enumerate(answer):
        if c == ch:
            answered[i] = ch

while True:
    print("H A N G M A N")
    menu_choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')

    if menu_choice == "play":
        attempts = 8
        answer = list(random.choice(['python', 'java', 'swift', 'javascript']))
        answered = list('-' * len(answer))
        history = set()
        won = False

        while attempts > 0 and not won:
            if '-' not in answered:
                won = True
                continue
            print(f"\n{''.join(answered)}")
            letter = input('Input a letter: ')
            check_letter(letter)
            history.add(letter)

        if won:
            games_won += 1
            print(f'\nYou guessed the word {"".join(answer)}!\nYou survived!')
        else:
            games_lost += 1
            print(f'\nYou lost!')

    elif menu_choice == "results":
        print(f'You won: {games_won} times')
        print(f'You lost: {games_lost} times')

    elif menu_choice == "exit":
        break

    else:
        print('Invalid choice. Please choose "play", "results", or "exit".')
