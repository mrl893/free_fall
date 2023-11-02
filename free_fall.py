from math import sqrt



# variable
GRAVITY = 9.8

# funct 
def main()->str:
    d = float(input("Height from which the object is dropped (in meters): "))
    vf = sqrt(2* GRAVITY * d)
    return f"It will hit the groud at %.2f m/s. " % vf
if __name__ == "__main__":
    print(main())
    
