class Point:
    a = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def instance_func(self):
        print('인스턴스 메소드')

    @classmethod
    def class_method(cls):
        print('클래스 메소드: {}'.format(cls.a))

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


"""
클래스 메소드는 클래스 생성자 오버로딩, 클래스 변수 수정 메소드 등을 추가할 때 사용한다...
"""


class MomClass:
    name = 'mom'

    @staticmethod
    def get_name_static():
        return MomClass.name

    @classmethod
    def get_name_class(cls):
        return cls.name

    @classmethod
    def set_name_class(cls, name):
        cls.name = name


class SonClass(MomClass):
    name = 'son'


class Rainbow:
    def __init__(self):
        self.COLORS = ['빨', '주', '노', '초', '파', '남', '보']
        self._colors = self.COLORS

    @property
    def colors(self):
        print("getter 실행!")
        return self._colors

    @colors.setter
    def colors(self, color_set_list):
        print("setter 실행!")
        self._colors = [color for color in color_set_list if color in self.COLORS]