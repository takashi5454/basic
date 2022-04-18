fruits = ['apple','peach','grapes','banana']
print('apple' in fruits)

list = input("好きなフルーツを入力してください")



if list in fruits:
    print("{}ですね、差し上げますよ".format(list))
    fruits.remove(list)
    print(fruits)
else:
    print("{}ですね、仕入れました".format(list))
    fruits.append(list)
    print(fruits)
