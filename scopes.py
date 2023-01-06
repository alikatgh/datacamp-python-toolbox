# global
gl = 10

def fn1():
    enc = 8

    lc = 5

    def fn2():
        lc = 5
        print(gl)
        print(enc)
    # local
    
    fn2()
    # print(gl)

# fn1(lc)

fn1()

print(gl)

