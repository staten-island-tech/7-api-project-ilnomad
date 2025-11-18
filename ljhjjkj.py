plusminus=[1,1,0,-1,-1]
def posneg(plusminus):
    a=pluscount=zerocount=minuscount=b=0
    for h in plusminus:
        if plusminus[a]<0:
            minuscount+=1
        elif plusminus[a]>0:
            pluscount+=1
        else:
            zerocount+=1
        a+=1
        b+=1
    print(f"Positive:{pluscount/b}, Zero:{zerocount/b}, Negative:{minuscount/b}")
posneg(plusminus)