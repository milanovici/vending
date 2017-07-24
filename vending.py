
def getChange(inserted, price): # inserted=1.9 price=1.2
	deno = [100, 50, 25, 10, 5, 1] # 2.35 % 1 -> Error
	retVal = [0 for _ in deno]
	inserted *= 100
	price *= 100
	inserted -= price
	for index, amount in enumerate(deno):
		retVal[index] = int(inserted // amount) # floor devision
		inserted %= amount # residue
	return retVal[::-1]

print(getChange(inserted=5, price=.99))