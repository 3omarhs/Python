Y = 2021
M = 10
D = 29
JDN = (1461 * (Y + 4800 + (M - 14)/12))/4 +(367 * (M - 2 - 12 * ((M - 14)/12)))/12 - (3 * ((Y + 4900 + (M - 14)/12)/100))/4 + D - 32075
print(JDN)
JDN  = 367 * Y - (7 * (Y + 5001 + (M - 9)/7))/4 + (275 * M)/9 + D + 1729777
print(JDN)
#JDN = 367 × Y − (7 × (Y + 5001 + (M − 9)/7))/4 + (275 × M)/9 + D + 1729777
