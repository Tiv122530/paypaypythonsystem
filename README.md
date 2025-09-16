# paypaypythonsystem

A Python library for interacting with the PayPay API.

## Installation

```bash
pip install paypaypythonsystem
```

## Usage

```python
from paypaypythonsystem import PayPay

paypay = PayPay("your_phone", "your_password")
result = paypay.login()
if result.success:
    print("Logged in successfully")
```

## Features

- Login to PayPay
- Get balance
- Send money
- Receive money
- And more...

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

MIT License
