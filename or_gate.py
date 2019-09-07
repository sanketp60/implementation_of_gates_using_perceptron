#Initialize parameters
alpha=1 #Training speed
w1,w2,b=0,0,0 #weights and biases initialized
t=[-1,1,1,1] #declare target
x1=[-1,-1,1,1] #declare input 1
x2=[-1,1,-1,1] #declare input 2

#method to convert calculated o/p to actual o/p
def calc_yact(num):
    if(num>0):
        return 1
    elif(num==0):
        return 0
    else:
        return -1

#calculation function
def calc(x1,x2,t):  
    global w1
    global w2
    global b
    global alpha
    yact=calc_yact(w1*x1+w2*x2+b)

    #turing weights and biases if target not matched
    if(yact!=t):
        w1=w1+alpha*t*x1
        w2=w2+alpha*t*x2
        b=b+alpha*t

#executing loop for input sequence
for i in range(0,4):
    calc(x1[i],x2[i],t[i])
print(f'w1={w1}, w2={w2}, b={b}')
