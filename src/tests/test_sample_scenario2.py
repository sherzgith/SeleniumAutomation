
import pytest
# @pytest.fixture(scope='module')


@pytest.mark.smoketest
@pytest.mark.scen2case1
def test_scen2_case1():
    print("\nScenario 2 case 1 starting...")
    assert True


def test_scen2_case2():
    print("\nScenario 2 case 2 starting...")
    assert False
