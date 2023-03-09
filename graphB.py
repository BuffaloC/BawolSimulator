yl=0
xl=0
mapM={}
mapMp={}
devT={}
def con(x,y):
    return x.__str__()+","+y.__str__()
def plot(x,y,Em,T):
    #exceptions needed
    global mapM
    cord=con(x,y)
    mapM[cord]=[Em,T]
    return "Success Written-->"+cord+":"+mapM[cord].__str__()
def call(a,x,y):
    if a=="ts":
        yl=y
        xl=x
        ret=""
        y=0
        x=0
        for y in range(yl):
            cord=con(x,y)
            ret=ret+"\n"
            ret=ret+mapM[cord].__str__()
            ret=ret+" "
            for x in range(xl):
                if x!=0:
                    cord=con(x,y)
                    ret=ret+mapM[cord].__str__()
                    ret=ret+" "
        return ret
    elif a=="t":
        return mapM
    elif a=="d":
        return [mapMp,devT]
    elif a=="s":
        cord=con(x,y)
        return mapM[cord]
def form(x,y,rM,rT):
    from random import random
    xl=x
    yl=y
    y=0
    x=0
    for y in range(yl):
        cord=con(x,y)
        randMass=round(random()*rM)
        randTemp=round(random()*rT)
        mapM[cord]=[randMass,randTemp]
        for x in range(xl):
            cord=con(x,y)
            randMass=round(random()*rM)
            randTemp=round(random()*rT)
            mapM[cord]=[randMass,randTemp]
def directMap(in1):
    mapM=in1