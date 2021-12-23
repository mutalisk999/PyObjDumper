#!/usr/bin/env python
# encoding: utf-8
import json

from pydantic import BaseModel
from PyObjDumper.py_class_obj import PyClassObjToPydanticObj, PyClassObjToPyClassObj
from PyObjDumper.pydantic_obj import PydanticObjToPyClassObj, PydanticObjToPydanticObj


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


def testPyClassObjToPyClassObj():
    print("testPyClassObjToPyClassObj")
    sObj = PyClassType1()
    sObj.f1 = 1
    sObj.f2 = "123"
    sObj.f3 = 0.001
    
    dObj = PyClassType2()
    print(dObj.__dict__)
    dObj = PyClassObjToPyClassObj(sObj, dObj)
    print(dObj.__dict__)


def testPyClassObjToPydanticObj():
    print("testPyClassObjToPydanticObj")
    sObj = PyClassType1()
    sObj.f1 = 1
    sObj.f2 = "123"
    sObj.f3 = 0.001

    dObj = PyDanticType1()
    print(dObj.json())
    dObj = PyClassObjToPydanticObj(sObj, dObj)
    print(dObj.json())


def testPydanticObjToPydanticObj():
    print("testPydanticObjToPydanticObj")
    sObj = PyDanticType1()
    sObj.f1 = 1
    sObj.f2 = "123"
    sObj.f3 = 0.001

    dObj = PyDanticType2()
    print(dObj.json())
    dObj = PydanticObjToPydanticObj(sObj, dObj)
    print(dObj.json())


def testPydanticObjToPyClassObj():
    print("testPydanticObjToPyClassObj")
    sObj = PyDanticType1()
    sObj.f1 = 1
    sObj.f2 = "123"
    sObj.f3 = 0.001
    
    dObj = PyClassType1()
    print(dObj.__dict__)
    dObj = PydanticObjToPyClassObj(sObj, dObj)
    print(dObj.__dict__)


def test():
    testPyClassObjToPyClassObj()
    testPyClassObjToPydanticObj()
    testPydanticObjToPydanticObj()
    testPydanticObjToPyClassObj()


if __name__ == "__main__":
    test()
