def haromszogKerulete():
	a=float(input("Kérem a háromszög 'a' oldalát [cm]:"))
	b=float(input("Kérem a háromszög 'b' oldalát [cm]:"))
	c=float(input("Kérem a háromszög 'c' oldalát [cm]:"))
	return float (a+b+c)
	
def haromszogTerulete():
	a=float(input("Kérem a háromszög 'a' oldalát [cm]:"))
	ma=float(input("Kérem a háromszög 'm' magasságát [cm]:"))
	return float ((ma*a)/2)