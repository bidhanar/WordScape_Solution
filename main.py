#import itertools to find all combinations of letters
import itertools

#This function finds all the combinations of a list of letters and outputs a listg of these combinations
def combs(letters, startIdx):
    #base cases
    if startIdx == len(letters):
        return [""]

    # recursive cases
    res = []
    temp = []
    #exclude
    res = combs(letters, startIdx + 1)

    #include
    temp = res.copy()
    for i in range(len(temp)):
        temp[i] += letters[startIdx]
        res.append(temp[i])

    return res

#This function returns all the permutations of a list of words
def all_words(words):
    all = []
    for i in range(len(words)):
        perm = list(itertools.permutations(words[i]))
        for i in range(len(perm)):
            st = ""
            for j in range(len(perm[i])):
                st += perm[i][j]
            all.append(st)
    return all

def getAll(string):
    lis = []
    for i in range(len(string)):
        lis.append(string[i])
    words = combs(lis, 0)
    words_all = []
    #Since all the words in this game are more than or equal to three letters we remove all the words less than than three letters
    for i in range(len(words)):
        if(len(words[i]) >= 3):
            words_all.append(words[i])

    #combinantions is the list of all the valid combinations of the letters of length 3 or more
    combinations = all_words(words_all)
    lines = []
    #all_words.txt is the list of all words to search from
    #This list is taken from /usr/share/dict/words
    #To put yur list here all the text file in the path and replace all_words.txt with your file
    with open('all_words.txt') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        # lines[i] = lines[i][:len(lines[i]) - 2]
        lines[i] = lines[i].lower()
    # print(lines)
    answer = []
    for word in combinations:
        for i in range(len(lines)):
            if word+'\n' == lines[i]:
                # print(word + " " + lines[i])
                answer.append(word)
    # print(lines)
    answer = list(set(answer))
    print(sorted(answer, key=len))

string = "None"
#This runs until an empty string is passed.... No need to restart every new level
while(string != ""):
    string = input("Please enter all the letters:\n")
    getAll(string)