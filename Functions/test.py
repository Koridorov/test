def myFunc(*args, **kwargs):
    for x in args:
        print(x)
    for x in kwargs:
        print(x)

myFunc("Dani", "Misho", "Stoyan", dani = "Dani1", misho="Misho1", stoyan="Stoyan1")