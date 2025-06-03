# 1 То же, что и lru, иногда lru может не сработать хзлол

f= {} #Dict
for n in range(10, 48000): #Perebor
    if n < 20: #Uslovie
        f[n] = n #Uslovie
    if n >= 20: #Uslovie
        f[n] = (n - 6) * f[n - 7] #Uslovie
print((f[47872] - 290 * f[47865])/f[47858]) #Uslovie

# 2 Sposob IMPORTANT

from functools import lru_cache # Import
@lru_cache(None) #Temp

def ff(nn): #Init func
    if nn < 20: return nn #Uslovie
    if nn >= 20: return (nn - 6) * ff(nn - 7) #Uslovie

for p in range(1, 48000): #For lru
    ff(p)
print((ff(47872) - 290 * ff(47865)) / ff(47858)) #Print