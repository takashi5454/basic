def outer(outer_param):
    def inner():
        print("This is inner")
        print(outer_param)
    inner()

outer("outer_param")