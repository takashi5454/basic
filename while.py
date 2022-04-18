#while
#count=0
#while count < 10:
 #   print(count)
  #  count += 1
#braekとcontinue
age = int(input("何歳ですか？"))
casino_age=18
game_text = """プレイするゲームを選択してください
1: ルーレット
2: ブラックジャック
3: ポーカー
"""

if age >= casino_age:
    print("どうぞお入りください")
    while True:
        game = input(game_text)
        if game == '1':
             print("あなたはルーレットを選びました")
             break
        elif game == '2':
             print("あなたはブラックジャックを選びました")
             break
        elif game == '3':
             print("あなたはポーカーを選びました")
             break
        else:
             print("1～3を選んでください")
else:
    print("18才未満は入れません")
