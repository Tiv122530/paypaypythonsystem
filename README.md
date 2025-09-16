# paypaypythonsystem

paypaypythonsystemは、PayPay APIと連携するためのPythonライブラリです。PayPayのモバイル決済サービスをプログラムから操作できます。このライブラリは、TypeScript版のpaypax-mainを基にPythonで実装されています。

## 特徴

- PayPayへのログイン機能
- 残高の取得
- 送金機能
- リンク経由での受け取り
- OTP（ワンタイムパスワード）認証対応
- リカバリーコードによるアカウント復元
- シンプルで使いやすいAPI

## 必要条件

- Python 3.8以上
- requestsライブラリ（自動インストールされます）

## インストール

### PyPIからインストール（公開後）

```bash
pip install paypaypythonsystem
```

### ローカルからインストール（開発時）

リポジトリをクローンまたはダウンロードした後：

```bash
# プロジェクトフォルダに移動
cd paypaypythonsystem

# 依存関係をインストール
pip install -e .
```

または、requirements.txtを作成して：

```bash
pip install -r requirements.txt
```

## 使用方法

### 基本的な使い方

```python
from paypaypythonsystem import PayPay

# PayPayインスタンスを作成（電話番号とパスワードを指定）
paypay = PayPay("09012345678", "YourPassword123")

# ログイン
result = paypay.login()
if result.success:
    print("ログイン成功")
    print(f"ステータス: {result.status}")
else:
    print("ログイン失敗")
    print(f"エラー: {result.status}")
```

### 残高を取得する

```python
# ログイン後に残高を取得
balance = paypay.get_balance()
if balance.success:
    print(f"残高: {balance.total} {balance.currency}")
    print(f"更新日時: {balance.updated_at}")
else:
    print(f"エラー: {balance.message}")
```

### 送金する

```python
# 送金リクエストを作成
send_result = paypay.send_money(
    external_receiver_id="receiver@example.com",
    amount=1000,
    request_id="unique-request-id",
    request_at="2023-10-01T12:00:00Z"
)
if send_result.success:
    print("送金成功")
else:
    print(f"送金失敗: {send_result.message}")
```

### OTP認証を使用する

```python
# OTPが必要な場合
if paypay.otp.waiting:
    print(f"OTPプレフィックス: {paypay.otp.otp_prefix}")
    print(f"OTPリファレンスID: {paypay.otp.otp_ref_id}")
    # OTPコードを入力して認証を完了
    otp_result = paypay.verify_otp("123456")
```

### リカバリーコードを使用する

```python
from paypaypythonsystem import PayPayRecovery

# リカバリーコードから情報を復元
recovery = PayPayRecovery()
phone, password, uuid = recovery.parse_recovery_code("your-recovery-code")
```

## API リファレンス

### PayPay クラス

#### コンストラクタ
```python
PayPay(phone: str, password: str)
```
- `phone`: PayPayに登録された電話番号（例: "09012345678"）
- `password`: PayPayのパスワード

#### メソッド

##### login(context: Optional[LoginContext] = None) -> LoginResult
PayPayにログインします。
- `context`: オプションのログインコンテキスト（UUIDやトークンを指定）

##### get_balance() -> ResponseBalance
現在の残高を取得します。

##### send_money(context: SendMoneyContext) -> ResponseSendMoney
送金を実行します。

##### create_link(context: CreateLinkContext) -> ResponseCreateLink
支払いリンクを作成します。

##### receive_link(context: ReceiveLinkContext) -> ResponseReceiveLink
リンク経由で支払いを受け取ります。

##### logout() -> bool
ログアウトします。

### エラーハンドリング

ライブラリは`PayPayError`例外を投げます。適切にtry-exceptで囲んでください。

```python
try:
    paypay = PayPay("invalid-phone", "password")
except PayPayError as e:
    print(f"エラー: {e.message}")
```

## テスト

テストを実行するにはpytestをインストールしてください：

```bash
pip install pytest
pytest
```

## 貢献

貢献を歓迎します！以下の方法で参加できます：

1. Issueを開いてバグ報告や機能リクエストをする
2. Pull Requestを送ってコードを改善する
3. ドキュメントを更新する

貢献する際は、以下のガイドラインに従ってください：
- コードはPEP 8スタイルに従う
- 新しい機能にはテストを追加する
- コミットメッセージは明確に書く

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細はLICENSEファイルを参照してください。

## 連絡先

- GitHub: [https://github.com/Tiv122530/paypaypythonsystem](https://github.com/Tiv122530/paypaypythonsystem)
- メール: muzui122530@gmail.com

## 注意事項

- このライブラリは非公式です。PayPayのAPI仕様変更により動作しなくなる可能性があります。
- セキュリティのため、パスワードやトークンは安全に管理してください。
- 商用利用の場合はPayPayの利用規約を確認してください。
