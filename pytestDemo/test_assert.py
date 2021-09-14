import pytest
# 上海-悠悠
from pytest_assume.plugin import assume

@pytest.mark.parametrize(('x', 'y'),
                         [(1, 1), (1, 0), (0, 1)])
def test_simple_assume(x, y):
    print("测试数据x=%s, y=%s" % (x, y))
    pytest.assume(x == y)
    pytest.assume(x+y > 1)
    pytest.assume(x > 1)
    print("测试完成！")

@pytest.mark.parametrize(('x', 'y'),
                         [(2, 2), (1, 0), (0, 1)])
def test_simple_assume(x, y):
    print("测试数据x=%s, y=%s" % (x, y))
    with assume:
        assert x == y
        assert x > 1
        assert x + y > 1
        print("测试完成！")