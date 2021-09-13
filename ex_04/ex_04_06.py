from var_dump import var_dump

def computepay(hours, rate):
    var_dump("In computepay", hours, rate)
    if hours > 40:
        reg = hours * rate
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()

print("Pay:", computepay(fh, fr))

