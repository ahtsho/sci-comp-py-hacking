__author__ = 'Ahadu Tsegaye Abebe - 09/07/17'

def printTestName(name):
    print("- - - - {} - - - - -".format(name))
#lambda arguments: expression
#lambda with name binding
sum = lambda x, y: x+y

def testLambdaSum():
    printTestName("lambda")
    print "lambda sum(3,5) = {}\n".format(sum(3,5))

#MAP
def testMap():
    printTestName("map")
    print "map f(x)=x^2+3 to [0,1,...10] ->",map(lambda x:x**2+3, range(10)),"\n"

#FILTER
def testFilter():
    printTestName("filter")
    y = map(lambda x:x**2+3, range(10))
    print "filter evens from map above ->", filter(lambda x: x%2==0, y),"\n"


#REDUCE
'''
list = [x0,x1,x2,x3,...,xn]
given g(x,y) reduce(g(x,y),list) ->  g(...g(g(g(x0,x1),x3),x4),...xn)
'''

def testReduce():
    printTestName("reduce")
    list = [x*2 for x in range(6)]
    print "reduce [0,2,4,...,10] with g(x,y)=x+y ->", reduce(lambda x,y: x+y,list),"\n"

def fibonacciReduce(n):
    fib = [0,1]
    for i in range(1,n):
        fib.append(reduce(lambda x,y: x+y,(fib[i-1],fib[1-2])))
    return fib

def testfibonacci():
    printTestName("Fibonacci")
    print "first 10 fibonacci numbers: ",fibonacciReduce(10),"\n"

'''
def flattenList(li):
    if type(li,list)=='list':
        for l in li:
            flattenList()
'''


def testFlattenList():
    printTestName("flattenList")
    #print flattenList([[1,2,3],[4,[5,6,[7,8]]],[9],10])


testLambdaSum()
testMap()
testFilter()
testReduce()
testfibonacci()

#testFlattenList()