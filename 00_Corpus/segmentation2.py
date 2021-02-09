import sys
line = sys.stdin.readline()
while line != '':
	for token in line.strip().split(' '):
		if token == ': \n':
			sys.stdout.write(token+'\n')
			continue
		if token.strip() == '':
                        continue
		if token[-1] in '!?':
			sys.stdout.write(token + '\n')
		elif token[-1] == '.':
			if token in ['etc.', 'i.e.', 'e.g.','Dr.','Ms.','Mrs.','Mr.','St.','...']:
				sys.stdout.write(token+' ')
			else:
				sys.stdout.write(token+'\n')
		else:
			sys.stdout.write(token +' ')
	sys.stdout.write('\n')

	line = sys.stdin.readline()

#Remmeber 2D array double check stackoverflow
