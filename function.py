#関数ビルトイン関数
#print()
#len()
#input()

#℉から摂氏に変換
fahrenheit = 72
#celsius = (fahrenheit-32) * 5/9
#print(celsius)

#関数の定義
def fahrenheit_to_celsius(x):
    y = (x - 32) * 5 / 9
    return y


celsius=fahrenheit_to_celsius(fahrenheit)
print(celsius)


