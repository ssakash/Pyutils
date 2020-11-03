f   = open("words.txt")
content =  f.read()
s_content = content.split()
word  = ""
count =  0
s  = 0
debug = 0 # Turn to  1 to enable advanced debugging


word  = input("Mention the word which needs to be counted:")



for split in s_content:
    node = str(split)
    if (debug):
        print("%s  == %s"%  (node, word))
    if  (node == word):
        count += 1
    s += 1    
    
print("Total  words: %d   Searched word: %d" % (s,count))