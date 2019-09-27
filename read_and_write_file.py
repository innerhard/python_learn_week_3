with open('referat.txt', 'r', encoding='utf-8') as myfile:
    content = myfile.read()
    content = content.replace('.', '!')
    print(len(content))
    a = 0
for counted in content.split(' '):
    a += 1

print(a)
content = content.replace('.', '!')
with open('referat2.txt', 'w', encoding='utf-8') as myfile2:
    myfile2.write(content)
