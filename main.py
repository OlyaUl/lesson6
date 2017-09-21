#! env bin/python
# codding = utf-8
from abc import ABCMeta,abstractmethod
import os


#! env bin/python
# codding = utf-8
from abc import ABCMeta,abstractmethod
import os


def add(p1, p2, take=False):
    """
    some text
    test text
    ''':param p2:
    :param take:
    :return:'''
    """
    pass
help(add)

class Bot:

    def __init__(self, name):
        self.name = name

    def __getattr__(self,name):
        return "you want {}".format(name)

    def __str__(self):
        return "this is {}".format(self.name)

    def __add__(self, other):
        return str(self) + other

    def __eq__(self, other):
        return self.name == other

    def __lt__(self, other):
        return len(self.name) < len(other.name)

    def __repr__(self):
        return self.name + str(id(self))

    '''def say_hi(self):
        print("My name is {self.name}".format(**locals()))'''

    def _say_stdout(self):
        print("My name is {self.name}".format(**locals()))

    def _say_env(self):
        os.environ["{}_SAYS".format(self.__class__.__name__)]= "a Message"

    def say_hi(self):
        self._say_stdout()


myBot = Bot('test')
myB = Bot('test123')

#print(myBot + "rrrrrr")
lstBot = [(Bot('test' + str(x))) for x in range(1,5)]# [Bot("t1") *2]
lstBot1 = []
print(lstBot)
print(sorted(lstBot))
print("----")
print(lstBot.sort(reverse=True))
print(lstBot)

print(myBot == myB)
print(myBot < myB)


myBot.say_hi()
print(myBot.testttt)
#print(vars(myBot))
#print(vars(Bot))
#print(help(myBot))
#print(dir(myBot))
Bot("ddd").say_hi()
# print(myBot)


class AngryBot(Bot):
    def say_hi(self):
        print("angry test")

a_bot = AngryBot("The bad")
a_bot.say_hi()


class EvilBot(Bot):

    @staticmethod
    def __new__(cls, *args, **kwargs):
        return AngryBot(*args, **kwargs)


evil = EvilBot("ha-ha")
print(evil.say_hi())


class Sayer:
    def say(self, message):
        pass


class HttpHandler(metaclass=ABCMeta):

    @abstractmethod
    def get(self, location):
        raise NotImplementedError()

    @abstractmethod
    def get(self, location, data):
        raise NotImplementedError()


class Memoize(HttpHandler):
    value = "default"
    def get(self, location):
        return self.value

    def post(self,location,data):
        self.value = data


class HomePage(HttpHandler, Sayer):
    def say(self, message):
        print('YOLO' + message)

    def get(self, location):
        return "HomePage"
