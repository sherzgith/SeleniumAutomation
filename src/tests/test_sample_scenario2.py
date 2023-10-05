
import pytest
# @pytest.fixture(scope='module')

@pytest.mark.regression
@pytest.mark.smoketest
@pytest.mark.scen2case1
def test_scen2_case1(greet):
    print("\nScenario 2 case 1 starting...")
    assert True

@pytest.mark.regression
def test_scen2_case2(greet):
    print("\nScenario 2 case 2 starting...")
    assert False
