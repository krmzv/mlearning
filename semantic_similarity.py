import re, math
from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):

	intersection = set(vec1.keys()) & set(vec1.keys())
	numerator = sum([vec1[x] * vec2[x] for x in intersection])

	sum1 = sum([vec1[x]**2 for x in vec1.keys()])
	sum2 = sum([vec2[x]**2 for x in vec2.keys()])

	denominator = math.sqrt(sum1) * math.sqrt(sum2)

	if not denominator:
		return 0.0
	else:
		patka = float(numerator)
		nikako = patka/denominator
		return nikako
		


def text_to_vector(text):
	word = WORD.findall(text)
	return Counter(word)

text1 = 'sta te ne ubije to te ojaca'
text2 = 'nije me ubilo ali me je ojacalo'

vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)

cosine = get_cosine(vector1, vector2)

print (cosine)


