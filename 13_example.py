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
