import functions
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
