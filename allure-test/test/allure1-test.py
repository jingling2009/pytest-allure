# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
import allure
import pytest
# import os
@allure.step
def f():
    return 1

@allure.feature('测试函数')
def test_func():
    assert f()==1

# if __name__ == "__main__":
#     # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /report 目录
#     pytest.main(['--alluredir', './report'])
#     # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
#     os.system('allure generate ./report --clean')

@allure.title("This test has a custom titlee：excepting:failure,real:false")
@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_xfail_expected_failure():
    """this test is an xfail that will be marked as expected failure"""
    assert False

@allure.title("This test has a custom title：excepting:failure,real:true")
@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_xfail_unexpected_pass():
    """this test is an xfail that will be marked as unexpected success"""
    assert True

@pytest.mark.skipif('2 + 2 != 5', reason='This test is skipped by a triggered condition in @pytest.mark.skipif')
def test_skip_by_triggered_condition():
    pass
