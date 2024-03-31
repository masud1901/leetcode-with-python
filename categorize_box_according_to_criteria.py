length = 1000
width = 35
height = 700
mass = 300
# Output: "Heavy"

length = 3223
width = 1271
height = 2418
mass = 749

limitBulky1 = int(10e3)
limitBulky2 = int(10e8)
limitHeavy = 100

checkBulky = False
checkHeavy = False

if length >= limitBulky1 or width >= limitBulky1 or height >= limitBulky1:
    checkBulky = True


volume = length * width * height

if volume >= limitBulky2:
    checkBulky = True

if mass >= limitHeavy:
    checkHeavy = True

if checkBulky and checkHeavy:
    print("Both")
if checkHeavy != True and checkBulky:
    print("Bulky")
if checkHeavy and checkBulky != True:
    print("Heavy")
else:
    print("Neither")

