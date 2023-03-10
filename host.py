import graphB
import physicsB
from time import sleep
jared=10
xD=jared
yD=jared
xM=0
yM=0
t=0
testT=100
version=1
def call(a):
    return graphB.call(a,xD,yD)
print("BawolSimulator")
print("by Dyson Bawol")
print('''    1111
    1111
111111111111111111
    1111
    1111   11111111
    1111 11111111111
    111111         11
    11111           11
    1111             11
    1111             11
    1111             11
    1111             11''')
def userInterface():
    def default():
        print("You selected \"yes\"")
        print("Starting with default settings...")
    def alternate():
        global xD
        global yD
        global testT
        print("You selected \"no\"")
        in2=input("Please enter the simulation domain as an INT value")
        print("You selected "+in2)
        xD=int(in2)
        in3=input("Please enter the simulation range as an INT value")
        print("You selected "+in3)
        yD=int(in3)
        in4=input("Please enter the simulation time as an INT value")
        print("You selected "+in4)
        testT=int(in4)
    setIn1=None
    setIn=None
    DirSet=0
    while DirSet==0:
        inDir=input("Would you prefer to run a raw simulation or an object structure? (raw/obj)")
        if inDir=="raw":
            setIn1=1
            setIn=0
        elif inDir=="obj":
            setIn=1
            setIn1=0
        else:
            print("Invalid input. Please try again.")
        while setIn1==0:
            in1=input("Would you like to select a premade object or create a new one? (pre/new)")
            if in1=="pre":
                print("This feature is not available for this alpha version. Redirecting...")
                setIn1=1
            elif in1=="new":
                print("This feature is not available for this alpha version. Redirecting...")
                setIn1=1
        while setIn==0:
            in1=input("Would you like to proceed with the recommended settings? (y/n)")
            if in1=="y":
                default()
                setIn=1
                DirSet=1
            elif in1=="n":
                alternate()
                setIn=1
                DirSet=1
            else:
                print("Invalid input. Please try again.")
            
xP=xD
yP=yD
userInterface()
print("Configuring mapM...")
graphB.form(xD+1,yD+1,xM+1,yM+1)
print("Saving initial configuration...")
iC=call("ts")
iCR=call("t")
print("Simulation starting...")
for i in range(testT):
    print(t)
    print("Calling mapM...")
    call1=call("t")
    print("Simulating temperature via mKeep()...")
    newMapM=physicsB.mKeep(call1,xD,yD)
    print("Redefining mapM...")
    graphB.directMap(newMapM)
    t=t+1
print("Saving final configuration...")
fC=call("ts")
print("Before:\n")
print(iC)
print("After:\n")
print(fC)
print("^results^")
imageList=[]
imageList1=[]
x=0
for y in range(yD):
    cord=graphB.con(x,y)
    imageList=imageList+[call1[cord][0]*100,1000]
    for x in range(xD):
        cord=graphB.con(x,y)
        imageList=imageList+[call1[cord][0]*100,1000]
x=0
for y in range(yD):
    cord=graphB.con(x,y)
    imageList1=imageList1+[iCR[cord][0]*100,1000]
    for x in range(xD):
        cord=graphB.con(x,y)
        imageList1=imageList1+[iCR[cord][0]*100,1000]
print("Simulation concluded")