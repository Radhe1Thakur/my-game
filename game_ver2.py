import random
def guess_check(point):
	#p = point
	print(point)
	num = int(input('Enter any no. between 0 and 20 : '))
	if num in range(0,21):
		ran = random.randint(0,20)
		dif = abs(num - ran)
		if dif > 15 :
			point += 10
			print('{} is too far from {}.\n\nYou got 10 points.\n'.format(num,ran))
			
		elif dif > 10 :
			point += 20
			print('{} is far from {}.\n\nYou got 20 points.\n'.format(num,ran))
			 
		elif dif > 5 :
			point += 30
			print('{} is stil far from {}.\n\nYou got 30 points.\n'.format(num,ran)) 
		elif dif > 1 :
			point += 40
			print('{} is approximate to {}.\n\nYou got 40 points.\n'.format(num,ran)) 
		elif dif == 0 :
			print('Congratulations !!!!!!! {} matched to {}.\n\nYou got 50 points.\n'.format(num,ran))
			point += 50
		
	else :
		print("{} is out of range !!!!!".format(num))
		print('you lost your one Chance !!!!!')
		#guess_check(point)
	return point


npt = 0
count = 0
while count < 5:
	npt = guess_check(npt)
	count += 1
print('\n\nYour points are {}.'.format(npt))
if npt > 200 :
	print('You are very lucky!!!!!!'.center(80))
elif npt > 170 :
	print('Your luck is good!!!!!'.center(80))
elif npt <= 170:
	print('Sorry luck is not supporting You!!!!!'.center(100))
