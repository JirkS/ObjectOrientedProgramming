class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


try:
    a = Singleton()
    b = Singleton()

    print(a is b)

    a.singl_variable = "Singleton Variable"
    print(a.singl_variable)
    print(b.singl_variable)
except Exception as e:
    print(e)