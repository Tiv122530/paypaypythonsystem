from typing import Dict

PayPayStatusBase = [
    {
        "success": True,
        "status": "LoginSuccess",
    },
    {
        "success": False,
        "status": "LoginFailed",
    },
    {
        "success": False,
        "status": "LoginIncorrectPassOrPhone",
    },
    {
        "success": False,
        "status": "LoginNeedOTP",
    },
    {
        "success": True,
        "status": "LoginDontNeedOTP",
    },
    {
        "success": True,
        "status": "OTPLoginSuccess",
    },
    {
        "success": False,
        "status": "OTPLoginFail",
    },
    {
        "success": True,
        "status": "LoginAlreadySuccess",
    }
]

PayPayStatus: Dict[str, str] = {}
for item in PayPayStatusBase:
    PayPayStatus[item["status"]] = item["status"]

def statusof(status: str) -> bool:
    result = next((item for item in PayPayStatusBase if item["status"] == status), None)
    if not result:
        return False
    return result["success"]