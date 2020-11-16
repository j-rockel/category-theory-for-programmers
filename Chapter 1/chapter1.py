def id(something): 
    return something

def compose(fun1, fun2, input): 
    return fun1(fun2(input))

def composeDoubleIdentityTest(input): 
    result = compose(id, id, input)
    if result == id(input): 
        print('True, compose(id, id, '+str(input)+') = '+str(result))
    else:
        print('False, compose(id, id, '+str(input)+') = '+str(result))
    return

def composeLeftIdentityTest(input, someFun): 
    result = compose(id, someFun, input)
    if result == someFun(input): 
        print('True, compose(id, '+str(someFun)+', '+str(input)+') = '+str(result))
    else:
        print('False, compose(id, '+str(someFun)+', '+str(input)+') = '+str(result))
    return

def composeRightIdentityTest(input, someFun): 
    result = compose(someFun, id, input)
    if result == someFun(input): 
        print('True, compose(id, '+str(someFun)+', '+str(input)+') = '+str(result))
    else:
        print('False, compose(id, '+str(someFun)+', '+str(input)+') = '+str(result))
    return
    
def testAll(input, someFun): 
    print('\nFor '+str(input)+' and '+str(someFun)+':')
    composeDoubleIdentityTest(input) 
    composeLeftIdentityTest(input, someFun)
    composeRightIdentityTest(input, someFun)
    return

def plusOne(x):
    return x + 1

testAll(0, plusOne)

def addB(x):
    return x + 'b'

testAll('a', addB)

