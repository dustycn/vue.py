from .object import Object


class Vue(Object):
    @staticmethod
    def __can_wrap__(obj):
        return hasattr(obj, "_isVue") and obj._isVue

    def __getattr__(self, item):
        try:
            return Object.from_js(getattr(self._js, item))
        except AttributeError:
            if not item.startswith("$"):
                return self.__getattr__("${}".format(item))
            raise

    def __setattr__(self, key, value):
        if key in ["_js"]:
            object.__setattr__(self, key, value)
        elif hasattr(getattr(self, key), "__set__"):
            getattr(self, key).__set__(value)
        else:
            if key not in dir(getattr(self._js, "$props")):
                setattr(self._js, key, value)


Object.SubClasses.append(Vue)
