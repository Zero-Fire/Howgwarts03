# -*- coding: utf-8 -*-
from calculator_code.calc_code import Calculator

import pytest
import yaml

def setup_module():
    # 实例化计算器类
    print("计算开始")

def teardown_module():
    print("计算结束")

with open('datas/calc.yaml', encoding='utf-8') as f:
    datas= yaml.safe_load(f)['add']
    div_data=datas['div']
    div_datas=div_data['datas_1']
    div_key=div_data['key_1']
    add_data=datas['datas']
    add_key=datas['key']
class TestCalc:

    @pytest.mark.parametrize(
        'a,b,expect',
        add_data,ids=add_key)

    def test_add(self,a,b,expect):
        #实例化计算器类
        self.calc= Calculator()
        result=self.calc.add(a,b)
        #判断结果是否为浮点类型，是就保留2位小数
        if isinstance(result,float):
            result=round(result,2)
        assert result == expect

class Test_Calc_1:

    @pytest.mark.parametrize(
       'a,b,expect',div_datas,ids=div_key
    )

    def test_div(self,a,b,expect):
        self.calc = Calculator()
        result=self.calc.div(a,b)
        if isinstance(result,float):
            result=round(result,2)
        assert result == expect
        if isinstance(result,str):
            assert result==expect

 #  @pytest.mark.parametrize(
    #     'a,b,expect',
    #     [
    #         (1,1,2),
    #         (0.1,0.2,0.3),
    #         (-1,-1,-2)
    #     ],ids=['int','float','negative']
    #
    # )


















