def required_area_of_steel(Mu, fck, fy, b, d):
    gamma_c = 1.5
    gamma_s = 1.15

    fcd = fck / gamma_c
    fyd = fy / gamma_s

    xu = (0.87 * fy * d) / (0.36 * fcd + 0.87 * fy)
    
    if xu > d:
        xu = d

    MR = 0.36 * fcd * b * xu * (d - 0.42 * xu)

    Ast = Mu * 10**6 / (0.87 * fyd * (d - 0.42 * xu))

    return Ast

# User input section
try:
    Mu = float(input("Enter the ultimate bending moment (in kNm): "))
    fck = float(input("Enter the characteristic compressive strength of concrete (in MPa): "))
    fy = float(input("Enter the yield strength of steel (in MPa): "))
    b = float(input("Enter the width of the beam (in mm): "))
    d = float(input("Enter the effective depth of the beam (in mm): "))

    Ast = required_area_of_steel(Mu, fck, fy, b, d)
    print("The required area of steel reinforcement is:", round(Ast, 2), "mm^2")
except ValueError:
    print("Please enter valid numerical values.")
