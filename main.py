#! env bin/python
# codding = utf-8
from abc import ABCMeta,abstractmethod
import os
from functools import total_ordering, lru_cache

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

@lru_cache(3)
def fib1(n):
    print("enter {}".format(n))
    if n < 2:
        return n
    return fib1(n-1) + fib1(n-2)

#n1 = int(input())
#print(fib1(n1))

print("........")


class SetGet(object):

    def __set__(self, instance, value):
        instance.dummy = value
        self.sth = 0
        # return value

    def __get__(self, instance, owner):
        return instance.dummy


@total_ordering
class Bot:

    property = SetGet()
    property1 = SetGet()

    def __init__(self, name):
        self.name = name

    def __getattr__(self, name):
        return "you want {}".format(name)

    def __str__(self):
        return "this is {}".format(self.name)

    def __add__(self, other):
        return str(self) + other

    #@total_ordering
    def __eq__(self, other):
        return self.name == other

    #@total_ordering
    def __lt__(self, other):
        return len(self.name) < len(other.name)

    def __repr__(self):
        return self.name + str(id(self))

    def _say_stdout(self):
        print("My name is {self.name}".format(**locals()))

    def _say_env(self):
        os.environ["{}_SAYS".format(self.__class__.__name__)]= "a Message"

    def say_hi(self):
        self._say_stdout()


myBot = Bot('test')
myB = Bot('test123')
bot = Bot('newtest')
bot.property = "Something"
bot.property1 = "Something123"

print(bot.property)
print(bot.property1)

bot.__dict__['property'] = 'a property'
print(vars(Bot))
# print (Bot.property.dummy = bot.property)

# print(myBot + "rrrrrr")
# lstBot = [(Bot('test' + str(x))) for x in range(1,5)]# [Bot("t1") *2]
# lstBot1 = []
# print(lstBot)
# print(sorted(lstBot))
# print("----")
# print(lstBot.sort(reverse=True))
# print(lstBot)

# print(myBot == myB)
# print(myBot != myB)

# print(myBot > myB)
# print(myBot <= myB)







#myBot.say_hi()
#print(myBot.testttt)
#print(vars(myBot))
#print(vars(Bot))
#print(help(myBot))
#print(dir(myBot))
#Bot("ddd").say_hi()
# print(myBot)
'''print("............")


def logged(func):
    def wrapped(*args, **kwargs):
        print('entered into:', func.__name__)
        result = func(*args, **kwargs)
        print('got result:', result)
        return result
    return wrapped

def output(message):
    print(message)

@logged
def logged_output(message):
    print(message)

output('hello')
print('-' * 50)
logged_output('hello')


def maybe_logged(do_log=True):
    def logged(func):
        def wrapped(*args, **kwargs):
            if do_log:
                print('entered into:', func.__name__)
            result = func(*args, **kwargs)
            if do_log:
                print('got result:', result)
            return result
        return wrapped'''