#input()
age = int(input("何歳ですか？"))
casino_age=18
game_text = """プレイするゲームを選択してください
1: ルーレット
2: ブラックジャック
3: ポーカー
"""

if age >= casino_age:
    print("どうぞお入りください")
    game = input(game_text)
    if game == '1':
        print("あなたはルーレットを選びました")
    elif game == '2':
        print("あなたはブラックジャックを選びました")
    elif game == '3':
        print("あなたはポーカーを選びました")
    else:
        print("1～3を選んでください")
else:
    print("18才未満は入れません")
