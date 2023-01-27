from fastapi.testclient import TestClient
from ..main import app
from .utils import TestUtils

client = TestClient(app)
    
mainResponseCode = 200
mainResponseBody = {
    "msg": str
}

def test_read_main():
    response = client.get("/")
    assert response.status_code == mainResponseCode
    assert TestUtils.GetResponseTypes(response.json()) == mainResponseBody

