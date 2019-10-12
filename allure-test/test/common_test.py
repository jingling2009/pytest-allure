import unittest

# class AlienTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         print("TestCase  start running ")
#
#     def test_1_run(self):
#         print("hello world_1")
#
#     def test_2_run(self):
#         print("hello world_2")
#
#     def test_3_run(self):
#         print("hello world_3")
# if __name__ == '__main__':
#     print("hello world")
#     unittest.main()
import pytest

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


# content of test_sysexit.py
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()

# def test_success():
#     """this test succeeds"""
#     assert True
#
#
# def test_failure():
#     """this test fails"""
#     assert False
#
#
# def test_skip():
#     """this test is skipped"""
#     pytest.skip('for a reason!')
#
#
# def test_broken():
#     raise Exception('oops')