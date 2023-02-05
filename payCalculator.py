def calculatePay():
    # Implement your solution in between the two comment blocks
    print("calculating pay")
    # This first line is provided for you
    hrs = float(input("Enter Hours:"))
    rate = float(input("Enter Rate:"))

    pay = hrs * rate

    if hrs > 40:
        othours = float(hrs - 40) 
        otrate = float(.5 * rate)
        otpay = float(othours * otrate) 

        totalpay = float(pay + otpay)
        print(totalpay)

    if hrs <= 40:
        print (pay)
    
    # end assignment


## If you want to test locally before you try to sync
## Open your terminal and run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
