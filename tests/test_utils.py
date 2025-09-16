import pytest
from src.utils import is_phone, is_password, is_uuid

def test_is_phone():
    assert is_phone("09019194545") == True
    assert is_phone("0901919404") == False
    assert is_phone("0a019194545") == False

def test_is_password():
    assert is_password("Aa123456") == True
    assert is_password("123a6") == False
    assert is_password("helloworld") == False

def test_is_uuid():
    assert is_uuid("12345678-1234-1234-1234-123456789012") == True
    assert is_uuid("invalid-uuid") == False