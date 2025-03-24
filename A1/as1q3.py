feet=float(input("Enter Length In Feet : "))
print("ENTER 1 TO CONVERT FEET INTO INCHES")
print("ENTER 2 TO CONVERT FEET INTO YARDS")
print("ENTER 3 TO CONVERT FEET INTO MILES")
print("ENTER 4 TO CONVERT FEET INTO METRES")
print("ENTER 5 TO CONVERT FEET INTO MILLIMETRES")
print("ENTER 6 TO CONVERT FEET INTO CENTIMETRES")
print("ENTER 7 TO CONVERT FEET INTO KILOMETRES")
k=int(input("enter:"))
match k:
    case 1:
        inch=feet*12
        print(inch)
    case 2:
        yards=feet/3
        print(yards)
    case 3:
        mile=feet/5280
        print(mile)
    case 4:
        metre=feet/3.281
        print(metre)
    case 5:
        millimetre=feet*304.8
        print(millimetre)
    case 6:
        centimetre=feet*30.48
        print(centimetre)
    case 7:
        kilometre=feet/3281
        print(kilometre)
    

    
