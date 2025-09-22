import requests
import time
count = 15
while True:
    temp = requests.get('http://127.0.0.1:5000/temp/')
    print("status code : ${temp.status_code},Temp : ${temp}")
    print("-----------------------------------------------")
    count += 1
    payload = dict(value=f'{count}')

    req =requests.post('http://127.0.0.1:5000/temp',data = payload)
    print(req.text)
    time.sleep(1)

