class SingletonObject(object):
    class __SingletonObject():
        def __init__(self):
            self.val = None

        def __str__(self):
            return "{0!r} {1}".format(self, self.val)

    instance = None

    def __new__(cls, *args, **kwargs):
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject.__SingletonObject
        return SingletonObject.instance


    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setattr__(self, key, value):
        return setattr(self.instance, key, value)

a = SingletonObject()
a.val = 5
print(a)
print(a.val)