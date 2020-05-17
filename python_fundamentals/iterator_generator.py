"""
Iterable 객체에서 실제 Iteration을 실행하는 것은 iterator로서,
iterator는 next 메서드를 사용하여 다음 요소(element)를 가져온다.

만약 더이상 next 요소가 없으면 StopIteration Exception을 발생시킨다.

list, set과 같은 iterable한 collection은 for문을 돌리면 내부에서 임시로 iterator로 자동 변환하여 진행한다.
"""


class MyCollection:
    def __init__(self):
        self.size = 10
        self.data = list(range(self.size))

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= self.size:
            raise StopIteration
        n = self.data[self.index]
        self.index += 1
        return n


a = MyCollection()
for e in a:
    print(e)


"""
Generator는 Iterator의 특수한 한 형태이다.
Generator 함수(Generator function)는 함수 안에 yield를 사용하여 데이터를 하나씩 리턴하는 함수이다.
Generator 함수가 처음 호출되면, 그 함수 실행 중 처음으로 만나는 yield에서 값을 리턴한다.
Generator 함수가 다시 호출되면, 직전에 실행되었던 yield문 다음부터 다음 yield문을 만날 때까지 문장들을 실행하게 된다.
이러한 Generator 함수를 변수에 할당하면 그 변수는 Generator 클래스 객체가 된다.
"""


def gen():
    yield 1
    yield 2
    yield 3


g = gen()
print(type(g))
n = next(gen())
print(n)
n = next(gen())
print(n)
n = next(gen())
print(n)

for x in gen():
    print(x)

"""
iterator와 generator의 차이:

list, set과 같은 컬렉션에 대ㅛ한 iterator는 해당 컬렉션이 이미 모든 값을 가지고 있는 경우이지만,
generator는 모든 데이터를 갖지 않은 상태에서 yield에 의해 하나씩만 데이터를 만들어 가져온다는 차이점이 있다.

generator는 이럴 때 사용한다.
1. 데이터가 무제한이어서 모든 데이터를 리턴할 수 없는 경우
2. 데이터가 대량이어서 일부씩 처리하는 것이 필요하는 경우
3. 모든 데이터를 미리 계산하면 속도가 느려서 on demand로 처리하는 것이 좋은 경우 등등...
"""
