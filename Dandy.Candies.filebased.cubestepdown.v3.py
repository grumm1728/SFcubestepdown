import math
import csv

def cubestepdown(n):
    s1_0 = int(math.ceil(n ** (1 / 3.0))) # find cube root first
    minSA=-1
    s1 = s1_0
    count = 0               # how many cases did we test?
    while s1>=1:            # doublewhile loops through all divisor s1s of n
        while n % s1 > 0:   # find largest number under cube root that divides n
            s1 = s1 - 1
        s1quot = int(n/s1)  # quotient of candies divided by first side
        s2_0 = int(math.ceil(math.sqrt(n/s1))) #find square root of remaining product
        s2 = s2_0
        while s1quot % s2 > 0: #find number closest to square root that divides s1quot
            s2 = s2 - 1
        s3 = int(n / (s1 * s2))             #final side
        SA = 2*(s1*s2 + s1*s3 + s2*s3)      # surface area of a rectangular prism
        if minSA==-1:
            count=count+1
            minSA=SA
            print(n, " : {",s1,", ",s2,", ",s3,"} with Surface Area =", SA) #progress indicator
            x, y, z = s1, s2, s3
        else:
            if SA<minSA:
                count=count+1
                minSA=SA
                print(n, " : {",s1,", ",s2,", ",s3,"} with Surface Area =", SA) #progress indicator
                x, y, z = s1, s2, s3
        s1 = s1 - 1   
    return [n,count,x,y,z,minSA]




#------------------- Main Routine ---------------------

file = open('surfacearea.csv', 'w', newline='')
f = csv.writer(file)
f.writerow(["n","count","s1","s2","s3","SA"])

i = int(input("Starting with how many? min n="))
N = int(input("Ending with how many? max n="))
seq = []
while i<=N:
    n=i
    row = cubestepdown(n)
    f.writerow(row)
    seq.append(row[4])   #sequence of minSAs only
    #progress indicator if not printing all lines
    #if i % int((N/math.floor(math.log(N)))) == 0:  #status indicator scales with N
    #    print("Completed through case ",i)
    i = i+1

f.writerow(seq)
file.close()
print("\n===== End =====\n")

