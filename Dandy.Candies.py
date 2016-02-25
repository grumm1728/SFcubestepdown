import math

while 1==1:
    #input
    n = input("How many candies? n=")
    n = int(n)
    
    s1_0 = int(math.floor(n ** (1 / 3.0)))
    print("s1_0 = ", s1_0)
    
    s1 = s1_0
    
    while n % s1 > 0:
        s1 = s1 - 1
        print(s1)
    print("Side 1 = ",s1)

    s1quot = int(n/s1) # quotient of candies divided by first side

    s2_0 = int(math.floor(math.sqrt(n/s1)))
    print("s2_0 = ", s2_0)

    s2 = s2_0
    
    while s1quot % s2 > 0:
        s2 = s2 - 1
        print(s2)
    print("Side 2 = ",s2)

    s3 = int(n / (s1 * s2))

    print("Side 3 = ",s3)

    SA = 2*(s1*s2 + s1*s3 + s2*s3)
    print("\n {",s1,", ",s2,", ",s3,"} with Surface Area =", SA)

print("\n===== End =====\n")
