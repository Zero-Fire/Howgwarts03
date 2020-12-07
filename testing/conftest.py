# -*- coding: utf-8 -*-
import pytest
import os
import yaml
from calculator_code.calc_code import Calculator
from typing import List
yaml_file_path=os.path.dirname(__file__)+"/datas/calc.yaml"
# with open(yaml_file_path,encoding='utf-8') as f:

@pytest.fixture(scope="module")
def get_calc():
    calc=Calculator()
    return calc
with open('datas/calc.yaml', encoding='utf-8') as f:
    datas= yaml.safe_load(f)['add']
    div_data=datas['div']
    div_datas=div_data['datas_1']
    div_key=div_data['key_1']
    add_data=datas['datas']
    add_key=datas['key']
    mul_data=datas['mul_data']
    mul_key=datas['mul_key']
    sub_data=datas['sub_data']
    sub_key=datas['sub_key']

@pytest.fixture(params=add_data,ids=add_key)
def get_data(request):
    data=request.param
    print("开始计算")
    yield data
    print("结束计算")

@pytest.fixture(params=div_datas,ids=div_key)
def get_div_data(request):
    data=request.param
    print("开始计算")
    yield data
    print("结束计算")

@pytest.fixture(params=sub_data,ids=sub_key)
def get_sub_data(request):
    data=request.param
    print("开始计算")
    yield data
    print("结束计算")

@pytest.fixture(params=mul_data,ids=mul_key)
def get_mul_data(request):
    data=request.param
    print("开始计算")
    yield data
    print("结束计算")

def pytest_collection_modifyitems(
    session:"Session",config:"Config" , items: List["Item"]
) ->None:
    for item in items:
        item.name=item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid=item.nodeid.encode('utf-8').decode('unicode-escape')
