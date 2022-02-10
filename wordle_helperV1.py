from allWords_final import allWords
# allWords = ['seven', 'world', 'about', 'again', 'heart', 'pizza', 'water', 'happy', 'hpppp', 'hpppy', 'sixty', 'board', 'month', 'angel', 'death', 'green', 'music', 'fifty', 'three', 'party', 'piano', 'mouth', 'woman', 'ruple', 'sugar']
# allWords = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy']
# allWords = ['smirk']

word_list = allWords.copy() ## Makes a copy of all words and puts it into loop.

inputWord = ''

output_list = []
output_list_a = []

# ---------------------------------- START OF LOOP

while inputWord != 'exit':

    inputWord = input('Upper, Lower or Wild i.e. *xXx* : ')
    if inputWord == 'exit': #Forces immediate EXIT without going to second input.
        break
    noLetter = input('Not these letters : ')
     
    iCounter = 0 # I COUNTER

    for word in word_list: # x_list, x_list equals survivors(iteration)
        for letter in word:
            
            xCounter = 0 # X COUNTER
            xLower = 0 # counts LOWER only
            xDouble = 0
            noLetCount = 0
            
# ---------------------------------- START NOLETTER QUALIFIER  # Needs to be condensed. 
            
            for letter in noLetter: #Qualifies noLetter and Changes to noLetAddStar
                if len(noLetter) <= 5: 
                    if len(noLetter) == 5:
                        noLetAddStar = (noLetter + '')
                    if len(noLetter) == 4:
                        noLetAddStar = (noLetter + '*')
                    if len(noLetter) == 3:
                        noLetAddStar = (noLetter + '**')
                    if len(noLetter) == 2:
                        noLetAddStar = (noLetter + '***')
                    if len(noLetter) == 1:
                        noLetAddStar = (noLetter + '****')
                else: pass
                    
                if (noLetAddStar[0]) in word: #CHECKS WORD FOR NOLETTERS
                    noLetCount += 1
                elif (noLetAddStar[1]) in word:
                    noLetCount += 1
                elif (noLetAddStar[2]) in word:
                    noLetCount += 1
                elif (noLetAddStar[3]) in word:
                    noLetCount += 1
                elif (noLetAddStar[4]) in word:
                    noLetCount += 1
                else: pass

# ---------------------------------- END NOLETTER QUALIFIER                                
                            
            for letter in inputWord:    
                            
                if letter != '*': # CHECKS INPUT AND WORD FOR DOUBLE LETTERS
                    h = inputWord.lower() #MAKE EVERTHING LOWER FOR DOUBLE COMPARISON
                    j = h.count(letter) #H INSTEAD OF INPUTWORD (NOW LOWER)
                    k = word.count(letter)
                    # print(i)

                if letter.islower() and (inputWord[xCounter]) == word[xCounter] and j == 2: #IS LOWER, ACCOUNTS FOR DOUBLES         
                    xDouble += 1 
                elif letter.islower() and (inputWord[xCounter]) == word[xCounter] and j == 3: #IS LOWER, ACCOUNTS FOR TRIPLES         
                    xDouble += 2 
                elif letter.islower() and (inputWord[xCounter]) == word[xCounter] and j == 4: #IS LOWER, ACCOUNTS FOR QUADRUPLES         
                    xDouble += 3                 
                else: pass
                
                if letter.islower() and (inputWord[xCounter]) == word[xCounter]: #IS LOWER AND KILLS DIRECT MATCHES         
                    xLower += 1 #IF THIS IS ANYTHING BUT 0 WORD IS NOT APPENDED TO NEW LIST
                else: pass
                
                if letter.islower() and (inputWord[xCounter]) in word: #IS LOWER FORCES INCLUSION
                    xCounter += 1
                else: pass
                
                if letter == '*': #IS STAR
                    xCounter += 1
                else: pass
                
                if letter.isupper() and (inputWord[xCounter].lower()) == word[xCounter]: #CHECKS UPPERCASE LETTERS FOR MATCHING POSITION
                    xCounter += 1
                else: pass
                
                if xCounter == 5 and xLower == 0 and j == k and noLetCount == 0: #COUNTS THE COUNTERS
                    
                    

                    output_list_a.append(word) #MAKES THE NEW LIST
                    for i in output_list_a: 
                        if i not in output_list: 
                            output_list.append(i)
                            
            iCounter = iCounter + 1 #COUNTS LETTERS TO GET WORD COUNT (LETTERS/5)

        #TEST
        # print('REPORT OUT --- word#:', round(iCounter), '    j:', j, '   k:', k, '   Double?:', xDouble, '   xCounter=5:', xCounter, '   xLower=0:', xLower, '   noLetCount:', noLetCount)

    # print('S1:', output_list)
    
    word_list = output_list.copy()
    
    output_list = []
    output_list_a = []
    
    print('Last Line', word_list)
    
    
    
    
    



        