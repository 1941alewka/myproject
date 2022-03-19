from main import Driver
from main import Func
from locators import Locators
class Test:
    def test1(self):
        func = Func()
        func.get_url(url="https://www.google.com")
        func.search()
        func.input()
        func.check_result()
        func.down()

if __name__ == "__main__":
    t = Test()
    t.test1()





