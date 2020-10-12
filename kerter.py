def nyolcszogKerulet ():
    a=float(input("Kérem a nyolcszög oldalát [cm]: "))
    return float (8*a)

def nyolcszogTerulet ():
    a=float(input("Kérem a nyolcszög oldalát [cm]: "))
    r=float(input("Kérem a nyolcszög sugarát [cm]: "))
    return float (4*a*r) 

def teglalapKerulet():
    a=int(input("Kérem a téglalap egyik oldalát [cm]:"))
    b=int(input("Kérem a téglalap másik oldalát [cm]:"))
    return float(2*(a+b))

def teglalapTerulet():
    a=int(input("Kérem a téglalap egyik oldalát [cm]:"))
    b=int(input("Kérem a téglalap másik oldalát [cm]:"))
    return float(a*b)

def haromszogKerulete():
    a=float(input("Kérem a háromszög 'a' oldalát [cm]:"))
    b=float(input("Kérem a háromszög 'b' oldalát [cm]:"))
    c=float(input("Kérem a háromszög 'c' oldalát [cm]:"))
    return float (a+b+c)
	
def haromszogTerulete():
    a=float(input("Kérem a háromszög 'a' oldalát [cm]:"))
    ma=float(input("Kérem a háromszög 'm' magasságát [cm]:"))
    return float ((ma*a)/2)


print ("1 - Háromszög")
print ("2 - Kör")
print ("3 - Téglalap")
print ("4 - Nyolcszög")
v=input ("Milyen alakzattal szeretnél dolgoyni?")

if v =="1":
	print(haromszogKerulete())
	print(haromszogTerulete())




if v =="3":
        print("Téglalap kerülete: ", teglalapKerulet(), "cm" )
        print("Téglalap területe: ", teglalapTerulet(), "cm2")



