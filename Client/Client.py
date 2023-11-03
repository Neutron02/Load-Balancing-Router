import requests
import time
import threading

# The URL of your router
ROUTER_URL = 'http://172.18.0.22:5000'

# The rate at which to send requests (requests per second)
REQUEST_RATE = 10

# The duration to run the test (in seconds)
TEST_DURATION = 60

# A simple function to send a request
def send_request():
    try:
        response = requests.get(ROUTER_URL)
        print(f'Response Code: {response.status_code}, Response Time: {response.elapsed.total_seconds()}')
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')

# A function to send requests at a defined rate
def send_requests_at_rate(rate, duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        # Start a new thread for each request
        threading.Thread(target=send_request).start()
        # Wait before sending the next request
        time.sleep(1 / rate)

# Run the test
if __name__ == '__main__':
    print(f'Starting load test at a rate of {REQUEST_RATE} requests per second for {TEST_DURATION} seconds...')
    send_requests_at_rate(REQUEST_RATE, TEST_DURATION)
