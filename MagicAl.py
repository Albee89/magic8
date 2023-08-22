import random
import app

def Replay() -> object:
    print("Do you have another question, beloved?[y/n]")
    reply = input()
    if reply == 'y':
        Magic8Ball()
    elif reply == 'n':
        print('Toodle-Loo Lovely!')
        exit()
    else:
        print("Sorry, love. Spin it to win it")
        Replay()
def Magic8Ball():
    print("Ask away then hit enter!")
    input()
    print(answers[random.randint(0, len(answers) - 1)])
    print("I hope this has helped guide you today *")
    Replay()


answers = ("Sorry, boo... not sure", "I'm gonna take my horse down New Orleans...it\'s a yay",
             "You better you better you bet- 100 per cent, OK?", "Only you can decide this now, your way",
             'It\'s a no from me, for now, my bae', 'It is decidedly so, and so yes, they say', 'You already know from where you lay', "Try again, babes, whatcha wanna say?")
print("Hello, I am a loving Magic8 'ball' coded by a good witch! See what your future holds with a quick spin")

print("*")
print("|")
print("To start with- what is your name, blessed? Type and hit 'enter'")
Name = input()
print("Hi, " + Name +  "!\nWelcome.")
print("It's time to have a spin, but before we begin...please ensure you make your questions "
      "positive and affirmative, it\'s all a win! "
      "\nA no right now does not mean a no forever, so don\'t ask the same question so close together...")
print("Press the star '*' and 'enter' to begin")
Star = input()
print('  __  __          _____ _____ _____    ___  ')
print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
print(' | \  / |  /  \ | |  __  | || |      | (_) |')
print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')

Magic8Ball()
Replay()
