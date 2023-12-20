import time
def print_slow(text, delay=0.00001):
    for char in text:
        print(char,end='',flush = True)
        time.sleep(delay)
    print() #make it 0.05 for the actual typing, testing is 0.01

def print_mid(text, delay=0.001):
    for char in text:
        print(char,end='',flush = True)
        time.sleep(delay)
    print()

def print_fast(text, delay=0.0000001):
    for char in text:
        print(char,end='',flush = True)
        time.sleep(delay)
    print()

def Validate_12_Input():
    one_two_input = "1"
    valid_input = False
    while valid_input == False:
        try:
            one_two_input = input("Enter your answer: ").lower()
            if one_two_input == "1" or one_two_input == "2":
                valid_input = True
        except ValueError():
            print("Try again, enter a number")
    return one_two_input #validates inputs for yes or no 


def Validate_123_Input():
    one_two_three_input = "1"
    valid_input = False
    while valid_input == False:
        try:
            one_two_three_input = input("Enter your answer: ").lower()
            if one_two_three_input == "1" or one_two_three_input == "2" or one_two_three_input == "3":
                valid_input = True
        except ValueError():
            print("Try again, enter a number")
    return one_two_three_input #validates inputs for yes or no 
def You_Died():
    print_mid("""
▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓ 
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░ 
 ░ ░         ░ ░     ░           ░     ░     ░  ░   ░    
 ░ ░                           ░                  ░      
        """)

def You_Won():
    print_mid("""
▓██   ██▓ ▒█████   █    ██     █     █░ ▒█████   ███▄    █ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓█░ █ ░█░▒██▒  ██▒ ██ ▀█   █ 
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒█░ █ ░█ ▒██░  ██▒▓██  ▀█ ██▒
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░█░ █ ░█ ▒██   ██░▓██▒  ▐▌██▒
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░░██▒██▓ ░ ████▓▒░▒██░   ▓██░
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░      ▒ ░ ░    ░ ▒ ▒░ ░ ░░   ░ ▒░
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░   ░  ░ ░ ░ ▒     ░   ░ ░ 
 ░ ░         ░ ░     ░            ░        ░ ░           ░ 
 ░ ░                                                           
        """)

def spectre_image():
    print_fast("""            ████████████████████████████████████████████████████████████████████████████▓▓░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒██████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████▓▓██▓▓▒▒░░░░▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒▓▓████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░▒▒▓▓██████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░▒▒▒▒▒▒████████████████████████████████████████████████████████████████████████
▓▓████████████████████████████████████████████████████████████████▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓██████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░▒▒▒▒▓▓████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓▓▓██████████████████████████████████████████████████████████████
██▓▓████████████████████████████████████████████████████████▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓██████████████████████████████████████████████████████████████
██▓▓██████████████████████████████████████████████████████▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████▓▓▒▒░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓██████████████████████████████████████████████████████████
████████████████████████████████████████████████████████▓▓▒▒░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓██████████████████████████████████████████████████████████
████████████████████████████████████████████████████████▓▓▒▒░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓████████████████████████████████████████████████████████
████████████████████████████████████████████████████████▓▓░░░░░░░░░░░░░░░░░░░░░░░░                          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██████████████████████████████████████████████████████████
████████████████████████████████████████████████████████▓▓░░░░░░░░░░░░░░░░░░░░░░░░                            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██████████████████████████████████████████████████████████
████████████████████████████████████████████████████████▓▓░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓████████████████████████████████████████████████████████
████████████████████████████████████████████████████████▓▓░░░░░░░░░░░░░░░░░░░░▓▓▓▓████░░                  ░░▒▒▒▒▒▒░░░░░░  ░░░░░░░░░░░░░░░░░░░░██████████████████████████████████████████████████████████
████████████████████████████████████████████████████████▓▓░░░░░░░░░░░░░░░░░░░░▓▓████████░░                ▒▒▓▓▓▓██▒▒░░░░░░░░    ░░░░░░░░░░░░░░██████████████████████████████████████████████████████████
████████████████████████████████████████████████████████▓▓░░░░░░░░░░░░░░  ░░░░██████████▒▒      ░░      ░░▓▓▓▓▓▓▓▓██▓▓░░░░░░░░  ░░░░░░░░░░░░░░▓▓████████████████████████████████████████████████████████
████████████████████████████████████████████████████████▓▓░░░░░░░░░░░░    ░░▒▒▓▓██████▒▒        ░░      ▒▒▓▓▓▓██▓▓▓▓██▓▓░░░░░░  ░░░░░░░░░░░░░░▓▓████████████████████████████████████████████████████████
████████▓▓██████████████████████████████████████████████▓▓░░░░░░░░░░░░░░░░░░░░▓▓▓▓▒▒░░                  ░░▓▓▓▓▓▓▓▓████▓▓      ░░░░░░░░░░  ░░░░▓▓████████████████████████████████████████████████████████
████████████████████████████████████████████████████████▓▓░░░░░░░░░░░░░░░░░░░░░░░░                        ░░▓▓▓▓██▓▓▒▒      ░░░░░░░░░░░░  ░░▒▒▓▓████████████████████████████████████████████████████████
████████████████████████████████████████████████████████▓▓░░░░░░░░░░                                                              ░░░░░░░░░░░░▓▓▓▓██████████████████████████████████████████████████▓▓██
████████████████████████████████████████████████████▓▓░░░░░░░░░░░░░░                                                            ░░░░░░░░░░░░░░░░▓▓████████████████████████████████████████████████▓▓████
████████████████████████████████████████████████████▓▓░░░░░░░░                                                                ░░░░░░░░  ░░░░░░░░▓▓██████████████████████████████████████████████████████
██████████████████████████████████████████▓▓▓▓████▓▓▓▓░░░░░░░░                                                                          ░░░░░░░░▓▓▓▓████████████████████████████████████████████████████
██████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░                                  ▒▒░░                                    ░░░░░░░░▓▓██████████████████████████████████████████████████████
████████████▓▓████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░                                ▒▒████▒▒                                ░░░░░░░░▒▒▓▓████▓▓▓▓▓▓████████████████████████████████████████████
████████████████████████████████████████████░░░░▓▓▓▓▓▓▓▓▒▒░░                              ░░▓▓████████░░░░                            ░░░░░░░░▓▓▓▓▓▓▓▓▒▒░░██▓▓████████████████████████████████▓▓████████
████████████████████████████████████████████░░▒▒▓▓▓▓▓▓▓▓▓▓░░░░░░░░                      ░░▒▒██████████▓▓░░░░                          ░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓░░▓▓████████████████████████████████████████████
██████████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░                    ░░▓▓██████████▓▓▒▒░░                            ░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████████████████████▓▓██████████
██████████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░              ░░▓▓▓▓████████████▓▓░░                          ░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓██████████████████████████████████████████████
██████████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░          ▒▒▒▒██████████████▓▓▒▒░░░░                      ░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓████▓▓██▓▓██████▓▓████████████████████████████
████████████████████████████████████████████████▒▒▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░          ░░▓▓████████████▓▓▓▓▒▒░░██▒▒                  ░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓██████████████████████▓▓████████████
████████████████████████▓▓▓▓████████████████████▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░        ▒▒▓▓██████████████▓▓▒▒░░  ▓▓                ░░░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓██████████████████████▓▓████████████████████████
████████████████████▓▓▓▓▓▓██████████▓▓██████████▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░  ░░▒▒████████████████▓▓▓▓░░                      ░░░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓████████▓▓████████████▓▓▓▓▒▒▓▓▓▓▓▓██████████████
████████████████▓▓▓▓▒▒▓▓▓▓▓▓████▓▓██▓▓▓▓▓▓██████▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░      ░░░░      ░░▒▒▓▓████████████████▒▒░░                      ░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓██████▓▓▓▓▓▓████████▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓████████████
██▓▓▒▒████▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▒▒▒▒░░░░░░░░░░░░                ░░▒▒▓▓████████████▓▓▓▓▓▓░░                        ░░░░░░░░▒▒▒▒▒▒▓▓▓▓████▓▓▓▓▓▓▓▓██████▓▓▒▒▒▒▒▒░░░░▒▒▒▒▓▓▓▓▒▒████▒▒▓▓
██▒▒▒▒██████▒▒▒▒██▒▒▒▒▓▓▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▒▒░░░░░░░░░░░░                ░░▓▓▓▓██████████████▓▓▒▒▒▒                    ░░░░░░░░░░░░░░▒▒▒▒▓▓████▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒░░▒▒▒▒▒▒░░░░░░░░░░▒▒██████▒▒▒▒
██▒▒▒▒████▓▓░░░░░░░░░░░░▒▒▓▓▓▓▓▓██▓▓██████▓▓██████▓▓▓▓░░░░░░░░░░░░░░░░              ▒▒▒▒▓▓██████████████▓▓░░░░▒▒              ░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓████▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒░░░░░░░░░░▓▓████▒▒░░
████▓▓██▓▓▒▒░░░░░░░░░░░░░░░░░░▓▓▓▓██▓▓▓▓▓▓██▓▓██▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░            ▒▒▓▓▓▓████████████▓▓▓▓░░░░░░              ░░▒▒░░░░░░░░░░░░░░▒▒▒▒▓▓████▓▓▓▓▓▓██▓▓████▓▓██████▓▓▓▓▒▒░░░░░░░░▓▓████▓▓██
████▒▒██▓▓▒▒░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓████▓▓██▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░          ▒▒▒▒▓▓▓▓██████████▓▓▓▓▒▒░░                ░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓██▓▓██▓▓▓▓██▓▓▒▒▒▒▓▓████▓▓▒▒░░░░░░░░░░▒▒████▒▒██
██████████░░░░░░░░▒▒▒▒░░▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▒▒░░░░░░░░░░░░░░░░            ▒▒▓▓▓▓▓▓██████████████▒▒░░                  ░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░▒▒▓▓░░░░░░░░░░░░░░▒▒▓▓██████
██████████░░░░░░░░░░▒▒░░▓▓▓▓▒▒▒▒▓▓██▓▓▒▒▒▒▒▒▓▓▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░██            ▒▒▓▓▓▓▓▓████████▓▓████▒▒░░                  ░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓██████
████████▓▓░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒░░░░░░░░░░░░░░░░░░▒▒            ▒▒▓▓▓▓▒▒▓▓████▓▓▓▓▒▒▓▓▒▒░░                      ░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓██████
██▓▓██▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒░░░░░░░░░░░░░░░░            ░░▒▒▓▓▓▓████▓▓████▓▓░░▓▓░░░░                        ░░░░░░░░░░░░░░▒▒▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▒▒██▓▓
████████▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▒▒▒▒░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░                ░░▒▒▒▒▒▒▓▓▓▓▓▓██▒▒▒▒▓▓▒▒░░                          ░░░░░░░░░░▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▒▒░░░░░░  ░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓
██████▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░▒▒▒▒░░░░░░                        ░░▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒░░░░░░                                    ░░▒▒░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██████
████████░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▒▒░░░░                              ▓▓░░░░░░▒▒▒▒▒▒▒▒░░░░░░                                    ░░░░▒▒░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██████
████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓░░░░░░░░░░░░░░                              ▓▓░░░░░░░░░░░░▒▒▒▒░░░░                                    ░░░░░░░░░░▒▒▒▒▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░██▓▓████
████████▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░                              ██░░░░░░░░░░░░░░░░░░░░                                    ░░░░░░░░░░░░░░▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██▒▒▓▓██
████▓▓▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░  ░░░░░░                            ░░    ░░░░░░░░░░░░░░                                      ░░░░  ░░░░░░░░▒▒▒▒░░░░░░░░░░  ░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓██
████▓▓░░▒▒░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░  ░░  ░░░░░░                            ░░        ░░                                              ░░░░  ░░  ░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██
████▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░        ░░░░░░                                                                                      ░░░░        ░░░░░░░░░░░░░░░░▓▓▓▓▒▒░░░░░░░░░░░░░░░░▒▒▓▓██
████▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    ░░  ░░░░                            ░░                        ░░░░                            ░░░░        ░░░░░░░░░░░░░░░░▓▓▒▒░░░░░░░░░░░░░░░░░░▒▒████""")

def skeleton_image():
    print_fast("""     .            )        )
                  (  (|              .
              )   )\/ ( ( (
      *  (   ((  /     ))\))  (  )    )
    (     \   )\(          |  ))( )  (|
    >)     ))/   |          )/  \((  ) \\
    (     (      .        -.     V )/   )(    (
     \   /     .   \            .       \))   ))
       )(      (  | |   )            .    (  /
      )(    ,'))     \ /          \( `.    )
      (\>  ,'/__      ))            __`.  /
     ( \   | /  ___   ( \/     ___   \ | ( (
      \.)  |/  /   \__      __/   \   \|  ))
     .  \. |>  \      | __ |      /   <|  /
          )/    \____/ :..: \____/     \ <
   )   \ (|__  .      / ;: \          __| )  (
  ((    )\)  ~--_     --  --      _--~    /  ))
   \    (    |  ||               ||  |   (  /
         \.  |  ||_             _||  |  /
           > :  |  ~V+-I_I_I-+V~  |  : (.
          (  \:  T\   _     _   /T  : ./
           \  :    T^T T-+-T T^T    ;<
            \..`_       -+-       _'  )
  )            . `--=.._____..=--'. ./         (
 ((     ) (          )             (     ) (   )> 
  > \/^/) )) (   ( /(.      ))     ))._/(__))./ (_.
 (  _../ ( \))    )   \ (  / \.  ./ ||  ..__:|  _. \\
 |  \__.  ) |   (/  /: :)) |   \/   |(  <.._  )|  ) )
))  _./   |  )  ))  __  <  | :(     :))   .//( :  : |
(: <     ):  --:   ^  \  )(   )\/:   /   /_/ ) :._) :
 \..)   (_..  ..  :    :  : .(   \..:..    ./__.  ./
            ^    ^      \^ ^           ^\/^     ^""")

def beast_image():
    print_mid("""
                                             ,--,  ,.-.
               ,                   \,       '-,-`,'-.' | ._
              /|           \    ,   |\         }  )/  / `-,',
              [ ,          |\  /|   | |        /  \|  |/`  ,`
              | |       ,.`  `,` `, | |  _,...(   (      .',
              \  \  __ ,-` `  ,  , `/ |,'      Y     (   /_L\\ 
               \  \_\,``,   ` , ,  /  |         )         _,/
                \  '  `  ,_ _`_,-,<._.<        /         /
                 ', `>.,`  `  `   ,., |_      |         /
                   \/`  `,   `   ,`  | /__,.-`    _,   `\\
               -,-..\  _  \  `  /  ,  / `._) _,-\`       \\
                \_,,.) /\    ` /  / ) (-,, ``    ,        |
               ,` )  | \_\       '-`  |  `(               \\
              /  /```(   , --, ,' \   |`<`    ,            |
             /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
       ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
      (-, \           ) \ ('_.-._)/ /,`    /
      | /  `          `/ \\ V   V, /`     /
   ,--\(        ,     <_/`\\     ||      /
  (   ,``-     \/|         \-A.A-`|     /
 ,>,_ )_,..(    )\          -,,_-`  _--`
(_ \|`   _,/_  /  \_            ,--`
 \( `   <.,../`     `-.._   _,-`""")
beast_attacked = False
dagger_acquired = False
cloak_acquired = False
figures_attack_run_cloak = 1
game_over = False
stone_acquired = False

print_mid("""Welcome to\n
▓█████▄ ▓█████ ▄▄▄     ▄▄▄█████▓ ██░ ██   ██████    ▓█████▄  ▒█████   ▒█████   ██▀███  
▒██▀ ██▌▓█   ▀▒████▄   ▓  ██▒ ▓▒▓██░ ██▒▒██    ▒    ▒██▀ ██▌▒██▒  ██▒▒██▒  ██▒▓██ ▒ ██▒
░██   █▌▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██▀▀██░░ ▓██▄      ░██   █▌▒██░  ██▒▒██░  ██▒▓██ ░▄█ ▒
░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ░▓█ ░██   ▒   ██▒   ░▓█▄   ▌▒██   ██░▒██   ██░▒██▀▀█▄  
░▒████▓ ░▒████▒▓█   ▓██▒ ▒██▒ ░ ░▓█▒░██▓▒██████▒▒   ░▒████▓ ░ ████▓▒░░ ████▓▒░░██▓ ▒██▒
 ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░    ▒ ░░▒░▒▒ ▒▓▒ ▒ ░    ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
 ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░   ░     ▒ ░▒░ ░░ ░▒  ░ ░    ░ ▒  ▒   ░ ▒ ▒░   ░ ▒ ▒░   ░▒ ░ ▒░
 ░ ░  ░    ░    ░   ▒    ░       ░  ░░ ░░  ░  ░      ░ ░  ░ ░ ░ ░ ▒  ░ ░ ░ ▒    ░░   ░ 
   ░       ░  ░     ░  ░         ░  ░  ░      ░        ░        ░ ░      ░ ░     ░     
 ░                                                   ░      """)
print_slow("You awake trapped in a cell, a far away light glimmers through the open cell door.\nAs you look around you, a broken sword catches your eye.")
print_mid("""
                           ___
                          ( ((
                           ) ))
  .::.                    / /(
 'M .-;-.-.-.-.-.-.-.-.-/| ((:::::::::::::::::::::::::::::::::\\
(J ( ( ( ( ( ( ( ( ( ( ( |  ))   -=============================\\
 `P `-;-`-`-`-`-`-`-`-`-\| ((:::::::::::::::::::::::::::::::::::/
  `::'                    \ \(
                           ) ))
                          (_(()""")
print_slow("Do you pick it up?\n1. Pick up the sword\n2. Ignore the sword")
one_two_input = Validate_12_Input() #calls the yes or no input and uses that as the variable

if one_two_input == "1": #if they answered 1, they now have the sword
    sword_acquired = True
    print_slow("You hastily grab the sword, your nerves are slightly calmed but the gnawing dread does not disipate.\nAs you approach the open cell door the sole torch illuminates a narrow derelict hallway.\nIt seems like it is the only option, and so you advance onwards.\n")
elif one_two_input == "2": #if they answered 2, they don't have the sword
    sword_acquired = False
    print_slow("You ignore the broken sword and slowly inch toward the open cell door.\nThe sole torch illuminates a narrow derelict hallway.\nIt seems like it is the only option, and so you advance onwards.\n")

print_slow("You hear an almost hypnotic cackling within the hallway, its melodic voice is captivating and fills your mind with ideas of love and adoration.\nYou quickly plug your ears and attempt to resist its call. As it fades from your mind, you can barely make out a set of glowing eyes.\nIt seems there's no way to sneak past the creature without it spotting you.\nWill you attack the creature, or attempt to speak with it?\n1. Attack the creature\n2. Call out to the beast")
a_s_input = Validate_12_Input()
if a_s_input == "1" and sword_acquired == True: #if picked attack, and the sword is acquired, they'll have a different outcome
        print_slow("You rush forward in a mad frenzy, slicing at the monster with unbridled rage.\n")
        beast_image()
        print_slow("As your sword lands a solid strike, the creature howls in pain.\nWhen you attempt to continue your assault, the beast lunges forward, knocking you down.\nNow, as you lie on the uncaring stone, you see the true form of the malformed creature.\nIts body is covered in a thick set of fur, matted and bloodied.\nThe creature has clearly been down here a while, surviving on any unlucky adventurers found exploring this ancient ruin.\nOn its back is a small rucksack, near overflowing with various items and trinkets.\nBefore your eyes can take in any more features of the abnormality, it readies a strike, clearly aiming to end your helpless life.\nFrom seeming divine intervention, the beast howls in pain and rather sluggishly strikes the ground, barely missing your body.\nIn your foes' moment of weakness, you quickly run off, further down the corridor.")
        beast_attacked = True
        #player is further down the corridor
        print_slow("\nYou slowly continue down the hallway.\nIt seems that the tunnel stretches ever onward, plain and unchanging.\nYou suddenly reach a hallway with three branching paths.\nOne is overgrown with lush green vines and moss, its bricks are cracked and in complete disrepair.\nThe second is near identical to the unchanging walls of the hallway, nothing special marks its walls or floor.\nThe third and final door is one marked by a roaring bonfire, its glow illuminates the entire hallway.\nWithin the hallway, you can just make out 3 figures, all standing and staring at you ominously.\nWhich path will you choose?\n1. The derelict doorway\n2. The unchanging doorway\n3. The burning doorway")
        corridor_choice = Validate_123_Input() 
        if corridor_choice == "1":
            print_slow("You ready yourself as you choose the seemingly forgotten hallway.\nAs you take your first hesitant steps, the walls shift and contort into images, memories you had once known.\nThe once familiar recollections are blurred and marked with a sense of violence that fills you with a nauseating dread.\nSuddenly, two figures morph from the still images, their bodies twist and contort in this plane.")
            spectre_image() #prints big image
            print_slow("\nThey begin to rush at you and you must act quickly.\n1. Attack the spectres\n2. Run")
            figures_attack_run = Validate_12_Input()     
            if figures_attack_run == "1" and sword_acquired == True or sword_acquired == False: #if the person has either no sword or the broken sword, this plays
                print_slow("You rush hoping to swiftly taking out the spectres.\nYour flurry of strikes simply float through the ghosts, doing no damage.\nIn a grim embrace the spectres engulf you, your mind seems to gain clarity and you awke somewhere else.\nMomentarily you find yourself within a burning house, its smoke begins to fill your lungs and before you know it, you fall into a deep sleep.")
                You_Died()
            elif figures_attack_run == "2":
                print_slow("As you attempt to run, the spectres open their mouths and the unmistakable crackling of flame escapes their gaping maws.\nAs soon as the noise escapes their mouth, their bodies disipate and reappear in front of you.\nAs you attempt to run past them, one of the ghosts embraces in.\nAs its tendrils draw you in, your mind gains clarity and you awake somewhere else.\nAs you awake, you see a vision of a man lighting a small cabin alight.\nHe does not shy away from the flames and instead runs straight into the house.\nYour vision fades and you fall into a deep sleep.")
                You_Died()
        elif corridor_choice == "2":
            print_slow("\nYou continue down the unchanging hallway, preparing yourself for whatever may happen.\nYet as you continue down the unending hallway, nothing changes.\nThe walls remain the same and no monsters block your path.\nYou do not know how much time passes, but eventually your legs give out and you collapse.\nAs you lay there, you fall into a deep sleep.")
            You_Died()
        elif corridor_choice == "3":
                print_slow("You step through the flames ahead of you, the figures all turn towards you in somber unison.\nTheir faces are bare of any flesh, marked with the unmistakable presence of flames.")
                skeleton_image()
                print_slow("\n\nAs you turn around, the flames that guarded the entrance have now grown into a roaring blaze.\nThere is no escape.\nThey began a slow approach towards you, what will you do?\n1. Rush forward and attack them\n2. Run into the flames")
                skeleton_choice = Validate_12_Input()
                if skeleton_choice == "1" and dagger_acquired == False:
                    print("You rush forward, swiping at the skeletons with all your might.\nDespite the strenuous effort, they seem near impervious to your attacks.\nShurgging off your attacks, they surround you and force you backwards.\nCloser and closer you near the restless flames, until eventually you stand right before them.\nYou feel the inescapable heat and before you know it, you stand within them.\nYour body begins to burn but your consciousness fades.")
                    You_Died()
                    game_over = True

                elif skeleton_choice == "1" and dagger_acquired == True:
                    print("You rush forward, swinging at the skeletons with all your might.\nYour blade clatters against their charred remains, one at a time, they crumble to the ground.\nYou continue onwards, the path begins to be consumed in a pure white flame.\nSeeing no other path forward, you step into the flames.\n\nYou awake outside the burnt remains of a cabin, you feel a sense of intense guilt and sorrow.")
                    You_Won()
                    game_over = True

elif a_s_input == "1" and sword_acquired == False:
        print_slow("You rush forward in a mad frenzy, attempting to take the creature by surprise.\nYou jump on the creature's back, trying to wrestle it down.\nYet its overwhelming bulk proves an insurmountable challenge to overcome.\nThe beast pulls you off its back and slams you to the ground, mortally wounding you.\nNow, as you lie on the uncaring stone, you see the true form of the malformed creature through bloodshot eyes.\nIts body is covered in a thick set of fur, matted and bloodied.\nThe creature has clearly been down here a while, surviving on any unlucky adventurers found exploring this ancient ruin.\nOn its back is a small rucksack, near overflowing with various items and trinkets.\nBefore your eyes can take in any more features of the abnormality, it strikes your body with a final blow.\nThe attack instantly severes your connection to this plane, ending your life.")
        You_Died() #subroutine to display you died screen 
elif a_s_input == "2":
        beast_image()
        print_slow("You call out to the mysterious entity, it instantly snaps its head to face you.\nIn a terrifying display of speed, it runs over to you, its head unmoving.\nIts terrifying appearance is a far cry from the melodic voice you heard just moments ago.\nDespite being such an odd creature, the thing seems relatively friendly.\nIn an intelligent display of communication, it gestures towards a rucksack located on its back.\nIt seems it wants you to look inside, you see no way of dismissing his request and so you oblige.\n")
        print_slow("There are multiple items laid out before your eyes:\nOne is a small dagger, incredibly sharp to the touch.")
        print_mid("""       
       .---. 
       |---|
       |---|
       |---|
   .---^ - ^---.
   :___________:
      |  |//|
      |  |//|
      |  |//|
      |  |//|
      |  |//|
      |  |//|
      |  |.-|
      |.-'**|
       \***/
        \*/
         V
            """)
        print_slow("\nA mysterious cloak vaguely shimmers within your vision.")
        print_mid("""
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
              ⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣶⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣦⡈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣷⣤⣈⠙⠛⠛⠛⠉⣉⣠⣴⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀
⠀⠀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢃⣾⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⡇⠀
⠀⠀⠘⢿⣿⣿⣿⠿⠿⠛⠋⣁⣴⣿⣿⣿⣿⣿⣿⣿⡿⢋⣾⣿⣿⣿⣿⣿⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⢾⣿⣿⣿⣿⣿⠏⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠙⣿⣿⣿⠏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡿⠃⠀⠀⠀⠀⠀
            """)
        print_slow("\nFinally, the beast offers you a small triknket, a small rock with no apparent use.")
        print_mid("""
        ██        
      ██░░██      
    ██░░░░  ██    
  ██░░░░▓▓    ██  
██░░░░▓▓░░      ██
██▓▓▓▓░░░░░░▓▓▓▓██
██▓▓▓▓░░░░░░▓▓▓▓██
██▓▓▓▓░░░░░░▓▓▓▓██
██▓▓▓▓░░░░▒▒▓▓▓▓██
██▓▓▓▓░░░░░░▓▓▓▓██
██▓▓▓▓░░░░░░▓▓▓▓██
██▓▓▓▓░░░░░░▓▓▓▓██
██░░░░▓▓░░▓▓▓▓▓▓██
  ██░░░░▓▓▓▓▓▓██  
    ██░░░░▓▓██    
      ██░░██      
        ██         

            """)
        print_slow("\nWhich will you choose?\n1.The dagger\n2.The cloak\n3.The trinket.")
        item_choice_one_input = Validate_123_Input()
        if item_choice_one_input == "1":
            print_slow("You drop your broken sword and pick up the dagger, it fits firmly in the palm of your hand.\nThe tense air seems to disappear, you ready yourself for whatever is ahead.\n")
            dagger_acquired = True
            sword_acquired = False
        elif item_choice_one_input == "2":
            print_slow("You pick up the cloak and wrap it around yourself.\nThe creature grunts in surprise, as you look at your enveloped arm, it is seemingly completely transparent.\nHappy with your choice, you ready yourself for whatever comes next.\n")
            cloak_acquired = True
            print_slow("You slowly continue down the hallway.\nIt seems that the tunnel stretches ever onward, plain and unchanging.\nYou suddenly reach a hallway with three branching paths.\nOne is overgrown with lush green vines and moss, its bricks are cracked and in complete disrepair.\nThe second is near identical to the unchanging walls of the hallway, nothing special marks its walls or floor.\nThe third and final door is one marked by a roaring bonfire, its glow illuminates the entire hallway.\nWithin the hallway, you can just make out 3 figures, all standing and staring at you ominously.\nWhich path will you choose?\n1. The derelict doorway\n2. The unchanging doorway\n3. The burning doorway")
            corridor_choice = Validate_123_Input()
            if corridor_choice == "1" and cloak_acquired == True:
                print_slow("You ready yourself as you choose the seemingly forgotten hallway.\nAs you take your first hesitant steps, the walls shift and contort into images, memories you had once known.\nThe once familiar recollections are blurred and marked with a sense of violence that fills you with a nauseating dread.\nSuddenly, two figures morph from the still images, their bodies twist and contort in this plane.")
                spectre_image()

            print_slow("\nThey begin to rush you and you must act quickly.\n1. Attack the spectres\n2. Run\n3. Put on your cloak")
            figures_attack_run_cloak = Validate_123_Input()     
            if figures_attack_run_cloak == "1" and sword_acquired == True or sword_acquired == False: #if the person has either no sword or the broken sword, this plays
                print_slow("You rush hoping to swiftly taking out the spectres.\nYour flurry of strikes simply float through the ghosts, doing no damage.\nIn a grim embrace the spectres engulf you, your mind seems to gain clarity and you awke somewhere else.\nMomentarily you find yourself within a burning house, its smoke begins to fill your lungs and before you know it, you fall into a deep sleep.")
                You_Died()
                game_over = True
            elif figures_attack_run_cloak == "2":
                print_slow("As you attempt to run, the spectres open their mouths and the unmistakable crackling of flame.\nAs soon as the noise escapes their mouth, their bodies disipate and reappear in front of you.\nAs you attempt to run past them, one of the ghosts embraces in.\nAs its tendrils draw you in, your mind gains clarity and you awake somewhere else.\nAs you awake, you see a vision of a man lighting a small cabin alight.\nHe does not shy away from the flames and instead runs straight into the house.\nYour vision fades and you fall into a deep sleep.")
                You_Died()
                game_over = True
            elif figures_attack_run_cloak == "3" and cloak_acquired == True:
                print_slow("You drape yourself in your cloak, your body is enveloped in a transparent fog.\nConfounded and confused, the spectres stumble around, looking for your presence.\nEventually giving up, they morph back into the walls and you walk past, further down the corridor.\nAs you continue down the walkway, the stone becomes more and more damaged with it eventually coming to an end altogether.\nThe walls now gone, a wall of infinite shadow awaits you.\nSeeing no other option, you step forward, into the abyss.\nYou awaken in a small cabin, secluded and alone but together with your familly.")
                You_Won()
                game_over = True
        elif item_choice_one_input == "3":
            print_slow("As you prepare your body to pick up the stone, your mind is filled with countless ideas of what may happen.\nYour fingers grasp the trinket in intense anticipation.\nThey finally collide and your expectations are crushed when the mundane object does not grant you limitless power.\nSeverely disappointed, you place the stone in your pocket.\n")
            stone_acquired = True
        if game_over == False:
            print_slow("You slowly continue down the hallway.\nIt seems that the tunnel stretches ever onward, plain and unchanging.\nYou suddenly reach a hallway with three branching paths.\nOne is overgrown with lush green vines and moss, its bricks are cracked and in complete disrepair.\nThe second is near identical to the unchanging walls of the hallway, nothing special marks its walls or floor.\nThe third and final door is one marked by a roaring bonfire, its glow illuminates the entire hallway.\nWithin the hallway, you can just make out 3 figures, all standing and staring at you ominously.\nWhich path will you choose?\n1. The derelict doorway\n2. The unchanging doorway\n3. The burning doorway")
            corridor_choice = Validate_123_Input()
            if corridor_choice == "1":
                    print_slow("You ready yourself as you choose the seemingly forgotten hallway.\nAs you take your first hesitant steps, the walls shift and contort into images, memories you had once known.\nThe once familiar recollections are blurred and marked with a sense of violence that fills you with a nauseating dread.\nSuddenly, two figures morph from the still images, their bodies twist and contort in this plane.")
                    spectre_image()
                    print_slow("\nThey begin to rush you and you must act quickly.\n1. Attack the spectres\n2. Run")
                    figures_attack_run = Validate_12_Input()     
                    if figures_attack_run == "1" and sword_acquired == True or sword_acquired == False: #if the person has either no sword or the broken sword, this plays
                        print_slow("You rush hoping to swiftly taking out the spectres.\nYour flurry of strikes simply float through the ghosts, doing no damage.\nIn a grim embrace the spectres engulf you, your mind seems to gain clarity and you awke somewhere else.\nMomentarily you find yourself within a burning house, its smoke begins to fill your lungs and before you know it, you fall into a deep sleep.")
                        You_Died()
                        game_over = True
                    elif figures_attack_run == "2":
                        print_slow("As you attempt to run, the spectres open their mouths and the unmistakable crackling of flame escapes their gaping maws.\nAs soon as the noise escapes their mouth, their bodies disipate and reappear in front of you.\nAs you attempt to run past them, one of the ghosts embraces in.\nAs its tendrils draw you in, your mind gains clarity and you awake somewhere else.\nAs you awake, you see a vision of a man lighting a small cabin alight.\nHe does not shy away from the flames and instead runs straight into the house.\nYour vision fades and you fall into a deep sleep.")
                        You_Died()
                        game_over = True
            elif corridor_choice == "2" and stone_acquired == False:
                print_slow("You continue down the unchanging hallway, preparing yourself for whatever may happen.\nYet as you continue down the unending hallway, nothing changes.\nThe walls remain the same and no monsters block your path.\nYou do not know how much time passes, but eventually your legs give out and you collapse.\nAs you lay there, you fall into a deep sleep.")
                You_Died()
                game_over = True
            elif corridor_choice == "3":
                print_slow("You step through the flames ahead of you, the figures all turn towards you in somber unison.\nTheir faces are bare of any flesh, marked with the unmistakable presence of flames.")
                skeleton_image()
                print_slow("\n\nAs you turn around, the flames that guarded the entrance have now grown into a roaring blaze.\nThere is no escape.\nThey began a slow approach towards you, what will you do?\n1. Rush forward and attack them\n2. Run into the flames")
                skeleton_choice = Validate_12_Input()
                if skeleton_choice == "1" and dagger_acquired == False:
                    print("You rush forward, swiping at the skeletons with all your might.\nDespite the strenuous effort, they seem near impervious to your attacks.\nShurgging off your attacks, they surround you and force you backwards.\nCloser and closer you near the restless flames, until eventually you stand right before them.\nYou feel the inescapable heat and before you know it, you stand within them.\nYour body begins to burn but your consciousness fades.")
                    You_Died()
                    game_over = True

                elif skeleton_choice == "1" and dagger_acquired == True:
                    print("\nYou rush forward, swinging at the skeletons with all your might.\nYour blade clatters against their charred remains, one at a time, they crumble to the ground.\nYou continue onwards, the path begins to be consumed in a pure white flame.\nSeeing no other path forward, you step into the flames.\n\nYou awake outside the burnt remains of a cabin, you feel a sense of intense guilt and sorrow.")
                    You_Won()
                    game_over = True
