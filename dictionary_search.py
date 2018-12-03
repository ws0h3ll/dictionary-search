filename = input("Where am i getting the file from senpai? ") # where am i looking for it
search = input("What am i trying to find?") # what am i looking for senpai
i = 0  # is zewo
with open(filename, 'r') as f: # i can read senpai
    for line in f: # itewationkdhfs sowwy too long of a word for little ol me
        for word in line.split(): # splits for me to read indivijual word
            i = i + 1 # when iterated it tells you where it found it 
            if word == search: # this checks if your word has been found senpai
                print(word) # pwints the word you were looking for 
                print("Senpai i found it on line ", i) # uwu senpai i found what you was looking for
            else:
                print("I could not find it sorry senpai pwease dont be mad") # please no be mad
