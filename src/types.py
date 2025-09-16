from typing import Any, Dict, Optional, Union
from enum import Enum

Anyone = Any

class BaseHeader:
    Accept: str
    User_Agent: str
    Content_Type: str

class LoginResultStatus(Enum):
    LoginSuccess = "LoginSuccess"
    LoginAlreadySuccess = "LoginAlreadySuccess"
    # Add other statuses from PayPayStatus

class LoginResult:
    success: bool
    status: LoginResultStatus

class OTP:
    waiting: bool
    otp_prefix: str
    otp_ref_id: str

class LoginContext:
    uuid: Optional[str] = None
    token: Optional[str] = None

class CreateLinkContext:
    androidMinimumVersion: str
    requestId: str
    requestAt: str
    theme: str
    amount: int
    iosMinimumVersion: str
    passcode: Optional[str] = None

class ReceiveLinkContext:
    verificationCode: str
    client_uuid: str
    passcode: str
    requestAt: str
    requestId: str
    orderId: str
    senderMessageId: str
    senderChannelUrl: str
    iosMinimumVersion: str
    androidMinimumVersion: str

class SendMoneyContext:
    theme: str
    externalReceiverId: str
    amount: int
    requestId: str
    requestAt: str
    iosMinimumVersion: str
    androidMinimumVersion: str

class FetchContext:
    method: str  # 'POST' | 'GET' | 'DELETE' | 'PUT' | 'PATCH' | 'OPTIONS' | 'HEAD' | 'TRACE' | 'CONNECT'
    body: Optional[str] = None

class ResponseBody:
    pass

class ResponseFail:
    success: bool = False
    status: str

class ResponseBalance:
    success: bool
    message: str
    total: int
    currency: str
    updated_at: str
    raw: Dict[str, Any]

class ResponseUserInfo:
    success: bool
    message: str
    id: int
    user_id: str
    state: str
    first_name: str
    last_name: str
    # ... other fields

# Add more types as needed