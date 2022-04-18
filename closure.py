#clousure
def compute_square(num):
    return num * num

#closure 状態をキープした関数
#静的状態　1度作れば関数の状態を変えない
def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power


power4 = power(4)
print(power4(2))

#状態が動的
def average():
    nums = []

    def inner_average(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return inner_average


average_nums = average()
print(average_nums(5))
