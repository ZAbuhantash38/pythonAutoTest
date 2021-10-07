import jsonpath
import requests
import json
import pytest

#API URL
url="https://run.mocky.io/v3/403b5dc4-fd94-4940-bc08-5529230ffabf"

def test_postReq():
    # Read input Json file
    file = open('C:\\Users\\itg\\Desktop\\API\\dataToSend.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    # Make post request
    response = requests.post(url, request_json)
    assert response.status_code == 200
    #check the  X-Foo-Bar
    fooBar = (response.headers.get('X-Foo-Bar'))
    assert fooBar == 'Hello World'

@pytest.mark.skip(resoan="It's passed")
def test_postReq2():
    file = open('C:\\Users\\itg\\Desktop\\API\\dataToSend.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    # Make post request
    response = requests.post(url, request_json)
    print(response.headers.get('Content-Length'))

