def get_answer_mask(text: str) -> list[int]:
	word_1, word_2 = text.split(', ')
	result = []
	unique = set()

	for letter_1, letter_2 in zip(word_1, word_2):
		if letter_1 == letter_2:
			result.append('1')
		elif letter_1 in word_2:
			if letter_1 in unique:
				result.append('-1')
			else:
				result.append('0')
		else:
			result.append('-1')
		unique.add(letter_1)

	return ', '.join(result)


if __name__ == "__main__":
	# Необходимо преобразовать список в строку перед выводом.
	result = get_answer_mask('АГАВА, ПАЛКА')
	print(result)
	print(result == '0, -1, -1, -1, 1')