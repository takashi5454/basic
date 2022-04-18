#encapsulation
def casino_entrance(age,min_age=21):
    if age < min_age:
        print(f"{min_age}歳未満お断り")
        return

    def inner_casio_entrance():
        print("ようこそカジノへ")

    inner_casio_entrance()


casino_entrance(18)