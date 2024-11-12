import requests
email = 'test'
password = 'test'
def call():
    url = "https://wzm-ios-loginservice.prod.demonware.net/v1/login/uno/?titleID=7100&client=atvimobile-cod-wzm-ios"
    headers = {
        "Host": "wzm-ios-loginservice.prod.demonware.net",
        "Accept": "*/*",
        "Upload-Incomplete": "?0",
        "Upload-Draft-Interop-Version": "3",
        "DW-Trace": "tr=10279678104485037497; sp=9ae0b8c4; ss=2473972402625670225",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "Midnight/202403252 CFNetwork/1494.0.7 Darwin/23.4.0",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "X-BDVersion": "8.31.1-master",
        "X-TransactionID": "10279678104485037497"
    }
    data = {
        "version": 1496,
        "platform": "ios",
        "hardwareType": "ios",
        "auth": {
            "email": email,
            "password": password
        }
    }
    response = requests.post(url, json=data, headers=headers)
    print(response.text)

call()
