# 1 Example № 21899

from ipaddress import *

adr = ip_network('98.81.154.195/255.252.0.0', 0)

print(adr[-2])

# 2 Example № 21412

from ipaddress import *

adr = ip_network('143.168.72.213/255.255.255.240', 0)

print(adr[-2])

# 3 Example № 21708

from ipaddress import *

adr = ip_network('11.92.135.56/255.224.0.0', 0)

print(adr[-2])

# 4 Example № 20902

from ipaddress import *

net = ip_network('172.16.80.0/255.255.248.0')

c = 0

for n in net:
    b = bin(int(n))[2:]
    if b.count('1') % 2 == 0:
        c += 1

print(c)

# 5 Example № 20807
from ipaddress import *

net = ip_network('172.16.192.0/255.255.192.0')

c = 0

for n in net:
    b = bin(int(n))[2:]
    if b.count('1') % 5 != 0:
        c += 1
print(c)