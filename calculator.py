hrs = input("Enter Hours: ")
rphrs = input("Enter Rate: ")

try:
    irphrs = float(rphrs)
    ihrs = int(hrs)

except:
    irphrs = -1
    ihrs = -1

if irphrs > 0.0 and ihrs > 0 :
    pay: float = float(hrs) * float(rphrs)
    print(pay)

else:
    print("Input not a Number")
