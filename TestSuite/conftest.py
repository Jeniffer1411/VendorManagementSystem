import pytest
from utilities.graphical_result import graphical_result


@pytest.fixture(scope="class")
def setup(request):
    request.cls.base_url = 'http://127.0.0.1:8000/api/'
    yield
    graphical_result('reports/test_report.xml')
    