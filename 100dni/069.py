#dzień 69
from datetime import datetime

#x = datetime.datetime.now()

#print(x)

#Tworzysz dwa obiekty  daty

date1 = datetime(2021,10,20)
date2 = datetime(2021,10,10)

diff = date1 - date2

print(diff.days)


#Proste zadanko. Wylicz, ile dni już żyjesz :)))


dateBirth = datetime(1999,1,29)
now = datetime.now()

diff1 = now - dateBirth

print(diff1)
