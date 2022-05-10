import MeCab
m = MeCab.Tagger("-Ochasen")
nouns = m.parse('学生ID').splitlines()
nouns.pop(-1)
print(nouns)
print(nouns[0].split())
