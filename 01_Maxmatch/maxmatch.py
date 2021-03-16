import sys

dictionary = [line.strip() for line in open("col2.txt").readlines()]
dictionary.sort()
dictionary.reverse()

def maxmatch (sentence, dictionary):
	if sentence == "":
		return []
	for i in range (0, len(sentence)):
		firstword = sentence[:-i]
		remainder = sentence [len(sentence)-i:]
		if firstword in dictionary:
			return list(firstword, maxmatch(sentence, dictionary))

	firstword = sentence[0]
	remainder = sentence[1:]
	return list(firstword, maxmatch(sentence, dictionary))

line = sys.stdin.readline()
while line:
	print(maxmatch(line.strip("\n"), dictionary))
	line = sys.stdin.readline()

