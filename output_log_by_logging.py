import time
import logging

logging.basicConfig(level=logging.DEBUG)


def test_1():
    log = logging.getLogger('test_1')
    time.sleep(1)
    log.debug('test 1 step1')
    time.sleep(1)
    log.debug('test 1 step2')
    time.sleep(1)
    log.debug('test 1 step3')
    assert True, 'Pass'


def test_2():
    log = logging.getLogger('test_2')
    time.sleep(1)
    log.debug('test 2 step1')
    time.sleep(1)
    log.debug('test 2 step2')
    time.sleep(1)
    log.debug('test 2 step3')
    log.error('test 2 failed')
    assert False, 'Failed'

