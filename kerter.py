<<<<<<< HEAD
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
def nyolcszogKerulet ():
a=float(input("Kérem a nyolcszög oldalát [cm]: "))
return float (8*a)

def nyolcszogTerulet ():
a=float(input("Kérem a nyolcszög oldalát [cm]: ")
r=float(input("Kérem a nyolcszög sugarát [cm]: ")
return float (4*a*r) 
=======
def haromszogKerulete():
	a=float(input("Kérem a háromszög 'a' oldalát [cm]:"))
	b=float(input("Kérem a háromszög 'b' oldalát [cm]:"))
	c=float(input("Kérem a háromszög 'c' oldalát [cm]:"))
	return float (a+b+c)
	
def haromszogTerulete():
	a=float(input("Kérem a háromszög 'a' oldalát [cm]:"))
	ma=float(input("Kérem a háromszög 'm' magasságát [cm]:"))
	return float ((ma*a)/2)
>>>>>>> deae6c27373ba2e8915cd4b00f14ac54c3a3f5ee

print ("1 - Háromszög")
print ("2 - Kör")
print ("3 - Téglalap")
print ("4 - Nyolcszög")
v=input ("Milyen alakzattal szeretnél dolgoyni?")
it v =="1":
print(haromszogKerulete())
print(haromszogTerulete())