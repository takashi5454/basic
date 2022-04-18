# def menu(wine,entree,dessert):
#     return {'wine':wine , 'entree': entree,'dessert':dessert}
#
# x=menu('beef','yes','ice')
# print(x)

def edit_story(words,func):
    for word in words:
        print(func(word))

stairs = ['cat','dog']

def end(word):
    return word

print(edit_story(stairs,end))