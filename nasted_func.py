def outer(outer_param):
    def inner():
        print("This is inner function")
        print(outer_param)
    inner()


outer("outer arg")