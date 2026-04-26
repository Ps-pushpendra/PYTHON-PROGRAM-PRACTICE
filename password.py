password = input("enter password:")
letter = digits = special = 0
for ch in password:
    if ch.isalpha():
        letter+=1
    elif ch.isdigit():
        digits+=1
    else:
        special+=1
        
print("letters = ",letter)
print("digits = ",digits)
print("special = ",special)