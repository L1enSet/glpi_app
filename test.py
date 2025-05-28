import requests

def get_data():
    url = "http://127.0.0.1:8000/send_notify/"
    headers = {'ContentType': 'json'}
    
    response=requests.post(url=url, headers=headers)
    print(response.status_code)

    print(response.text)

get_data()