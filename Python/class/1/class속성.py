# class Person:
#     def __init__(self, name, age, address):
#         self.hello = 'hi'
#         self.name = name
#         self.age = age
#         self.address = address

#     def greeting(self):
#         print('{} 저는 {} 입니다'.format(self.hello, self.name))


# maria = Person('kim', 28, 'gwanak')
# maria.greeting()

# 비공개클래스

class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet    # 변수 앞에 __를 붙여서 비공개 속성으로 만듦

    def pay(self, amout):
        self.__wallet -= amout
        print('{}원 남음'.format(self.__wallet))


maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)
