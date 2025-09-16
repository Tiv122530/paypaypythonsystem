import re
import base64
import uuid
from typing import Dict, Any
from .error import PayPayError
from .types import ResponseBalance, ResponseUserInfo

def is_phone(phone: str) -> bool:
    """
    Determines if a phone number is valid.

    @param phone: The phone number to validate.
    @return: True if the phone number is valid, false otherwise.
    """
    return bool(re.match(r'^0[1-9]0\d{8}$', phone))

def is_password(password: str) -> bool:
    """
    Determines if a password is valid.

    @param password: The password to validate.
    @return: True if the password is valid, false otherwise.
    """
    return bool(re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{6,32}$', password))

def is_uuid(uuid_str: str) -> bool:
    """
    Determines if a UUID is valid.

    @param uuid_str: The UUID to validate.
    @return: True if the UUID is valid, false otherwise.
    """
    try:
        uuid.UUID(uuid_str)
        return True
    except ValueError:
        return False

def parse_cookie_from_map(cookie_map: Dict[str, str]) -> str:
    return '; '.join([f'{key}={value}' for key, value in cookie_map.items()])

recovery_prefix = 'eyJhbGc'

def parse_recovery_code(phone: str, password: str, uuid_str: str) -> str:
    def encode(string: str) -> str:
        return base64.b64encode(string.encode('utf-8')).decode('utf-8')
    return f"{recovery_prefix}{encode(phone)}.{encode(password)}.{encode(uuid_str)}"

def unparse_recovery_code(recovery_code: str) -> Dict[str, str]:
    def decode(string: str) -> str:
        return base64.b64decode(string).decode('utf-8')

    if not recovery_code.startswith(recovery_prefix):
        raise PayPayError('Invalid recovery code', 2)

    cache = recovery_code.replace(recovery_prefix, '').split('.')

    if len(cache) != 3:
        raise PayPayError('Invalid recovery code', 3)

    phone, password, uuid_str = cache

    return {
        'phone': decode(phone),
        'password': decode(password),
        'uuid': decode(uuid_str),
    }

def parse_result_message(result: Any) -> str:
    if 'header' in result and 'resultMessage' in result['header']:
        return result['header'].get('resultMessage', 'unknown')
    else:
        return 'unknown'

def parse_balance_context(result: Any, success: bool) -> ResponseBalance:
    try:
        return ResponseBalance(
            success=success and is_success(result),
            message=parse_result_message(result),
            total=result.get('payload', {}).get('total', 0),
            currency=result.get('payload', {}).get('currency', 'JPY'),
            updated_at='1970-01-01T00:00:00.000Z',  # Placeholder
            raw=result,
        )
    except Exception:
        return ResponseBalance(
            success=False,
            message=parse_result_message(result),
            total=0,
            currency='JPY',
            updated_at='1970-01-01T00:00:00.000Z',
            raw=result,
        )

def parse_user_info_context(result: Any, success: bool) -> ResponseUserInfo:
    try:
        payload = result.get('payload', {})
        return ResponseUserInfo(
            success=success and is_success(result),
            message=parse_result_message(result),
            id=payload.get('id', 0),
            user_id=payload.get('user_defined_id', 'unknown'),
            state=payload.get('state', 'unknown'),
            first_name=payload.get('first_name', 'unknown'),
            last_name=payload.get('last_name', 'unknown'),
            # Add other fields as needed
        )
    except Exception:
        return ResponseUserInfo(
            success=False,
            message=parse_result_message(result),
            id=0,
            user_id='unknown',
            state='unknown',
            first_name='unknown',
            last_name='unknown',
        )

# Placeholder for is_success
def is_success(result: Any) -> bool:
    # Implement based on PayPayStatus
    return result.get('header', {}).get('resultCode') == 'S0000'

def random_uuid() -> str:
    return str(uuid.uuid4())