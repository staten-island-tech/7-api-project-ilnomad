# Word Problem: The School Portal Login System
# Your school is creating a new online portal for students to sign up for accounts. The login system needs a function that accepts two pieces of information from the user:
# Their email address
# Their password
# Before creating the new account, the function must verify that the email and password follow school rules:
# The email must be a string and must contain an "@" symbol.
# The password must also be a string.
# The password must be at least 8 characters long.
# The password must include at least one number.
# The password must include at least one uppercase letter.
# If ANY of these rules are broken, the function should return an error message explaining what went wrong.
# If EVERYTHING is good, the function should return a dictionary that represents the newly created user.

def signup(email,password):
    n=0
    if "@" not in email:
        return"where ur @ at"
    if email!=str:
        return"ur email aint a string"
    for h in password:
        n+=1
    if not n>=8:
        return"ur password isnt long enough"
    for h in password:
        if not h.isupper():
            return"u dont got uppercase letter"
        if not h.isdigit():
            return"u dont got number"
    if password!=str:
        return"ur password aint a string"
    print("you did it")

signup("nathanc124@nycstudents.net","passworD123")