#!/usr/bin/env python
# encoding: utf-8

from . import get_py_class_obj_attrs_name, get_pydantic_obj_attrs_name  # type: ignore


def PydanticObjToPydanticObj(srcObj, destObj):
    destObjAttrNames = get_pydantic_obj_attrs_name(destObj)
    for name in destObjAttrNames:
        setattr(destObj, name, getattr(srcObj, name, None))
    return destObj


def PydanticObjToPyClassObj(srcObj, destObj):
    destObjAttrNames = get_py_class_obj_attrs_name(destObj)
    for name in destObjAttrNames:
        setattr(destObj, name, getattr(srcObj, name, None))
    return destObj
