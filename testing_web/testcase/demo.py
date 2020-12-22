# -*- coding: utf-8 -*-
import pytest
import yaml

with open("data_member.yaml") as f:
   data = yaml.safe_load(f)['member']
   print(data)
   print(data[0])
@pytest.mark.parametrize("a,b,c",[('1','1','1')])
def test_a(a,b,c):
   print(a,b,c)

