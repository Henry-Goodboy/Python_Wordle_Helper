


    
from allWords_final import allWords
# allWords = ['seven', 'world', 'about', 'again', 'heart', 'pizza', 'water', 'happy', 'hpppp', 'hpppy', 'sixty', 'board', 'month', 'angel', 'death', 'green', 'music', 'fifty', 'three', 'party', 'piano', 'mouth', 'woman', 'ruple', 'sugar']
# allWords = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy']
# allWords = ['xxxxx', 'rxxxx', 'rrxxx', 'rrrxx', 'rrrrx', 'rrrrr']

word_list = allWords.copy()



inputWord = ''
while inputWord != 'exit':

    output_list = []
    output_list_a = []


    inputWord, noLetter = input('words noletters: ').split() 
    # inputWord = '*U*i*' #DOES NOT LIKE *skiL* Returns empty list... FUCK! DOUBLE LETTER ISSUE/ STAR ISSUE? DOES NOT LIKE *snaE (no double letters) either.
    # noLetter = 'raton'

    

    iCounter = 0 # I COUNTER

    for word in word_list: # x_list, x_list equals survivors(iteration)
        for letter in word:
            
            xCounter = 0 # X COUNTER
            xLower = 0 # counts LOWER only
            xDouble = 0
            noLetCount = 0
            
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
                                
                            
            for letter in inputWord:    
                            
                if letter != '*': # CHECKS INPUT AND WORD FOR DOUBLE LETTERS
                    j = inputWord.count(letter)
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
                
                if letter.isupper() and (inputWord[xCounter].lower()) == word[xCounter]: #CHECKS UPPER CASER LETTERS FOR MATCHING POSITION
                    xCounter += 1
                else: pass
                
                if xCounter == 5 and xLower == 0 and j == k and noLetCount == 0: #COUNTS THE COUNTERS
                    
                    output_list_a.append(word) #MAKES THE NEW LIST
                    for i in output_list_a: 
                        if i not in output_list: 
                            output_list.append(i)
                    
            iCounter = iCounter + 1 #COUNTS LETTERS TO GET WORD COUNT (LETTERS/5)
            
            
        #TEST
        print('word#:', round(iCounter/5), '    j:', j, '   k:', k, '   Double?:', xDouble, '   xCounter=5:', xCounter, '   xLower=0:', xLower, '   noLetCount:', noLetCount)
    
                

    print('S1:', output_list)



        