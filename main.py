# print("hello world")

def main():
	path = "books/frankenstein.txt"
	with open(path) as f:
		file_contents = f.read()
	# print(file_contents)
	words = file_contents.split()
	# print(type(words))
	print(f'--- Begin report of {path} ---')
	print(f"{len(words)} words found in the document")
	print('\n')
	char_count = count_characters()
	character_report(char_count)

def count_characters():
	with open("books/frankenstein.txt") as f:
		 file_contents = f.read()
	words = ''.join(file_contents).lower()
	#print(type(words))
	char_count = {}
	for char in words:
		if char.isalpha():
			if char in char_count:
				char_count[char] += 1
			else: char_count[char] = 1
	#print(char_count)
	return char_count

def character_report(dict):
	dict = {k:v for k,v in sorted(dict.items(), key = lambda item: item[1], reverse = True)}
	for k,v in dict.items():
		print(f'The \'{k}\' character was found {v} times')
	print('--- End report ---')
main()
