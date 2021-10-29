import pytest #导入pytest

def setup_module():
    """在整个模块用例测试开始前执行"""
    print("----->setup_module")

def teardown_module():
    """在整个模块用例测试结束后执行"""
    print("----->teardown_module")

def setup_function():
    """在每一个外部的用例测试开始前执行"""
    print("----->setup_function")

def teardown_function():
    """在每一个外部的用例测试结束后执行"""
    print("----->teardown_function")

def test_a():
    """以test开头的测试函数"""
    print("----->test_a")
    assert 1 #断言成功

def test_b():
    print('----->test_b')
    assert 'e' in 'et'

class Test_hh:
    def setup_class(self):
        """在整个类中用例测试开始前执行"""
        print("----->setup_class")

    def teardown_class(self):
        """在整个类中用例测试结束后执行"""
        print("----->teardown_class")

    def setup_method(self):
        """在每一个类中的用例测试开始前执行"""
        print("----->setup_method")

    def teardown_method(self):
        """在每一个类中的用例测试结束后执行"""
        print("----->teardown_method")

    def test_c(self):
        print('----->test_c')
        assert 'e' in 'et'

    def test_d(self):
        print('----->test_d')
        assert 'e' in 'et'


if __name__ == "__main__":
    pytest.main("-v -s")