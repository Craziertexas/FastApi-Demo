import requests

reportURL = "https://webhook.site/f62ca4df-2a17-4307-babc-633f6eb38b7c"

def pytest_sessionstart(session):
    msg = "Starting test session..."
    requests.post(reportURL, data=msg)

def pytest_sessionfinish(session, exitstatus):
    msg = "Test session finished."
    requests.post(reportURL, data=msg)