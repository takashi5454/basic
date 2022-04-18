#数値型(numeric):integer,float,complex

#int (inntger,整数)-3,-2,-1,0
print(type(-100))

#float(浮動小数点)
print(type(0.1))
print(0.1 + 0.1 + 0.1)

#Numeric Operator(数値演算子)
#四則演算
print(1+0.4)
print(5 * 6 - 3 / 6)
print(5*6 - 3 / 6)

result = 1+1.0
print(result)

#その他の演算
#floor division
print(14//3)
print(14%3)
print(2**3)

hit_point = 100
attack_point = 40.3
remain = hit_point - attack_point
print(f"remain hit point is{remain}")

# augmented assigment
a = 1
a +=1
print(a)
