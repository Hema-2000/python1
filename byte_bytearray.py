x=['pen','book','pencil'];
y=[1,2,3,4]
z=bytes(y)
print(z)  #b'\x01\x02\x03\x04'
#print(bytes(x)) # TypeError: 'str' object cannot be interpreted as an integer
print(bytearray(y))  #bytearray(b'\x01\x02\x03\x04')

