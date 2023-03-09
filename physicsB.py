import graphB
from random import random
#Control how temperature is represented:
def tempFunc(mapM,xD,yD):
    x=0
    y=0
    mD1={}
    def rand(x,y,mD1):
        cord=graphB.con(x,y)
        T=mapM[cord][1]
        r=round(random()*3)
        if r==0:
            mD1[cord]=[T,0]
        elif r==1:
            mD1[cord]=[0,T]
        elif r==2:
            mD1[cord]=[-T,0]
        elif r==3:
            mD1[cord]=[0,-T]
        return mD1
    for y in range(yD):
        mD1=rand(x,y,mD1)
        for x in range(xD):
            mD1=rand(x,y,mD1)
    return mD1
#A mess of logic that makes motion deviations work:
def mKeep(mapM,xD,yD):
    #This top code connects our mode to its associated function
    #returning the correct value for set 'mD'
    x=0
    y=0
    mapCombos={}
    mD={}
    for y in range(yD):
        cord=graphB.con(x,y)
        ret1=tempFunc(mapM,xD,yD)
        cordFx=x+ret1[cord][0]
        cordFy=y+ret1[cord][1]
        mD[cord]=[cordFx,cordFy]
        for x in range(xD):
            cord=graphB.con(x,y)
            ret1=tempFunc(mapM,xD,yD)
            cordFx=x+ret1[cord][0]
            cordFy=y+ret1[cord][1]
            mD[cord]=[cordFx,cordFy]
    x=0
    y=0
    def compare(cord):
        x1=0
        y1=0
        for y1 in range(yD):
            cord1=graphB.con(x1,y1)
            if cord1!=cord:
                if mD[cord]==mD[cord1]:
                    return {cord:cord1}
            for x1 in range(xD):
                cord1=graphB.con(x1,y1)
                if cord1!=cord:
                    if mD[cord]==mD[cord1]:
                        return {cord:cord1}
        return None
    for y in range(yD):
        cord=graphB.con(x,y)
        compResult=compare(cord)
        if compResult==None:
            mapCombos[cord]=None
        else:
            mapCombos[cord]=compResult[cord]
        for x in range(xD):
            cord=graphB.con(x,y)
            compResult=compare(cord)
            if compResult==None:
                mapCombos[cord]=None
            else:
                mapCombos[cord]=compResult[cord]
    result=mapUpdate(mapM,mapCombos,mD,xD,yD)
    return result
def mapUpdate(mapM,mapCombos,mD,xD,yD):
    x=0
    y=0
    def mapFinal(mapM,mapCombos,mD,x,y):
        cord=graphB.con(x,y)
        cord1=mapCombos[cord]
        xF=x+mD[cord][0]
        yF=y+mD[cord][1]
        cordF=graphB.con(xF,yF)
        if cord1!=None:
            massF=mapM[cord][0]+mapM[cord1][0]
            tempF=mapM[cord][1]+mapM[cord1][1]
            mapM[cordF]=[massF,tempF]
            mapM[cord]=[0,0]
    for y in range(yD):
        mapFinal(mapM,mapCombos,mD,x,y)
        for x in range(xD):
            mapFinal(mapM,mapCombos,mD,x,y)
    graphB.directMap(mapM)
    return mapM
   