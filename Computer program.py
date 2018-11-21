import math
teamNumber = 27
bodyWeight = (52.5*9.8)
#units --> Newtons
outerDia =  17
#units --> mm
canalDiameter =9.5
#units --> mm
canalOffset = 39
#units --> mm
modulusBone = 30
#ultTenStrength =
#The maximum stress a material can stand before it breaks 
#material is a Titanium alloy --> Ti-29Nb-13Ta-4.6Zr
modulusImplant = 47 
#units = GPa
#stemDia = 
def subprogram1():
    #calculates the minimum allowable implant stem diameter for a combined loading scenario
    #stemDia = canalDiameter
    stemDia = 9.5
    cross_area = (math.pi / 4 )*(outerDia**2 - canalDiameter**2)
    force = 3.5 * bodyWeight
    axial_stress = force/cross_area
    bending_moment = (math.pi / 64) *(stemDia)**4
    moment = force * canalOffset
    bending_stress = (moment * 0.5* stemDia)/bending_moment
    appTenStress = axial_stress + bending_stress 
    ultTenStrength = 
    minStemDia = 
    print ("The patients bodyweight is ", bodyWeight, "N")
    print ("The diameter of the canal is ", canalDiameter, "mm" '\n')
    print ("The Ultimate Tensile Strength is ", ultTenStrength)
    print ("The minimum allowable implant stem diameter is ", minStemDia)
    print ("The applied tensile stress that corresponds to the minimum allowable stem diameter is ", appTenStress)
    
#def subprogram2():


#def subprogram3():
    
    
    
def main():
    home = ("HOME \n")
    print (home.center(70))
    exit = False
    while (exit==False):
        print (" 1. Subprogram 1 \n 2. Subprogram 2 \n 3. Subprogram 3 \n 4. Exit from program \n")
        choice = input("Please choose one of the following options by indicating the number that corresponds to your choice: ")
        if choice == ("1"):
            subprogram1()
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


