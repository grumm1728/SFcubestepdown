import math
import csv



def cubestepdown(n):
    s1_0 = int(math.floor(n ** (1 / 3.0))) # find cube root first
    #print("s1_0 = ", s1_0)
    s1 = s1_0
    
    while n % s1 > 0:  # find largest number under cube root that divides n
        s1 = s1 - 1
        #print(s1)
    #print("Side 1 = ",s1)

    s1quot = int(n/s1) # quotient of candies divided by first side
    s2_0 = int(math.floor(math.sqrt(n/s1))) #find square root of remaining product
    #print("s2_0 = ", s2_0)
    s2 = s2_0
    while s1quot % s2 > 0: #find largest number under square root that divides s1quot
        s2 = s2 - 1
        #print(s2)
    #print("Side 2 = ",s2)

    s3 = int(n / (s1 * s2))  #final side
    #print("Side 3 = ",s3)

    SA = 2*(s1*s2 + s1*s3 + s2*s3)  # surface area of a rectangular prism
    #print("\n {",s1,", ",s2,", ",s3,"} with Surface Area =", SA)
    return [n, s1, s2, s3, SA]

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not int(n / i):
                large_divisors.insert(0, int(n / i))
    for divisor in large_divisors:
        yield divisor

def bruteForceMinSA(n):
    divs1 = divisorGenerator(n)
    divlst = list(divs1)
    print(divlst,len(divlst))
    if len(divlst)==2:
        #print("prime")
        return divlst[1]*4+2 # 1 by 1 by p for a prime
    minSA=-1
    for x in divlst:
        q = n/x
        print(n, x, q)
        divlst2 = list(divisorGenerator(q))
        for y in divlst2:
            z = q/y
            if minSA==-1:
                sa = 2*(x*y + x*z + y*z)
                print(n," SA = ",sa)
            else:
                if minSA > sa:
                    minSA = sa
    return minSA


#------------------- Main Code ---------------------

file = open('surfacearea.csv', 'w', newline='')
f = csv.writer(file)
f.writerow(["n","s1","s2","s3","SA","BF SA"])
        
N = int(input("Up to how many candies? max N="))
i=1
while i<=N:
    n=i
    row = cubestepdown(n).append(bruteForceMinSA(n))
    f.writerow(cubestepdown(n))

    #progress indicator
    #if i % int((N/math.floor(math.log(N)))) == 0:  #status indicator scales with N
    #    print("Completed through case ",i)
    i = i+1

file.close()
print("\n===== End =====\n")

