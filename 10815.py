import re
import sys

def parse(line):
	line = re.sub(r'[^a-zA-Z]', ' ', line)
	words = [word.lower() for word in line.split(' ')] 

	return set(words)

def main():
	ans = set()
	for line in sys.stdin.readline():
		ans.update(parse(line))
	if('' in ans):
		ans.remove('')
	for word in sorted(ans):
		print(word)

main()
    
