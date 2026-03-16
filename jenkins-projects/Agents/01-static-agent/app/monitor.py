import requests
import json
import time
import os

def load_urls(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data['urls']

def check_url(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        elapsed = round((time.time() - start) * 1000)
        return {
            "url": url,
            "status": "UP",
            "status_code": response.status_code,
            "response_time_ms": elapsed
        }
    except requests.exceptions.ConnectionError:
        return {
            "url": url,
            "status": "DOWN",
            "status_code": None,
            "response_time_ms": None,
            "reason": "Connection Error"
        }
    except requests.exceptions.Timeout:
        return {
            "url": url,
            "status": "DOWN",
            "status_code": None,
            "response_time_ms": None,
            "reason": "Timeout"
        }

def run_monitor():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    urls_path = os.path.join(base_dir, 'urls.json')
    urls = load_urls(urls_path)

    print("\n========== URL Health Monitor ==========\n")
    for url in urls:
        result = check_url(url)
        if result['status'] == 'UP':
            print(f"✅ {result['url']}")
            print(f"   Status : {result['status']}")
            print(f"   Code   : {result['status_code']}")
            print(f"   Time   : {result['response_time_ms']}ms\n")
        else:
            print(f"❌ {result['url']}")
            print(f"   Status : {result['status']}")
            print(f"   Reason : {result.get('reason', 'Unknown')}\n")
    print("========================================\n")

if __name__ == "__main__":
    run_monitor()