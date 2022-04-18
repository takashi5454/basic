#mutable 変更可能なオブジェクト list,dict.set
fruits = ['apple','peach','banana']
print(f"fruitsのIDは{id(fruits)}")
fruits.append('lemon')
print(fruits)
print(f"fruitsのIDは{id(fruits)}")
#immutable 変更不可能なオブジェクトint float str bool tuple
fruit='apple'
#練習
text = ""
for i in range(1,11):
    if i == 1:
        text += str(i)
    else:
        text += '-' + str(i)
print(text)

text_list = []
for i in range(1,11):
    text_list.append(str(i))
text = '-'.join(text_list)
print(text)