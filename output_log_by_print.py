import time


def test_1():
    print('test_1')
    time.sleep(1)
    print('test 1 step1')
    time.sleep(1)
    print('test 1 step2')
    time.sleep(1)
    print('test 2 step3')
    assert True, 'Pass'


def test_2():
    print('in test_2')
    time.sleep(1)
    print('test 2 step1')
    time.sleep(1)
    print('test 2 step2')
    time.sleep(1)
    print('test 2 step3')
    assert False, 'Failed'
