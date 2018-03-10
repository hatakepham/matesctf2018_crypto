import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator
import sys
from binascii import *
s = "cab0130b5edf8a983ae7acc1f3b0e804c73e14aa28bc44e7766478a30f23117ddd12217b4744fafafde645d396e9884b1cb6ebe94312a3983699751776dc50f"
n = int(6532711069652802445231009356214576273040140006075954728375486143178606084660045267455535660750621847610884730993796797913937017523341718065866575050588271)
e = int(30387964909*19477723457*146745640918967*437938955227339*473009241139151*47793607006385055646348379*7351391211030124529592567637834769276136765421608165102101253973)
c = int(s,16)


def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d

# TEST functions

def test_hack_RSA():
    print("Testing Wiener Attack")
    print(" e = " );
    print (e)
    print(" n = " );
    print(n)
    print("d = ")
    print(hack_RSA(e, n))    
    print("m =")
    m = pow ( c , hack_RSA(e, n) , n )
    print (type(m))
    print (hex(m))
    
if __name__ == "__main__":
    #test_is_perfect_square()
    #print("-------------------------")
    test_hack_RSA()

