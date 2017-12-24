"""
b -> c is the range we are looking at
we are only checking each 17th number

# "set b 84",
# "set c b",
# "jnz a 2",
# "jnz 1 5",
# "mul b 100",
# "sub b -100000",
# "set c b",
# "sub c -17000",
...
# # "sub b -17",

if d*e == b then we'll increment h which is for values
when d or e isn't b
# ### "set g d",
# ### "mul g e",
# ### "sub g b",
# ### "jnz g 2",
# ### "set f 0",
...
# # "jnz f 2",
# # "sub h -1",
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n%i == 0 or (n%(i + 2)) == 0:
            return False
        i += 6
    return True

b = 108400
c = 125400
h = 0
for i in range(b, c+1, 17):
    if not is_prime(i):
        h = h + 1 

print(h)
