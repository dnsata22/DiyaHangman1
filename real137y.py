import random
randomWords = ["ducks" , "jumbo" ,"lucky" , "pills" , "flour"]
secret = random.choice (randomWords)
letter = ""
updateWord = []
#print (secret) #only for tester
def initialize(): 
    print "We have a secret word"
    print "_ _ _ _ _"
def getLetter():
    print ("enter a letter:")
    global letter
    letter = raw_input()
def ifWon():
    if secret == updateWord: 
        print "you win"
    else:
        getLetter()
def main():
    initialize ()
    getLetter()
    ifWon()
main()

#this is the tester function
''' 
def tester():
    global updateWord
    updateWord = raw_input()
    if updateWord ==  secret:
        print "yay"
    else:
        print "no"  
'''

def test(): 
    global letter
    letter=int(input("What is letter:"))
    if letter in secret:
        pos=secret.find(letter)
        updateWord[pos]=letter
        print updateWord.join()
        ifWon()   
    else:
        getLetter()