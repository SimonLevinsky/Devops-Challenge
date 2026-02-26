import sys
import time
import urllib.request
import urllib.error

URL = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:30080"
MAX_RETRIES = 30
RETRY_INTERVAL = 10

print(f"Testing application at: {URL}")
print(f"Max retries: {MAX_RETRIES}, interval: {RETRY_INTERVAL}s")

for attempt in range(1, MAX_RETRIES + 1):
    print(f"Attempt {attempt} of {MAX_RETRIES}...")

    try:
        with urllib.request.urlopen(URL, timeout=5) as response:
            status = response.status
            body = response.read().decode("utf-8")

            if status == 200 and "200 OK" in body:
                print(f"✅ SUCCESS! Application is running.")
                print(f"Response: {body}")
                sys.exit(0)
            else:
                print(f"⏳ Unexpected response (HTTP {status}). Waiting {RETRY_INTERVAL}s...")

    except urllib.error.HTTPError as e:
        print(f"⏳ HTTP error: {e.code}. Waiting {RETRY_INTERVAL}s...")

    except urllib.error.URLError as e:
        print(f"⏳ Connection failed: {e.reason}. Waiting {RETRY_INTERVAL}s...")

    except Exception as e:
        print(f"⏳ Unexpected error: {e}. Waiting {RETRY_INTERVAL}s...")

    time.sleep(RETRY_INTERVAL)

print(f"❌ FAILED: Application did not respond after {MAX_RETRIES * RETRY_INTERVAL} seconds.")
sys.exit(1)