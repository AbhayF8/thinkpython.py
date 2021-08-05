fin = open('thinkpy.txt')
# for line in fin:
    # word=line.strip()
    # print(word)

# print(fin.readlines())

def read_words_txt(a,n):
    b=open(a)
    for line in b:
        word=line.strip()
        if len(word)>n:
            print(word)

    return '\nDone'

# print(read_words_txt('thinkpy.txt',20))

def has_no_e(a):
    for letter in a:
        if letter=='e':
            return False
    return True

# print(has_no_e('abhay'))

def has_no_e_words():
    b=open('thinkpy.txt')
    x=0
    y=0
    for line in b:
        y+=1
        word=line.strip()
        c=word.find('e')
        if c<0:
            print(word)
            x+=1
    return ('\n'+str(x/y*100)+'%'+' Words dont have e')
# print(has_no_e_words())

def avoids(word,string):
    for n in word:
        for m in string:
            if m==n:
                return False
    return True

# print(avoids('abhay','cda'))

def uses_only():
    n=0
    s=input('Enter the forbidden letters\n>> ')
    letsopen=open('thinkpy.txt')
    for words in letsopen:
        word=words.strip()
        if avoids(word,s):
            n+=1
            print(word)
    return 'No. of Words => '+str(n)
# uses_only()

def uses_all():
    a=input('Enter the word\n>> ')
    b=input('Enter the required letters\n>> ')
    for letters in a:
        if letters not in b:
            return False
    return True

# print(uses_all())

def is_abecedarian(word):
    n=0
    list1=[]
    for i in range(26):
        list1.append(i)

    print(list1)
is_abecedarian('w')