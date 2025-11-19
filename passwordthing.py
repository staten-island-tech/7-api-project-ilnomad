def signup(email,password):
    a=b=c=d=e=f=n=0
    if "@" in email:
        a=1
    if type(email)==str:
        b=1
    for h in password:
        n+=1
    if n>=8:
        c=1
    for h in password:
        if h.isupper():
            d=1
        if h.isdigit():
            e=1
    if type(password)==str:
        f=1
    if a==b==c==d==e==f==1:
        print("you did it")
    else:
        if a==0:
            print("@?")
        if b==0:
            print("strng email?")
        if c==0:
            print("paswrd not laqueous enof")
        if d==0:
            print("uprcse ltr?")
        if e==0:
            print("nmbr?")
        if f==0:
            print("strng paswrd?")

signup("nathanc124@nycstudents.net","Welcome1")

