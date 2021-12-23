# PyObjDumper


### example

* python class type and pydantic type

```
class PyClassType1(object):
    def __init__(self):
        self.f1: int = None
        self.f2: str = None
        self.f3: float = None


class PyClassType2(object):
    def __init__(self):
        self.f1: int = None
        self.f2: str = None
        self.f3: float = None
        self.f4: str = None


class PyDanticType1(BaseModel):
    f1: int = None
    f2: str = None
    f3: float = None


class PyDanticType2(BaseModel):
    f1: int = None
    f2: str = None
    f3: float = None
    f4: str = None
```


* python class type object to python class type object

```
    sObj = PyClassType1()
    sObj.f1 = 1
    sObj.f2 = "123"
    sObj.f3 = 0.001
    
    dObj = PyClassType2()
    print(dObj.__dict__)
    dObj = PyClassObjToPyClassObj(sObj, dObj)
    print(dObj.__dict__)
```

```
{'f1': None, 'f2': None, 'f3': None, 'f4': None}
{'f1': 1, 'f2': '123', 'f3': 0.001, 'f4': None}
```

* python class type object to pydantic type object

```
    sObj = PyClassType1()
    sObj.f1 = 1
    sObj.f2 = "123"
    sObj.f3 = 0.001

    dObj = PyDanticType1()
    print(dObj.json())
    dObj = PyClassObjToPydanticObj(sObj, dObj)
    print(dObj.json())
```

```
{"f1": null, "f2": null, "f3": null}
{"f1": 1, "f2": "123", "f3": 0.001}
```

* pydantic type object to pydantic type object

```
    sObj = PyDanticType1()
    sObj.f1 = 1
    sObj.f2 = "123"
    sObj.f3 = 0.001

    dObj = PyDanticType2()
    print(dObj.json())
    dObj = PydanticObjToPydanticObj(sObj, dObj)
    print(dObj.json())
```

```
{"f1": null, "f2": null, "f3": null, "f4": null}
{"f1": 1, "f2": "123", "f3": 0.001, "f4": null}
```

* pydantic type object to python class type object

```
    sObj = PyDanticType1()
    sObj.f1 = 1
    sObj.f2 = "123"
    sObj.f3 = 0.001
    
    dObj = PyClassType1()
    print(dObj.__dict__)
    dObj = PydanticObjToPyClassObj(sObj, dObj)
    print(dObj.__dict__)
```

```
{'f1': None, 'f2': None, 'f3': None}
{'f1': 1, 'f2': '123', 'f3': 0.001}
```
