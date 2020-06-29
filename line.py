def read(filename):
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		lines = []
		for line in f:
			lines.append(line.strip())
		return lines
def calculation(lines):
	Allen_word_count = 0
	Viki_word_count = 0
	Allen_pic = 0
	Viki_pic = 0
	for item in lines:
		msg = item.split(' ')
		for count in msg[2:]:
			if msg[1] == 'Allen':
				Allen_word_count += len(count)
				if msg[2] == '圖片' and msg[1] == 'Allen':
					Allen_pic += 1
			if msg[1] == 'Viki':
				Viki_word_count += len(count)
				if msg[2] == '圖片' and msg[1] == 'Viki':
					Viki_pic += 1
	print (Allen_word_count)
	print (Viki_word_count)
	print (Allen_pic)
	print (Viki_pic)
def write(filename, lines):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')
def main():
	lines = read ('LINE-viki.txt')
	lines = calculation(lines)
main()





