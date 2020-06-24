#04 -

lista = []
txt = ('''The Python Software Foundation and the global Python community
         welcome and encourage participation by everyone.
         Our community is based on mutual respect, tolerance,
         and encouragement, and we are working to help each
         other live up to these principles.
         We want our community to be more diverse:
         whoever you are, and whatever your background, we welcome you.''')
txt = txt.lower()
txt = txt.replace('.', ' ').replace(',',' ').replace(':', ' ')
lista = txt.split()
for i in lista:
    if i[0] in 'python' or i[-1] in 'python':
        print(i