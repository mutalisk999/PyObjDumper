#!/usr/bin/env python
# encoding: utf-8


def get_py_class_obj_attrs_name(o):
    return [a for a in o.__dict__]


def get_pydantic_obj_attrs_name(o):
    return [a[0] for a in o.__iter__()]
