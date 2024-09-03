def testDeco(func):
    def wapper():
        print('Je vais bien')
        func()
        print("AAAHH j'ai peur")
    return wapper

@testDeco
def boo():
    print("BOO!")

boo()