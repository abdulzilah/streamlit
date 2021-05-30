import os
import glob
uniquewords = set([])


for root, dirs, files in os.walk("C:\\Users\\abdul\\Desktop\\bigData\\data"):
    for name in files:
        [uniquewords.add(x)
         for x in open(os.path.join(root, name)).read().split()]

print(list(uniquewords))
print(len(uniquewords))
list_files = (glob.glob("C:\\Users\\abdul\\Desktop\\bigData\\data\\*.txt"))


def singleQuery(query):
    count = 0
    for file in list_files:
        with open(file) as f:
            if query in f.read():
                count = count+1
                print("The word: "+query + '  is found in file:  '+str(file))
    if count == 0:
        print("the word wasnt found in any of the stored files")


def AndQuery(query1, query2):
    count = 0
    for file in list_files:
        with open(file) as f:
            if query1 and query2 in f.read():
                count = count+1
                print("The words: "+query1+' and '+query2 +
                      '  are found in file:  '+str(file))
    if count == 0:
        print("the word wasnt found in any of the stored files")

AndQuery('football','doctor')
def OrQuery(query1, query2):
    count = 0
    for file in list_files:
        with open(file) as f:
            if query1 in f.read() or query2 in f.read():
                count = count+1
                print("The words: "+query1+' and '+query2 +
                      '  are found in file:  '+str(file))
    if count == 0:
        print("the word wasnt found in any of the stored files")


