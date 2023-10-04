import pytest

print('Starting the sample test scenarrio...')


@pytest.fixture(scope='module')
def greet():
    print ('Hello Test Master!')
    return [2, 3, 4]


@pytest.mark.smoketest
@pytest.mark.scen1
def test_scen1_case1(greet):
    print('test_scen1_case1 starting!')
    print(greet)
    greet.append(5)
    print(greet)
    assert 'hello' == 'hello'
@pytest.mark.scen1
@pytest.mark.smoketest
@pytest.mark.scen1case2
def test_scen1_case2(greet):
    print('Scenario 1 case 2 starting...')
    print(greet)
    greet.append(6)
    print(greet)
    assert 2 == 2, "Case 1 failed"
