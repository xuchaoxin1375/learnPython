import datetime
today = datetime.datetime.now()

# Prints readable format for date-time object

print (type(today),str(today))
# prints the official format of date-time object
print (repr(today))	
er_today=eval(repr(today))
print(type(er_today),er_today)
##
# Python program to demonstrate writing of __repr__ and
# __str__ for user defined classes

# A user defined class to represent Complex numbers
class Complex:
	# Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # For call to repr(). Prints object's information
    def __repr__(self):
        return 'by __repr__🎈:Rational(%s, %s)' % (self.real, self.imag)	

    # For call to str(). Prints readable form
    def __str__(self):
        return 'by __str__:%s + i%s' % (self.real, self.imag)	


# Driver program to test above
t = Complex(10, 20)

print (repr(t))
print (str(t))
