# Question 1
class Memoizer:

    def __init__(self, function):
        self.function = function
        self.dictionary = dict()

    def memoized_no_args(self):
        if 'noinput' in self.dictionary:
            return self.dictionary['noinput']
        else:
            result = self.function()
            self.dictionary['noinput'] = result
            return result

    def memoized(self, input):
        if input in self.dictionary:
            return self.dictionary[input]
        else:
            result = self.function(input)
            self.dictionary[input] = result
            return result

def testcomplicatedfunction(x): 
    ints = list(range(1, x))
    y = 0
    for i in ints: 
        for j in ints: 
            for k in ints: 
                y += i-j+k
    return y

testfunmemoizer = Memoizer(testcomplicatedfunction)

print('running non-memoized function...')
print('output for 327 is '+str(testcomplicatedfunction(327)))
print('output for 327 is '+str(testcomplicatedfunction(327)))

print('running memoized function...')
print('output for 327 is '+str(testfunmemoizer.memoized(327)))
print('output for 327 is '+str(testfunmemoizer.memoized(327)))

# Question 2

from random import random, seed

randommemoizer = Memoizer(random)

print('running non-memoized random function...')
print('random number 1: random() = '+str(random()))
print('random number 2: random() = '+str(random()))

print('running non-memoized random function...')
print('random number 1: random() = '+str(randommemoizer.memoized_no_args()))
print('random number 2: random() = '+str(randommemoizer.memoized_no_args()))

# Question 3

seed(327)

print('running non-memoized random function with seed set to 327...')
seed(327)
print('random number 1: random() = '+str(random()))
seed(327)
print('random number 2: random() = '+str(random()))

seed(327)
randomseedmemoizer = Memoizer(random)

print('running memoized random function with seed set to 327...')
print('random number 1: '+str(randomseedmemoizer.memoized_no_args()))
print('random number 2: '+str(randomseedmemoizer.memoized_no_args()))

# Question 4 a)

def fact(n):
    result = 1
    for i in range(2,n):
        result *= i
    return result

print('running non-memoized factorial function...')
print('fact(65) = ' + str(fact(65)))
print('fact(65) = ' + str(fact(65)))

factmemoizer = Memoizer(fact)

print('running memoized factorial function...')
print('fact(65) = ' + str(factmemoizer.memoized(65)))
print('fact(65) = ' + str(factmemoizer.memoized(65)))

# Question 4 d)

def f(x):
    f.y += x
    return f.y
f.y = 0

print('running non-memoized f...')
print('f(5) = '+str(f(5)))
print('f(5) = '+str(f(5)))

fmemoizer = Memoizer(f)

print('running memoized f...')
print('f(5) = '+str(fmemoizer.memoized(5)))
print('f(5) = '+str(fmemoizer.memoized(5)))

# Question 5

def id(bool):
    return bool

def flip(bool):
    if bool == True:
        return False
    if bool == False: 
        return True

def true(bool):
    return True

def false(bool):
    return False