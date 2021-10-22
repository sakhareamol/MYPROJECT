import os
def counter(fname):

    words = 0

    spaces = 0

    duplicate_words = 0

    special_character =0

    with open(fname,'r') as f:

        for line in f:

            line = line.strip(os.linesep)

            wordslist = line.split()

            num_words = num_words + len(wordslist)

            num_charc = num_charc + sum(1 for c in line 
                          if c not in (os.linesep, ' '))

            num_spaces = num_spaces + sum(1 for s in line 
                                if s in (os.linesep, ' '))

        print("Number of spaces in text file: ", words)
        print("Number of spaces in text file: ", num_spaces)

    if __name__ == '__main__': 
        fname = 'File1.txt'
        try: 
         counter(fname) 
        except: 
            print('File not found')

