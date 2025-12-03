def signup(email,password):
    a=b=c=d=e=f=n=0
    if "@" in email:
        a=1
    if type(email)==str:
        b=1
    if len(password)>=8:
        c=1
    if (h.isupper for h in email): d=1
    if (h.isdigit for h in email): e=1
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