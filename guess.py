import random




words = [ 'jokers' , 'king' , 'right' , 'eleven' , 'foggy' , 'daydream' ,]



while True:
        print("want to play ?? y or n")
        i = str(input())
        if i == 'n' :
           break
        else :
                while True :
                    print ( " choose difficulty : 1 for easy , 2 for medium , and 3 for hard ")
                    dif = input("\nEnter: ")
        
                    if dif == '1' : 
                        lives = 10
                        break
                    elif dif == '2' : 
                        lives = 7
                        break
                    elif dif == '3' : 
                        lives = 3
                        break
                    else :
                        print("enter properly")
        
                heart = u'\u2764'+" "
                word = random.choice(words)
                clue = list("?"*len(word))
                word = list(word)
                length = str(len(word)) 
                print("\n\n\n\nGuess the "+length+" letter word :\n\n")
                
                while True:
                
                    print("-"*80+"\n\n")
                    
                    print(clue)
                    
                    print ("\n\nLIVES LEFT - "+str(heart*lives)+"\n")
                    
                    inp = str(input("\n\nEnter your guess :"))
                    for i in range(len(word)) :
                        for j in range(0 ,len(word)) :
                                   
                                   if word[i] == str(inp) :
                                        clue[i] = str(word[i])
                                        flag = 1
                                        if i < len(word)-1:
                                            if word[i] != word[i+j]:
                                                break
                                        else :
                                            if word[-1] != word[-2]:
                                                break
                                   else :
                                        flag = 0
                                    
                    if flag == 1 :
                        print("good")
                    else :
                        lives = lives - 1
                        print("try again")
                        
                    if clue == word :
                        print(str(clue) + "\n\nYOU WON")
                        break
                        
                        
                    if lives == 0 :
                        print("GAME OVER")
                        break
                            
                    
    
        


        

