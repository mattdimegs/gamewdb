import mysql.connector
import random
import hashlib

db = mysql.connector.connect(
    host="69.122.121.144",
    user="gamedb",
    passwd="YellowBird1873!",
    database='game'
)
mycursor = db.cursor()

player = ''

def questions():
    returning = input('Returning User? y/n: ')
    if returning == 'y':
        login()
    elif returning == 'n':
        registration()
    else:
        questions()


def registration():
    player = input('Please insert your name: ')
    pp = input('Please enter your password: ')
    ppverify = input('Please verify your password: ')
    ppassword = ''

    if pp == ppverify:
        ppassword = ppverify.encode()
        encoded = hashlib.shake_128(ppassword).hexdigest(64)
    else:
        print('Passwords do not match, please try again!')
        while pp != ppverify:
            pp = input('Please enter your password: ')
            ppverify = input('Please verify your password: ')

        ppassword = ppverify.encode()
        encoded = hashlib.shake_128(ppassword).hexdigest(64)

    mypassword_queue = []
    userTest = "select * from profiles where username = '%s';" % player

    if player and encoded != '':
        mycursor.execute(userTest)
        myresults = mycursor.fetchall()
        for row in myresults:
            for x in row:
                mypassword_queue.append(x)

    if player in mypassword_queue:
        print('Something went wrong or credentials already in use, try again!')
        mypassword_queue = []
        registration()

    userPassInsert = "insert into profiles(username, password, points, level) values('%s', '%s', 0, 0);" % (player,
                                                                                                            encoded)
    mycursor.execute(userPassInsert)
    db.commit()
    print('Registration Complete, please login!')
    login()


def login():
    player = input('Please insert your name: ')
    ppassword = input('Please insert your password: ')
    ppassword = ppassword.encode()
    encoded = hashlib.shake_128(ppassword).hexdigest(64)
    mypassword_queue = []
    userPassCheck = "select * from profiles where username = '%s' and password = '%s'" % (player, encoded)

    if player and ppassword != '':
        mycursor.execute(userPassCheck)
        myresults = mycursor.fetchall()
        for row in myresults:
            for x in row:
                mypassword_queue.append(x)
    else:
        print('Error Occured')

    if (player and encoded) in mypassword_queue:
        print('Successful Login, your player id is {}.'.format(mypassword_queue[0]))
        mainMenu(player, mypassword_queue)
    else:
        print('Unsuccessful Login, Try again.')
        login()


moneyExp = '100 tokens equals 1 dollar.'
gameWins = '''In the "Number Guessing Game" you will win 25 tokens in the 1 die game if you win. 
If you guess one die correctly in the 2 die game, you will win 35 tokens.
If you guess both die correctly in the 2 die game, you will win 70 tokens.'''


def mainMenu(player, mypassword_queue):
    print('')
    print('Hello {}, and welcome to the Casino!'.format(player))
    print('Which game would you like to play: ')
    print('')
    print('\t1: Number Guessing Game')
    print('\t4: Information')
    if mypassword_queue[4] == 2:
        print('\t5: Developer')
        print('\t6: Administrator')
        print('')
    elif mypassword_queue[4] == 1:
        print('\t5: Developer')
        print('')
    else:
        print('')
    selection = input("Please select the game number to play it: ")
    if selection == '1':
        guessGame(player)
    elif selection == '2':
        print("Sorry this game is not available yet, we will return you to the main menu.")
        mainMenu(player, mypassword_queue)
    elif selection == '3':
        print("Sorry this game is not available yet, we will return you to the main menu.")
        mainMenu(player, mypassword_queue)
    elif selection == '4':
        information()
    elif selection == '5':
        if mypassword_queue[4] >= 1:
            developer()
        else:
            print('You need to enter a number that is 1 through 4.')
            mainMenu(player, mypassword_queue)
    elif selection == '6':
        if mypassword_queue[4] == 2:
            administrator(player)
        elif mypassword_queue[4] >= 1:
            print('You need to enter a number that is 1 through 5.')
            mainMenu(player, mypassword_queue)
        else:
            print('You need to enter a number that is 1 through 4.')
            mainMenu(player, mypassword_queue)
    elif selection != '1' or '2' or '3' or '4' or '5' or '6':
        print('You need to enter a number that is 1 through 4.')
        mainMenu(player, mypassword_queue)


def developer():
    print('Welcome to the Development Panel.')
    pusername = ''
    ppassword = ''


def administrator(player):
    print('Welcome to the Administration Panel.')
    pid = ''
    pusername = ''
    ppassword = ''
    ppoints = ''
    plevel = ''
    userinfo = []
    print('You have multiple choices. Would you like to:')
    print('')
    print('\t1. Edit a User.')
    print('\t2. Add a User.')
    print('\t3. Remove a User.')
    print('')
    choice = ''
    while True:
        try:
            choice = int(input('What would you like to do: '))
        except ValueError:
            print('Please enter a valid #.')
            continue
        break

    if choice == 1:
        print('Editing a User.')
        pid = ''
        while True:
            try:
                pid = int(input('Please insert the users ID: '))
            except ValueError:
                print('Please enter a valid ID #.')
                continue
            break

        checkID = "select * from profiles where id = '%s'" % pid

        if pid != '':
            mycursor.execute(checkID)
            myresults = mycursor.fetchall()
            for row in myresults:
                for x in row:
                    userinfo.append(x)

        if userinfo[0] == pid:
            if userinfo[4] == 2:
                print('I am sorry you can not edit someone with the equivalent access as you.')
                administrator(player)
            else:
                toContinue = input('The user is {}, do you wish to continue to '
                                   'edit them: '.format(userinfo[1]))
                if toContinue == 'y' or toContinue == 'yes':
                    print('User information:\n\tID: {}\n\tUsername: {}\n\tPoints: {}\n\tLevel: {}'
                          .format(userinfo[0], userinfo[1], userinfo[3], userinfo[4]))
                    edit = ''
                    while True:
                        try:
                            edit = int(input(('Options: \n\t1. Everything\n\t2. Username\n\t3. Password\n\t4. Points\n'
                                              '\t5. Level\nWhat would you like to edit: ')))
                        except ValueError:
                            print('Please enter a valid #.')
                            continue
                        break

                    if edit == 1:
                        print()
                    elif edit == 2:
                        print()
                    elif edit == 3:
                        print()
                    elif edit == 4:
                        print()
                    elif edit == 5:
                        print()
                    else:
                        print()
                else:
                    administrator(player)
        else:
            print('No existing user with this ID, Try again.')
            administrator(player)

    elif choice == 2:
        print('Adding a User.')
    elif choice == 3:
        print('Removing a User.')
    else:
        print('Incorrect Option')
        administrator(player)


def information():
    print('')
    print('Welcome to the information panel.')
    print('What would you like to know?')
    print("""
    C: Credits
    H: How to Play the Games
    W: Winnings of Each Game""")
    print('')
    print('Type "Exit" to return to the main menu.')
    print('')
    selection = input("Please enter a choice: ")
    if selection == 'C':
        print("Credits: ")
        print('')
        print("--------------------------------")
        print('')
        print('Original Creator: DiMeglio')
        print('Assistant Creator: Parkhurst')
        print('')
        print("--------------------------------")
        information()
    elif selection == 'H':
        print('')
        print('To play, return to the main menu and select the game using the number alongside the name.')
        print('After picking which game to play, follow the instructions and attempt to gain money by winning.')
        information()
    elif selection == 'W':
        print('')
        print(moneyExp)
        print(gameWins)
        information()
    elif selection == 'Exit':
        mainMenu()
    elif selection != 'Exit' or 'C' or 'H' or 'W':
        print('You need to enter a C, H, W, or simply "Exit".')
        information()


def guessGame(player):
    time = 0
    print('')
    print('Hello {} and welcome to the Guessing Game'.format(player))
    dieNumber = ''
    while True:
        try:
            dieNumber = int(input('Pick a number of die you would like to use between 1 and 3: '))
        except ValueError:
            print('Please enter a valid #.')
            continue
        break
    print('')
    if dieNumber == 1:  # Eventually this should cost 10 Tokens.
        guess1 = ''
        while True:
            try:
                guess1 = int(input('Please select a number between 1 and 6: '))
            except ValueError:
                print('Please enter a valid #.')
                continue
            break
        die = random.randint(1, 6)
        print('You rolled a', die, 'on the die.')
        print('You had previously guessed the number {}.'.format(guess1))
        if guess1 == die:
            print('Congrats you got it. You have received 25 Tokens')
        else:
            print('You did not get the right number.')
        time += 1
        if time > 0:
            kplay = input('Would you like to keep playing? y/n: ')
            if kplay == 'y':
                guessGame(player)
            else:
                mainMenu(player)
    elif dieNumber == 2:  # Eventually this should cost 20 Tokens.
        print('Insert 2 numbers in between 1 and 6:')
        die = random.randint(1, 6)
        die2 = random.randint(1, 6)
        guess1 = ''
        guess2 = ''
        while True:
            try:
                guess1 = int(input('1st Guess: '))
            except ValueError:
                print('Please enter a valid #.')
                continue
            break
        while True:
            try:
                guess2 = int(input('2nd Guess: '))
            except ValueError:
                print('Please enter a valid #.')
                continue
            break
        if guess1 == die and guess2 != die2 or guess1 != die and guess2 == die2:
            print('You have guessed one of the numbers correctly. The first roll was: {} and the second roll was: {}.'
                  ' You have received 35 tokens'.format(die, die2))
        elif guess1 == die and guess2 == die2:
            print('You have guessed both correct numbers! You have received 70 tokens.')
        else:
            print('You have not guessed any of the numbers correctly.')
        time += 1
        if time > 0:
            kplay = input('Would you like to keep playing? y/n: ')
            if kplay == 'y':
                guessGame(player)
            else:
                mainMenu(player)
    elif dieNumber == 0:
        print('Insert 3 numbers in between 1 and 6:')
        die = random.randint(1, 6)
        die2 = random.randint(1, 6)
        die3 = random.randint(1, 6)
        int(input('1st Number: '))
        int(input('2nd Number: '))
        int(input('3rd Number: '))
    elif dieNumber > 3 or dieNumber < 1:
        print('You need to enter a number that is 1 through 3')
        guessGame(player)


questions()
