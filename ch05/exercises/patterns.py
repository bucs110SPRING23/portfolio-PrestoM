def star_pyramid(rows):
    for i in range(1, rows+1):
        print("*"*i)

def rstar_pyramid(rows):
    for i in range(rows, 0, -1):
        print("*"*i)

star_pyramid(8)
print()
rstar_pyramid(7)