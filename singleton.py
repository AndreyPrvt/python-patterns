__author__ = 'andrey_prvt'


class C(object):

    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(C, cls).__new__(cls)
        return cls.instance