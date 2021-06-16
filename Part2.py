#1
fibonacci = [0,1,1]
while True:
    next = fibonacci[-1] + fibonacci[-2]
    if next<10000:
        fibonacci.append(next)
    else:
        break

print(f'Fibonacci serires till 10000 is: {fibonacci}')


check_Fibonaci = lambda x: x in fibonacci 

check_Fibonaci(610)
check_Fibonaci(611)




#2.1
list_a = [1,2,3,4,5,6,7,8,9]
list_b = [11,22,33,44,55,66,77,88,99]

a = list(filter(lambda x:x%2==0,list_a))
b = list(filter(lambda x:x%2!=0,list_b))
a
b

[x+y for x,y in list(zip(a,b) ) ]


#2.2    
name = 'Kshitij Mathur'
''.join([x for x in name if x.lower() not in ('a','e','i','o','u')])



#2.3
import math

inputlist = [1,2,4]
result = list(map(lambda x: 1 / (1 + math.exp(-x)),inputlist))

#2.4
input_string = 'tsaiz'
# [chr(ord(x) + 5) for x in input_string]
[chr(ord(x) + 5) if ord(x) < 118 else chr(ord(x) - 21) for x in input_string]

#3

from  urllib import request

def check_swear_words(input_para:str) -> bool:
    ''' Takes a string and tells if it contains any of the profane words managed at  https://raw.githubusercontent.com/RobertJGabriel/Google-profanity-words/master/list.txt '''
    
    url  = 'https://raw.githubusercontent.com/RobertJGabriel/Google-profanity-words/master/list.txt'
    google_profanity_words = request.urlopen(url)

    profane_words = []
    for line in google_profanity_words:
        profane_words.append(line.decode("utf-8").strip())

    return any([ True if inp in profane_words else False for inp in input_para.split(' ') ])


#4.1

from functools import partial, reduce
reduce(lambda x, y: x+y , filter(lambda x: x%2==0, [1,2,3,4,5,6]) )


#4.2
input_string = 'abcdz'
reduce(lambda a,b: a if a > b else b, input_string)


#4.3
inputlist = [0,1,2,3,4,5,6,7,8,9]
#list(filter(lambda a: inputlist.index(a) % 3 == 0, inputlist))
reduce(lambda a,b: a + b, filter(lambda a: inputlist.index(a) % 3 == 0, inputlist) )


#5
#KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999 PTS:100
import random
import string
gen = ('KA' + str(random.randint(10,99)) + random.choice(string.ascii_letters.upper()) + random.choice(string.ascii_letters.upper()) + str(x) for x in range(1000,9999))
for g in range(15):
    print(next(gen))


#6
from functools import partial

def complete(start,end,DL):
    gen = (DL + str(random.randint(10,99)) + random.choice(string.ascii_letters.upper()) + random.choice(string.ascii_letters.upper()) + str(x) for x in range(start,end))
    for g in range(15):
        print(next(gen))

f = partial(complete,1000,9999)
f('Ap')

