import math
teamNumber = 27
mass = float(input("Enter the mass of your patient in Kg: "))
bodyWeight = mass*9.8                  
#(52.5*9.8)
#units --> Newtons
outerDia = 17
#units --> mm
canalDiameter =9.5
#units --> mm
canalOffset = 39
#units --> mm
modulusBone = 30
#corticol bone
#ultTenStrength = float(input("Enter the ultimate tensile strength of the chosen material in MPa: "))      TO BE PLACED INSIDE SP1
#490
#units --> MPa
#The maximum stress a material can stand before it breaks 
#material is a Titanium alloy --> Ti-29Nb-13Ta-4.6Zr
#modulusImplant = 47 GPa

def subprogram3():
    modulusImplant = float(input("Enter the elastic modulus of the implant material in GPa: "))
    force = 30*bodyWeight
    #the force applied is assumed to be 30 times the bodyweight of the patient
    cross_secArea = math.pi/4 *(outerDia**2 - canalDiameter**2)
    stress_compression = force/cross_secArea
    stressReduc = stress_compression * ((2*modulusBone)/(modulusBone + modulusImplant))**(1/2)
    Eratio = (modulusImplant/modulusBone)**(1/2)
    #print ("reduced compressive stress", stressReduc)
    x = 0
    stressFail = 0
    yrsFail = 0
    #the above variable are assigned a value of zero so I can change their value each time the loop reiterates
    while (x<100):
        x+= 0.01
    #the value of years is going up by 0.01 each time the loop iterates, equivalent to saying x = x + 0.01
        if (round(compStrength(x),4) <(stressReduc)):
    #the stressFail will occur at the first value of compStrength that drops below the value of stressReduc
            stressFail = round(compStrength(x),4)
    #the function compStrength() is called and values of x are passed through it until it yields a value that is less than stressReduc
            yrsFail = round(x,4)
            break
    #once the condition for the "if" statement is satisfied, the loop breaks out and proceeds to the next line outside the loop
    print ("The number of years post-implantation before there is a risk of femoral fracture is ", yrsFail, "years")
    print ("The compressive stress on the bone that corresponds to failure is ", round(stressFail,4), "MPa" )
def compStrength (x):
    return (0.001*x**2 - 3.437*x*(1.251665557) + 181.72)
#compressive strength of bone after "x" number of years is placed in a separate function to ease the use of the while loop in subprogram3()
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
