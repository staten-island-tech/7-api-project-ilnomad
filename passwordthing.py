""" The email must be a string and must contain an "@" symbol.
The password must also be a string.
The password must be at least 8 characters long.
The password must include at least one number.
The password must include at least one uppercase letter. """

def signup(email,password):
    a=b=False
    if "@" not in email: return("no @?")
    if type(email)!=str and type(password)!=str: return("smth not str")
    if len(password)<8: return("pswrd not laqueous enof")
    if not any (h.isupper for h in email): return("no capital")
    if not any (h.isdigit for h in email): return("no #")
    if a==b==True: return("you did it")
print(signup("nathanc124@nycstudents.net","Welcome1"))

