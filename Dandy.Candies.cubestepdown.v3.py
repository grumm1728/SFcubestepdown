import math

def cubestepdown(n):
    s1_0 = int(math.ceil(n ** (1 / 3.0))) # find cube root first
    minSA=-1
    s1 = s1_0
    while s1>=1:            # doublewhile loops through all divisor s1s of n
        while n % s1 > 0:   # find largest number under cube root that divides n
            s1 = s1 - 1
        s1quot = int(n/s1)  # quotient of candies divided by first side
        s2_0 = int(math.ceil(math.sqrt(n/s1))) #find square root of remaining product
        s2 = s2_0
        while s1quot % s2 > 0: #find largest number under square root that divides s1quot
            s2 = s2 - 1
        s3 = int(n / (s1 * s2))             #final side
        SA = 2*(s1*s2 + s1*s3 + s2*s3)      # surface area of a rectangular prism
        if minSA==-1:
            minSA=SA
            print("{",s1,", ",s2,", ",s3,"} with Surface Area =", SA)
        else:
            if SA<minSA:
                minSA=SA
                print("{",s1,", ",s2,", ",s3,"} with Surface Area =", SA)
        s1 = s1 - 1    
    return minSA

while True:
    n = int(input("N = ? "))
    msa = cubestepdown(n)
    print("==== minSA =", msa," ====")
