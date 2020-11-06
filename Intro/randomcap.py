import random

text = "script para que modifique aleatoriamente las mayúsculas de un texto y las convierta en minúsculas, link del github(sin el algoritmo):"

def capi_sentence(sentence):
    new_sentence = ""
    number = 0 #Dummy number for tracking

    for letter in sentence.lower():
        if len(new_sentence)<2: #Creates the first two letter
            random_number = random.randint(0,1) #This randomly decides if the letter should be upper or lowercase
            if random_number==0:
                new_sentence += letter.upper()
            else:
                new_sentence += letter
        else:
            if (new_sentence[number-2].isupper() and new_sentence[number-1].isupper() or new_sentence[number-2].islower() and new_sentence[number-1].islower())==True:
                #Checks if the two letters before are both upper or lowercase
                if new_sentence[number-1].isupper(): #Makes the next letter the opposite of the letter before
                    new_sentence += letter.lower()
                else:
                    new_sentence += letter.upper()
            else:
                random_number = random.randint(0,1)
                if random_number==0:
                    new_sentence += letter.upper()
                else:
                    new_sentence += letter
                
        number += 1 #Add one more to the tracking
     
    print(new_sentence)

capi_sentence(text)