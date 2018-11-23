import math
teamNumber = 27
bodyWeight = (52.5*9.8)
#units --> Newtons
outerDia = 17
#units --> mm
canalDiameter =9.5
#units --> mm
canalOffset = 39
#units --> mm
modulusBone = 30
ultTenStrength = 490
#units --> MPa
#The maximum stress a material can stand before it breaks 
#material is a Titanium alloy --> Ti-29Nb-13Ta-4.6Zr
modulusImplant = 47
d = 0
#units = GPa
#stemDia = 
def subprogram1():
    #calculates the minimum allowable implant stem diameter for a combined loading scenario
    stemDia = canalDiameter
    force = 3.5*bodyWeight  
    result = ultTenStrength*(d**3)+ (4/math.pi)* force * d - (0.5*force*canalOffset*(64/math.pi))
    print ("The patients bodyweight is ", bodyWeight, "N")
    print ("The diameter of the canal is ", canalDiameter, "mm" '\n')
    print ("The Ultimate Tensile Strength is ", ultTenStrength)
    return result
def loop():
    while True:
        answer = subprogram1()
        if (answer) == 0:
            minStemDia = d
            break
        d+=0.001
    print ("The minimum allowable implant stem diameter is ", minStemDia)
    print ("The applied tensile stress that corresponds to the minimum allowable stem diameter is ", appTenStress)
def main():
    home = ("HOME \n")
    print (home.center(70))
    exit = False
    while (exit==False):
        print (" 1. Subprogram 1 \n 2. Subprogram 2 \n 3. Subprogram 3 \n 4. Exit from program \n")
        choice = input("Please choose one of the following options by indicating the number that corresponds to your choice: ")
        if choice == ("1"):
            subprogram1()
            loop()
            #a parameter must be passed in the paranthesis
        elif choice == ("2"):
            subprogram2()
            #a parameter must be passed in the paranthesis
        elif choice == ("3"):
            subprogram3()
            #a parameter must be passed in the paranthesis
        elif choice ==("4"):
            exit = True
            print ("You have exited from the program.")
    
    print ("Thank you for using the program")
main()
