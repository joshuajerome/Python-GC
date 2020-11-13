# Python Graphing Calculator Project

Find out more about me on [my site](https://sites.google.com/view/sherwin-jeromes-page/home)!

## About the Project

This was an invite-only project designed by my AP Computer Science teacher for the top two performing students in each of his classes. The APCS cirriculum taught Java programming language, but this project was in Python. Furthermore, this project focussed on Lambda functions. Students were expected to have no programming experience in Python, and were to code only in terminal. IDEs were restricted so students could find and resolve errors by themselves.

Terminal ran Python 3.7 at the time of this project. Students would store code on an external application such as Notes, Word Document, or Google Docs. 

## Starting the Project

Students were first taught what lambda functions were: small functions that could take _n_ number of arguments, but can only have one expression. Next, students were shown an example of very basic functions:

```markdown

import math
f = lambda x: 2 + x  `returns the sum of 2 and any given number`
g = lambda x: 2 * x `returns the product of 2 and any given number`

```

Using this basic understanding of functions, the next step was creating a _doTwice_ function which would essentially do a function twice. Students were expected to code this on their own which posed a challenge as we had to use our programming knowledge of Java to find a solution. For each succeding function, our teacher would conceptually describe its purpose and leave the coding to students. Students could not ask for help, search up solutions, and upon completion had to explain each piece in the one line of code.

## Goal

Ultimately, students would use their new-found knowledge of Lambda functions to write code for a fully functional graphing calculator. Features of the calculator include:

- returning a string with proper character syntax such that it could be copied and pasted into an online graphing utility such as [Desmos](https://www.desmos.com/calculator)
- Lagrange Interpolation
- Approxmation of Sine and Cosine up to 14 decimal points
- Polynomial arithmetics
- Differentiation and Integration

Upon completion of the Graphing Calculator, students were also asked to create Merge Sort and Binary Search Functions

## Code

Listed Below are all functions created in the project with descriptions, followed by test code - the soltution that I coded and successfully executed in Terminal for the Graphing Calculator Project.

```markdown

import math

`Used to access math.pi`

doTwice = lambda f : lambda x: f(f(x))

`Executed a function twice`

fib = lambda n : 1 if n < 2 else fib(n-1) + fib(n-2)

`Returns the nth term of the Fibonacci Sequence`

compose = lambda f,g: lambda x: f(g(x))

`Performs the composition of a function. Mathematical understanding: f(g(x)) or g(f(x))`

repeat = lambda f,n : (lambda x: x) if n == 0 else lambda x: f(repeat(f,n-1)(x))

`Repeats a function n number of times`

successor = lambda x: x+1

`Given a number x, provides the next number`

add = lambda x,y : repeat(successor,y)(x)

`Adds two numbers x and y together. add is defined as repetitive successtion`

mult = lambda x,y : repeat((lambda z: add(x,z)),y)(0)

`Multiplies two numbers x and y together. mult is defined as repetitive addition`

power = lambda x,n : repeat((lambda y: mult(x,y)),n)(1)

`Raises a number x to the nth power. power is defined as repetitive multiplication`

limit = lambda f,s,e,t: f((s+e)/2) if abs(f((s+e)/2)-f(s)) <= t else limit(f,((s+e)/2),e,t)

`Finds the limit of a function f given a start s, end e, and interval t`

limitList = lambda f,s,e,t: [f((s+e)/2)] if abs(f((s+e)/2)-f(s)) <= t else [f((s+e)/2)] + (limitList(f,(s+e)/2,e,t))

`Shows the value the limit function executes until base case is hit in a list format `

derivative = lambda f,x: limit(lambda h: ((f(x+h)-f(x))/h),1,0,0.001)

`Takes the derivative of a function at a point x using the limit process`

(W/o limit) integral  = lambda f,a,b : abs(b-a)*((f(a)+f(b))/2) if abs(b-a) < 2 else abs((f(a+1)+f(a))/2) + integral(f,a+1,b)

`Integrates a function f from a to b without using the limit process`

allHeights = lambda f,a,b,d: f(a) if abs(b-a) <= d else f(a) + allHeights(f,a+d,b,d)
integral = lambda f,a,b : limit(lambda x: x*allHeights(f,a,b,x),1,0,0.01)

`Integrates a function f from a to b using the limit process. Additionally uses a helper function allHeights which sums the values of the function f at all points incrementing by a number d, between values a and b`

intList = lambda f,a,b : limitList(lambda x: x*allHeights(f,a,b,x),a,b,1)

`Shows the value the intergral function executes until base case is hit in a list format`

remaining = lambda pa,pb: pa[len(pb):len(pa)] if len(pb) < len(pa) else pb[len(pa):len(pb)]

`Given two polynomials pa and pb, returns the terms included in one polynomial that doesn't exist in the other` 

shorter = lambda pa,pb: pa if len(pa) < len(pb) else pb

`Returns the shorter polynomial (by length)`

addPoly = lambda pa,pb: remaining(pa,pb) if len(shorter(pa,pb))==0 else [pa[0]+pb[0]] + remaining(pa,pb) if len(shorter(pa,pb)) == 1 else ([pa[0]+pb[0]] + addPoly(pa[1:len(shorter(pa,pb))],pb[1:len(shorter(pa,pb))])) + remaining(pa,pb)

`Adds polynomial pa to pb`

distribute = lambda x,pa: [pa[0]*x] if len(pa)==1 else [pa[0]*x] + distribute(x,pa[1:])

`Multiplies a polynomnial pa by a number`

multPoly = lambda pa,pb: distribute(pa[0],pb) if len(pa)==1 else addPoly(distribute(pa[0],pb),[0]+multPoly(pa[1:],pb))

`Multiplies two polynomials pa and pb`

evaluate = lambda p: lambda x: 0 if len(p) == 0 else p[0] if len(p) == 1 else evaluate(distribute(x,p[1:]))(x) + p[0]

`Evaluates a polynomial at a value x`

`For the following code:
lagrangeConstant takes a list of points excluding the jth point, and the x value of the jth point
lagrangeExpression takes a list of points excluding jth point`

points = [[1,2],[3,4],[5,1],[6,3]]

`Sample list of points`

lagrangeConstant  = lambda l,val: val-l[0][0] if len(l) == 1 else (val-l[0][0])*lagrangeConstant(l[1:],val)
lagrangeExpression = lambda l: [-l[0][0],1] if len(l)==1 else multPoly([-l[0][0],1],lagrangeExpression(l[1:]))
lagrangeBasic = lambda l,j: distribute(l[j][1]/lagrangeConstant(l[:j]+l[j+1:],l[j][0]),lagrangeExpression(l[:j]+l[j+1:]))

`Three helper functions that create a list of polynomials from a list of points`

lagHelp = lambda l,n: lagrangeBasic(l,n) if n==len(l)-1 else addPoly(lagrangeBasic(l,n),lagHelp(l,n+1))

`Uses the list of polynomials to interpolate the Lagrange polynomial`

interpolate = lambda l: lagHelp(l,0)

`Returns the lagrange polynomial as a function`

polyString = lambda l: str(0) if len(l)==0 else str(l[0]) if len(l)==1 else str(l[0])+ "+" +str(l[1])+"x" if len(l)==2 else polyString(l[:len(l)-1])+"+"+str(l[len(l)-1])+"x^"+str(len(l)-1)

`Returns a string that represents a polynomial that can be copied and pasted into a graphing utility`

listOfNPoints = lambda f,s,e: [[s,f(s)]] if s==e else [[s,f(s)]] + listOfNPoints(f,s+1,e)

`Creates a list of points from a function f, between a start and end, s and e`

dirPolyAt = lambda p,s,e : [[s,derivative(evaluate(p),s)]] if s==e else [[s,derivative(evaluate(p),s)]] + dirPolyAt(p,s+1,e)

`Finds the derivative of a polynomial at a certain value`

derivativePolynomial = lambda p: interpolate(dirPolyAt(p,1,len(p)-1))

`returns the derivative of polynomial as a polynomial`

createList = lambda f,s,e,t: [[s,f(s)]] if s==e else [[s,f(s)]] + createList(f,s+t,e,t)

`Returns list of 10 points which are a result of derivative of function(1—>10)`

dirFuncAt = lambda f,s,e,t: [[s,derivative(f,s)]] if s==e else [[s,derivative(f,s)]] + dirFuncAt(f,s+t,e)

`Differentiate a function f on the interval s to e at an interval t`

dirFunc = lambda f: interpolate(dirFuncAt(f,1,10,1))

`Returns the derivative of a function f as a function`

refinePoly = lambda p: p if p[len(p)-1] > 0.1 else refinePoly(p[:len(p)-1])

`Refines a polynomnial by removing irrelevant terms such as 0x^2`

`Transform: 
“a” is vertical stretch, “b” is horizontal stretch, “c” horizontal displacement, “d” is vertical displacement`

transform = lambda f,a,b,c,d: lambda x: a*f(b*x+c)+d

`Applies transformations to a function f`

cos = evaluate(interpolate(dirFuncAt(math.sin,0,4*math.pi,math.pi/2)))

`Creates Cosine by first creating a list of points differntiating Sine on an interval, then interpolating those points`

graphCosine = polyStringTrig(interpolate(createList(cos,0,2*math.pi,math.pi/2)))

`Returns a string that represents Cosine`

functionInPeriod = lambda f,a,b: polyString(interpolate(createList(f,a,b,math.pi/4)))

`Returns a string that represents a trig function on an interval a to b`

period = lambda f,a,b: lambda x: f(x) if (x >= a and x< b) else period(f,a,b)(x-(b+a)) if x > b else period(f,a,b)(x+(b-a))

`Returns the period of a function`

merge = lambda l1,l2: l1+l2 if len(l2)* len(l1) == 0 else ([l1[0]] + merge(l1[1:],l2) if l1[0] < l2[0] else [l2[0]] + merge(l1,l2[1:]))
mergeSort = lambda l: [] if len(l) == 0 else l if len(l) == 1 else merge(mergeSort(l[:int(len(l)/2)]),mergeSort(l[int(len(l)/2):]))

`Merge Sort function uses merge. Merge sort sorts a function recursively by divide and conquer method`

getIndex = lambda l,n: 0 if len(l) <= 1 else 0 if l[0] == n else 1 + getIndex(l[1:],n)

`Returns the index of an element n in a list l`

partition = lambda l: [] if len(l) == 0 else l if len(l) == 1 else ([l[1]]+partition(l[:1]+l[2:]) if l[1] <= l[0] else partition(l[:1] + l[2:]) + [l[1]])

`Partitions a list around the first element in smallest to largest order`

partition = lambda l: [] if len(l) == 0 else l if len(l) == 1 else ([l[0]]+partition(l[1:]) if l[0] <= l[len(l)-1] else partition(l[1:]) + [l[0]])

`Partitions a list around the lasat element in smallest to largest order`

sin = lambda x: period(evaluate(interpolate(createList(math.sin,0,2*math.pi,math.pi/5))),0,2*math.pi)(x)

`Returns a polynomial that represents Sine that has precision up to 14 decimal places`

howMuchOff = lambda n: 0 if n >= 2*math.pi else (abs(math.sin(n) - sin(n)) + howMuchOff(n+0.1))

`Returns the difference between math.sin and my Sine approximation`

OffAtEachPoint = lambda n: [abs(math.sin(n) - sin(n))] if n >= 2*math.pi else [abs(math.sin(n) - sin(n))] + OffAtEachPoint(n+0.01)

`Function provides a list of all points used to create the Sine approximation`

```
## Test Code

This test code is a list of the essential functions in a graphing calculator. If you plan to run the following code in terminal or other command line systems, I recommend inserting code one paragraph at a time as formatted below. At the bottom of the test code, I have included some sample code and a video of me testing it.

```markdown
import math
remaining = lambda pa,pb: pa[len(pb):len(pa)] if len(pb) < len(pa) else pb[len(pa):len(pb)]
shorter = lambda pa,pb: pa if len(pa) < len(pb) else pb
addPoly = lambda pa,pb: remaining(pa,pb) if len(shorter(pa,pb))==0 else [pa[0]+pb[0]] + remaining(pa,pb) if len(shorter(pa,pb)) == 1 else ([pa[0]+pb[0]] + addPoly(pa[1:len(shorter(pa,pb))],pb[1:len(shorter(pa,pb))])) + remaining(pa,pb)
distribute = lambda x,pa: [pa[0]*x] if len(pa)==1 else [pa[0]*x] + distribute(x,pa[1:])
multPoly = lambda pa,pb: distribute(pa[0],pb) if len(pa)==1 else addPoly(distribute(pa[0],pb),[0]+multPoly(pa[1:],pb))
lagrangeConstant  = lambda l,val: val-l[0][0] if len(l) == 1 else (val-l[0][0])*lagrangeConstant(l[1:],val)
lagrangeExpression = lambda l: [-l[0][0],1] if len(l)==1 else multPoly([-l[0][0],1],lagrangeExpression(l[1:]))
lagrangeBasic = lambda l,j: distribute(l[j][1]/lagrangeConstant(l[:j]+l[j+1:],l[j][0]),lagrangeExpression(l[:j]+l[j+1:]))

lagHelp = lambda l,n: lagrangeBasic(l,n) if n==len(l)-1 else addPoly(lagrangeBasic(l,n),lagHelp(l,n+1))
interpolate = lambda l: lagHelp(l,0)
polyString = lambda l: str(0) if len(l)==0 else str(l[0]) if len(l)==1 else str(l[0])+ "+" +str(l[1])+"x" if len(l)==2 else polyString(l[:len(l)-1])+"+"+str(l[len(l)-1])+"x^"+str(len(l)-1)
limit = lambda f,s,e,t: f((s+e)/2) if abs(f((s+e)/2)-f(s)) <= t else limit(f,((s+e)/2),e,t)
derivative = lambda f,x: limit(lambda h: ((f(x+h)-f(x))/h),1,0,0.001)
dirFuncAt = lambda f,s,e,t: [[s,derivative(f,s)]] if s==e else [[s,derivative(f,s)]] + dirFuncAt(f,s+t,e,t)
dirFunc = lambda f: interpolate(dirFuncAt(f,1,10))
refinePoly = lambda p: p if p[len(p)-1] > 0.1 else refinePoly(p[:len(p)-1])

evaluate = lambda p: lambda x: 0 if len(p) == 0 else p[0] if len(p) == 1 else evaluate(distribute(x,p[1:]))(x) + p[0]
transform = lambda f,a,b,c,d: lambda x: a*f(b*x+c)+d
cos = evaluate(interpolate(dirFuncAt(math.sin,0,4*math.pi,math.pi/2)))
createList = lambda f,s,e,t: [[s,f(s)]] if s==e else [[s,f(s)]] + createList(f,s+t,e,t)
graphCosine = polyString(interpolate(createList(cos,0,2*math.pi,math.pi/2)))
period = lambda f,a,b: lambda x: f(x) if (x >= a and x< b) else period(f,a,b)(x-(b+a)) if x > b else period(f,a,b)(x+(b-a))
sin = lambda x: period(evaluate(interpolate(createList(math.sin,0,2*math.pi,math.pi/5))),0,2*math.pi)(x)
howMuchOff = lambda n: 0 if n >= 2*math.pi else (abs(math.sin(n) - sin(n)) + howMuchOff(n+0.1))
OffAtEachPoint = lambda n: [abs(math.sin(n) - sin(n))] if n >= 2*math.pi else [abs(math.sin(n) - sin(n))] + OffAtEachPoint(n+0.01)

```
## Video Example
[](https://www.youtube.com/watch?v=CYzYW3znVHo&list=PL31HaAenzL5NA_1_7AqDwY1RZdEqE6jRM)
