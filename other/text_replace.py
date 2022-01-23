import re

# sentences = input().split('.')
sentences = 'I like to play video games and to ride in cars. I also enjoy table tennis, basketball, and hockey. ' \
            'Additionally, when bored, I sometimes like to play football, though I rarely do that anymore.'.split('.')
sentences = [i + '.' for i in sentences[:-1]]

# words_to_replace = input()
words_to_replace = '''To
                    In
                    Table
                    Additionally
                    Though'''
words_to_replace = words_to_replace.split()

print(sentences)
print(words_to_replace)

res = []
for num, s in enumerate(sentences):
    sent = ''
    words = []
    for r in words_to_replace:
        for _ in range(len(re.findall(r.lower(), s.lower()))):
            i = re.search(r.lower(), s.lower())
            s = list(s)
            s[i.span()[0]:i.span()[1]] = '[..]'
            s = ''.join(s)
            # sentences[num] = s
            words.append([r, i.span()[0]])
    sent = s.strip()
    words.sort(key=lambda words: words[1])
    words = [i[0].lower() for i in words]
    res.append([sent, words])

print('\n')
for i in res:
    print(i)
