age = int(input("Enter your age: "))
height = int(input("Enter your height: "))
statue = int(input("Are you a thin-boned or broad-boned statue? : "))
if age <= 40:
    weight = height - 110
else:
    weight = height - 100

if statue == 1:
    weight *= 0.9
elif statue == 2:
    weight *= 1.1

print("Your ideal weight is", weight)
