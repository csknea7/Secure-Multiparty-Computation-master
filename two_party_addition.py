from Util import Util
util = Util()
import random

x = 24
y = 36
z = 5
prime = util.closest_large_prime_finder(x) if x > y else util.closest_large_prime_finder(y)
print('Prime: ' + str(prime))

x_a, x_b = util.two_party_secret_share(x, prime)
y_a, y_b = util.two_party_secret_share(y, prime)
z_a, z_b = util.two_party_secret_share(z, prime)

s_a = x_a + y_a
s_b = x_b + y_b
s_z = z_a + z_b
s = (s_a + s_b + s_z)
print('Result of secure computation: ' + str(s))
print('Result of simple addition: ' + str(x+y+z))