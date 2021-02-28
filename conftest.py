from pytest import fixture


@fixture
def hs_data_factory():
    from hs_service.data.hs_data_factory import HSDataFactory
    return HSDataFactory()


@fixture
def hs_test_helper():
    from hs_service.hs_test_helper import HSTestHelper
    return HSTestHelper()
