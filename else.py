fruits = ['apple','peach','grapes','banana']

#for fruit in fruits:
#    choise = input(f"あなたの探しているフルーツは{fruit}ですか？ y/n:")
    #if choise == "y":
  #     print("見つかってよかった")
  #     break
 #   else:
#       print("そうですか")
#else:
 #   print("ループが回り切りました")

balance = 1000
game_price = 200
while balance >= game_price:
    choice = input(f"1回{game_price}円のゲームに参加しまか？(残高:{balance}円)(y/n?):")
    if choice == "y":
        balance -= game_price
    elif choice == "n":
       print("また遊びましょう")
       break
    else:
       print("yかnで答えてください")
else:
    print(f"もうお金ない")