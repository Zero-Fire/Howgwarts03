# -*- coding: utf-8 -*-
from calculator_code.calc_code import Calculator

import pytest
import yaml
import allure
#
# def setup_module():
#     # 实例化计算器类
#     print("计算开始")
#
# def teardown_module():
#     print("计算结束")

# with open('datas/calc.yaml', encoding='utf-8') as f:
#     datas= yaml.safe_load(f)['add']
#     div_data=datas['div']
#     div_datas=div_data['datas_1']
#     div_key=div_data['key_1']
#     add_data=datas['datas']
#     add_key=datas['key']
#     mul_data=datas['mul_data']
#     mul_key=datas['mul_key']
#     sub_data=datas['sub_data']
#     sub_key=datas['sub_key']


@allure.feature("测试计算器")
class TestCalc:

    # @pytest.mark.parametrize(
    #     'a,b,expect',
    #     add_data,ids=add_key)
    @allure.story("测试加法")
    @pytest.mark.run(order=1)
    @pytest.mark.add
    def test_add(self,get_data,get_calc):
        #实例化计算器类
        # self.calc= Calculator()
        result=None
        try:
            with allure.step("计算两个数的和的值"):
                result=get_calc.add(get_data[0],get_data[1])
            #判断结果是否为浮点类型，是就保留2位小数
            if isinstance(result,float):
                result=round(result,2)
        except Exception as e:
            print(e)
        assert result == get_data[2]

# class Test_Calc_1:
#
    # @pytest.mark.parametrize(
    #    'a,b,expect',div_datas,ids=div_key
    # )
    @allure.story("测试除法")
    @pytest.mark.last
    @pytest.mark.div
    def test_div(self,get_div_data,get_calc):
        # self.calc = Calculator()
        result=None
        try:
            with allure.step("计算两个数相除的值"):
                result=get_calc.div(get_div_data[0],get_div_data[1])
            if isinstance(result,float):
                result=round(result,2)
        except Exception as e:
            print(e)
        assert result == get_div_data[2]

# class TestCalc_sub:
#     @pytest.mark.parametrize('a,b,expect',sub_data,ids=sub_key)
    @allure.story("测试减法")
    @pytest.mark.run(order=2)
    @pytest.mark.sub
    def test_sub(self,get_sub_data,get_calc):
        # self.calc=Calculator()
        result = None
        try:
            with allure.step("计算两个数相减的值"):
                result=get_calc.sub(get_sub_data[0],get_sub_data[1])
            if isinstance(result,float):
                result=round(result,4)
        except Exception as e:
            print(e)
        assert result == get_sub_data[2]
# class TestCalc_mul:
#     @pytest.mark.parametrize('a,b,expect',mul_data,ids=mul_key)
    @allure.story("测试乘法")
    @pytest.mark.run(order=3)
    @pytest.mark.mul
    def test_mul(self,get_mul_data,get_calc):
        # self.calc=Calculator()
        result = None
        try:
            with allure.step("计算两个数相乘的值"):
                result =get_calc.mul(get_mul_data[0],get_mul_data[1])
            if isinstance(result,float):
                result=round(result,5)
        except Exception as e:
            print(e)
            assert result == get_mul_data[2]
#  #  @pytest.mark.parametrize(
#     #     'a,b,expect',
#     #     [
#     #         (1,1,2),
#     #         (0.1,0.2,0.3),
#     #         (-1,-1,-2)
#     #     ],ids=['int','float','negative']
#     #
#     # )
#
#
#
#
#
#
#











