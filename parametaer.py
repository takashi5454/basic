#def func(first,second,third):
 #   print(f"first:{first},second:{second},third:{third}")
#argument<-> parametar
#func("1","2","3")
#print("heloo" , "world")
def get_average(*args):
    num = len(args)
    print(num)
    if num == 0:
        return 0
    total = sum(args)
    return total/num


average = get_average(1,2,3,4,5)
print(average)

#**kwargs ディクショナリ{}
def kwargs_func(**kwargs):
    param1 = kwargs.get('param1',1)
    param2 = kwargs.get('param2',2)
    param3 = kwargs.get('param3',3)
    print(f"param1:{param1},param2:{param2},param3:{param3}")


kwargs_func(param1=10, param2=11, param3=12)