def line_generator(number = 3, message="Line"):
    for x in range(1,int(number)+1):
        print(message,x)

line_generator()
line_generator(2,"Snake")
