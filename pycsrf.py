import requests

url = input("Enter the URL to check for CSRF vulnerability: ")
cookies = {}

response = requests.get(url)

if response.cookies:
    cookies = response.cookies

    data = {'some_param': 'some_value', 'csrf_token': 'fake_token'}
    response = requests.post(url, data=data, cookies=cookies)

    if response.status_code == 403:
        print(f"The URL {url} has CSRF protection enabled.")
    else:
        print(f"The URL {url} does not have CSRF protection enabled.")
else:
    print("Could not retrieve cookies from the website.")
