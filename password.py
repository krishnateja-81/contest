password = input("enter password:")

def Capital(password):
    cap = False
    for i in password:
        if i == i.upper():
            cap = True
            return cap
def lower(password):
    low = False
    for i in password:
        if i == i.lower():
            low = True
            return low
def length(password):       
    if len(password) >= 6:
        return True
    else:
        return False

if Capital(password) and lower(password) and length(password):
    print("strong password")
else:
    print("week")
