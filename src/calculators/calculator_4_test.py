from pytest import raises
from typing import Dict, List
from .calculator_4 import Calculator4

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandlerError:
    def average(self, numbers: List[float]) -> float:
        return 3

def test_calculate_average_error():
    mock_request = MockRequest({ "number": [1, 2, 3, 4, 5] })
    calculator_4 = Calculator4(MockDriverHandlerError())

    with raises(Exception) as exc_info:
        response = calculator_4.calculate(mock_request)
    
    assert str(exc_info.value) == "Bad format body!"

def test_calculate():
    mock_request = MockRequest({ "numbers": [1, 2, 3, 4, 5] })
    calculator_4 = Calculator4(MockDriverHandlerError())

    response = calculator_4.calculate(mock_request)
    assert response == {'data': {'Calculator': 4, 'value': 3}}