import requests
import time
from typing import Optional, Dict, Any
from .error import PayPayError
from .types import LoginResult, LoginResultStatus, OTP, LoginContext, ResponseBalance, ResponseUserInfo
from .utils import is_phone, is_password, is_uuid, parse_balance_context, parse_user_info_context, random_uuid
from .headers import create_header
from .status import statusof

class PayPay:
    def __init__(self, phone: str, password: str):
        if not is_phone(phone):
            raise PayPayError("Phone is not valid", 0)
        if not is_password(password):
            raise PayPayError("Password is not valid", 0)
        self.phone = phone
        self.password = password
        self.uuid: Optional[str] = None
        self.token: Optional[str] = None
        self.header = create_header()
        self.cookie: Dict[str, str] = {}
        self.refresh_at: int = 0
        self.logged: bool = False
        self.otp: OTP = OTP(waiting=False, otp_prefix="", otp_ref_id="")

    def is_logged(self) -> bool:
        return self.logged

    def create_login_result(self, success: bool, status: str) -> LoginResult:
        return LoginResult(success=success, status=LoginResultStatus(status))

    async def login(self, context: Optional[LoginContext] = None) -> LoginResult:
        if self.is_logged():
            return self.create_login_result(True, "LoginAlreadySuccess")

        if context and context.token:
            self.token = context.token
            self.logged = True
            self.refresh_at = int(time.time() * 1000)
            self.cookie["token"] = context.token
            return self.create_login_result(True, "LoginSuccess")

        if context and context.uuid:
            if is_uuid(context.uuid):
                self.uuid = context.uuid
            else:
                raise PayPayError("UUID is not valid", 0)
        else:
            self.uuid = random_uuid()

        # Implement login logic here
        # This is a placeholder
        return self.create_login_result(False, "LoginFailed")

    # Add other methods like get_balance, send_money, etc.

class PayPayRecovery:
    # Implement recovery class if needed
    pass