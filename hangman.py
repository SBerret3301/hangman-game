#algorithme jeux
#fonction motvalide(mot:tableau caractere) : booleen
#      variable
#          a , b , i : entier
#          c : booleen
#      debut 
#                a <- 0
#                b <- 0
#                pour i <- 0 a longueur(mot) - 1 pas 1 faire
#                         si ascii(mot(i)) >= 65 et ascii(mot(i)) <= 90 alors
#                                 a <- a + 1
#                         sinon
#                                 b <- b + 1
#                         finsi
#                finpour
#                si longueur(mot) >= 4 et longueur(mot) <= 25 alors
#                       c <- vrai
#                 sinon
#                       c <- faux
#                finsi
#                si (a = longueur(mot) et b = 0) et c = vrai alors
#                           retourne vrai
#                sinon
#                           retourne faux
#                finsi
#      fin
#fonction find(mot : tableau caractere, m : caractere) : booleen
#       variable
#              a , i : entier
#       debut
#                  a <- 0 
#                  pour i <- 0 a longueur(mot) - 1 pas 1 faire
#                          si m = mot(i) alors 
#                                a <- a + 1
#                          finsi
#                  finpour
#                  si a = 0 alors
#                        retourne faux
#                  sinon 
#                        retourne vrai
#                  finsi            
#       fin
#variable 
#         tableau mot() : caractere
#         tableau Tcar() : caractere
#         l , i  : entier
#         m : chaine de caractere
#         a : caractere
#debut
#    ecrire("tapez un mot :")
#    lire(m)
#    redim(mot(longueur(m)))
#    pour i <- 0 a longueur(m)-1 pas 1 faire
#            mot(i) <- m(i)
#    finpour
#    tantque motvalide(mot) = faux faire
#            ecrire("tapez le mot en majuscules et le nombre des lettres entre 4 et 25 : ")
#            lire(mot)
#    fintantque
#    redim(Tcar(longueur(m)))
#    pour i <- 0 a longueur(m)-1 pas 1 faire
#            Tcar(i) <- "*"
#    finpour
#    l = 0 
#    repeter 
#            ecrire("tapez un caractere : ")
#            lire(a)
#            si find(mot , a) = faux alors 
#                  l <- l + 1
#            sinon 
#                  pour i <- 0 a longueur(m) - 1 pas 1 faire
#                          tantque a en Tcar(i) faire
#                                  ecrire("c'est caracter est existe, tapez autre caracter :")
#                          fintantque
#                  pour i <- 0 a longueur(m) - 1 pas 1 faire
#                         si a = mot(i) alors
#                              Tcar(i) <- a
#                              l <- l + 1
#                         finsi
#                  finpour
#                  ecrire(Tcar)
#            finsi
#    jusqua  l = 5 ou l = longueur(mot)
#    si l = 5 alors 
#            ecrire("Désolé, tu perds")
#     sinon 
#             ecrire("Félicitations, tu gagnes")
#    finsi
#fin
        























# Define a function to check the length of a word
def lengh(mot):
    if len(mot) >= 4 and len(mot) <= 25:
        return True

# Define a function to find occurrences of a letter in a word
def find(mot, m):
    a = 0
    for i in range(len(mot)):
        if mot[i] == m:
            a += 1
    return a

# Prompt the user to enter a word and convert it to uppercase
word = input("Enter a word: ").upper()

# Validate the length of the entered word
while lengh(word) != True:
    word = input("Enter a word with a number of letters between 4 and 25: ").upper()

# Initialize a list to represent the word with asterisks
Tcar = []

# Populate the list with asterisks, one for each letter in the word
for i in range(len(word)):
    Tcar.append("*")

# Initialize counters for incorrect and correct guesses
l = 0
n = 0

# Main game loop
while True:
    # Prompt the user to enter a letter and convert it to uppercase
    letter = input("Enter a letter: ").upper()

    # Check if the letter is not in the word
    if find(word, letter) == 0:
        l += 1  # Increment incorrect guess counter
    else:
        for i in range(len(word)) :
            while letter in Tcar :
                letter = input("this letter is already entred, enter another one: ").upper()
        # If the letter is in the word, replace asterisks with the guessed letter
        for i in range(len(word)):
            if word[i] == letter:
                n += 1  # Increment correct guess counter
                Tcar[i] = letter
        print(" ".join(Tcar))  # Print current state of the word

    # Check if the game should end (5 incorrect guesses or all letters guessed)
    if l == 5 or n == len(word):
        break

# Display the outcome of the game
if l == 5:
    print("Sorry, you lose!")
if n == len(word):
    print("Congratulations, you win!")
