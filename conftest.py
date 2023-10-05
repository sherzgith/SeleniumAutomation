# This is a shared fixture modules

import pytest


@pytest.fixture(scope='session')
def greet():
    print("-\n---------------------SetUp-------------------")
    print('Hello Test Master!')
    yield [2, 3, 4]
    print("\n-------------------TearDown-------------------")
    print("fixture steps are completed here.")