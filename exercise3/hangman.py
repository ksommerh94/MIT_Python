# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

#listo!
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    flag = len(secret_word)
    for lg in letters_guessed:
        if lg in secret_word:
            flag=flag-secret_word.count(lg)
    if flag==0:
        return True
    else:
        return False



    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass

#listo!
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    letterGuessed=['_ ']*len(secret_word)
    #print (" ".join(letterGuessed))
    for lg in letters_guessed:
        for i in range (len(secret_word)):
            if lg ==secret_word[i]:
                letterGuessed[i]=lg
    sLetterGuessed=" ".join(letterGuessed)
    return (sLetterGuessed)
    pass

#listo!
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    abcMissing=[]
    abc=string.ascii_lowercase
    for i in abc:
        if i not in letters_guessed:
            abcMissing.append(i)

    sabcMissing=" ".join(abcMissing)
    return (sabcMissing)
    pass

def unique_letters(secret_word):
    unique = []
    for char in secret_word:
        if char not in unique:
            unique.append(char)
    return(len(unique))

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed=[]
    all_vowels='aeiou'
    guesses=6
    warnings=3
    print('Loading word list from file...')
    #secret_word = choose_word(wordlist)
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is '+str(len(secret_word)) + ' letters long.')
    print('You have '+str(warnings) + ' warnings left.')
    print('-------------')
    while (not is_word_guessed(secret_word, letters_guessed)):
        #cantidad de vidas
        if guesses==0:
            print('Sorry, you ran out of guesses. The word was :',secret_word)
            return False
        #Verificacion de warnings
        print('You have',str(guesses),'guesses left.')
        print ('Available letters: ',(get_available_letters(letters_guessed)))
        #Ingresa la letra que adivina
        inputLetter=input("Please guess a letter: ")


        #verificar que la letra no se haya adiviando antes
        if inputLetter.lower()  not in letters_guessed:
            #verificar que la letra sea valida
            letters_guessed.append(inputLetter.lower())
            if (inputLetter.isalpha() and len(inputLetter)==1 ):
                #verificar que la letra este en la palabra
                if inputLetter.lower() not in secret_word:
                    if inputLetter.lower() not in all_vowels:
                        guesses-=1
                    else:
                        guesses-=2
                    print ('Oops! That letter is not in my word:',get_guessed_word(secret_word, letters_guessed))

                else:
                    print ('Good guess:',get_guessed_word(secret_word, letters_guessed))
            else:
                warnings-=1
                print('Oops! That is not a valid letter. You have', str(warnings), 'warnings left:', get_guessed_word(secret_word, letters_guessed))
        else:
            warnings-=1
            if warnings<0:
                print ('Oops! You have already guessed that letter. You have no warnings left so you lose one guess:',get_guessed_word(secret_word, letters_guessed) )
            else:
                print ('Oops! You have already guessed that letter. You have', str(warnings), 'warnings left:')
                print(get_guessed_word(secret_word, letters_guessed))

        if warnings<0 :
            guesses-=1
            warnings=3

        print('-------------')
    total_score=guesses*int(unique_letters(secret_word.lower()))
    print('Congratulations, you won!')
    print('Your total score for this game is: ', str(total_score))
    return True



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    check=[]
    check_flag=[]
    my_word=my_word.replace(" ", "")
    if len(my_word)==len(other_word):
        for i in range (len(secret_word)):
            if other_word[i] not in check:
                check.append(other_word[i])
                if my_word[i]==other_word[i]:
                    check_flag.append(1)
                elif my_word[i]=='_':
                    check_flag.append(0)
                else:
                    return False
            elif check_flag[check.index(other_word[i])]==0 and my_word[i]!='_':
                return False
            elif check_flag[check.index(other_word[i])]==1:
                return False
        return True

    else:
        return False




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    my_word=my_word.replace(" ", "")
    possible_list=[]
    for wl in wordlist:
        if len(wl)==len(my_word):
            possible_list_check=[]
            for i in range (len(my_word)):
                if my_word[i] == wl[i]:
                    possible_list_check.append(1)
                elif my_word[i]=='_' :
                    possible_list_check.append(1)
            if len(possible_list_check)==len(my_word):
                if(match_with_gaps(my_word, wl)):
                    possible_list.append(wl)

    return possible_list





def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed=[]
    all_vowels='aeiou'
    guesses=6
    warnings=3
    my_word='_ '*len(secret_word)
    print('Loading word list from file...')
    #secret_word = choose_word(wordlist)
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is '+str(len(secret_word)) + ' letters long.')
    print('You have '+str(warnings) + ' warnings left.')
    print('-------------')
    while (not is_word_guessed(secret_word, letters_guessed)):
        #cantidad de vidas
        if guesses==0:
            print('Sorry, you ran out of guesses. The word was :',secret_word)
            return False
        #Verificacion de warnings
        print('You have',str(guesses),'guesses left.')
        print ('Available letters: ',(get_available_letters(letters_guessed)))
        #Ingresa la letra que adivina
        inputLetter=input("Please guess a letter: ")


        #verificar que la letra no se haya adiviando antes
        if inputLetter=='*' and len(my_word)>0:
            print ('Possible word matches are:')
            print(show_possible_matches(my_word))
        elif inputLetter.lower()  not in letters_guessed and inputLetter!='*':
            #verificar que la letra sea valida
            letters_guessed.append(inputLetter.lower())
            if (inputLetter.isalpha() and len(inputLetter)==1  ):
                #verificar que la letra este en la palabra
                if inputLetter.lower() not in secret_word:
                    if inputLetter.lower() not in all_vowels:
                        guesses-=1
                    else:
                        guesses-=2
                    print ('Oops! That letter is not in my word:',get_guessed_word(secret_word, letters_guessed))

                else:
                    my_word=get_guessed_word(secret_word, letters_guessed)
                    print ('Good guess:',get_guessed_word(secret_word, letters_guessed))
            else:
                warnings-=1
                print('Oops! That is not a valid letter. You have', str(warnings), 'warnings left:', get_guessed_word(secret_word, letters_guessed))


        else:
            warnings-=1
            if warnings<0:
                print ('Oops! You have already guessed that letter. You have no warnings left so you lose one guess:',get_guessed_word(secret_word, letters_guessed) )
            else:
                print ('Oops! You have already guessed that letter. You have', str(warnings), 'warnings left:')
                print(get_guessed_word(secret_word, letters_guessed))

        if warnings<0 :
            guesses-=1
            warnings=3

        print('-------------')
    total_score=guesses*int(unique_letters(secret_word.lower()))
    print('Congratulations, you won!')
    print('Your total score for this game is: ', str(total_score))
    return True



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

    #print(match_with_gaps(a,secret_word))


    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    #print(show_possible_matches(a))




###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.


    #hangman_with_hints(secret_word)

        #print(is_word_guessed(secret_word, letters_guessed) )
