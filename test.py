import json
import requests

def test_details_route():
    response = requests.get('http://localhost:5000/details')
    assert response.status_code == 200
    data = json.loads(response.text)
    assert 'hostname' in data
    assert 'ip' in data
    assert 'mac' in data
