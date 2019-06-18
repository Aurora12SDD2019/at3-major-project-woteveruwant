from mods import *

test_leader_board = LeaderBoard()
test_file = open('tests\\name_banned_test.txt', 'r')
test_words = test_file.readlines()
test_file.close() #always good practice to close the file ASAP

for t in test_words:
    if "expected" in t: #headings
        print("{}\t actual".format(t.strip()))
    else:
        t = t.split("\t") #split it on tabs
    
        result = test_leader_board.name_banned(t[0])
        print("{}\t{}\t{}".format(t[0], t[1].strip(), result))
    
