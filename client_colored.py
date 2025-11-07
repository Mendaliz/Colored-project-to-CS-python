import requests
import sys
import time

# ANSI codes for colored output
OK, ERR, RST = "\033[32m", "\033[31m", "\033[0m"

def test_server():
    max_retries = 5
    retry_delay = 3
    
    for attempt in range(max_retries):
        try:
            print(f"Attempt {attempt + 1}/{max_retries}...")
            
            response = requests.get('http://localhost:5000/', timeout=10)
            
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.text}")
            
            if response.status_code == 200:
                print(f"::{OK}SUCCESS: Server returned 200 OK{RST}")
                print(f"::notice title=Healthcheck passed::Server is healthy and responding correctly")
                sys.exit(0)  # Success
            else:
                print(f"::{ERR}FAIL: Expected status 200, got {response.status_code}{RST}")
                print(f"::error::Server returned unexpected status code: {response.status_code}")
                sys.exit(1)  # Error
                
        except requests.exceptions.ConnectionError:
            if attempt < max_retries - 1:
                print(f"{ERR}Connection failed. Retrying in {retry_delay} seconds...{RST}")
                time.sleep(retry_delay)
            else:
                print(f"::error::Cannot connect to server after {max_retries} attempts")
                sys.exit(1)
                
        except requests.exceptions.Timeout:
            print(f"::error::Request timeout - server is not responding")
            sys.exit(1)
            
        except Exception as e:
            print(f"::error::Unexpected error: {e}")
            sys.exit(1)

if __name__ == '__main__':
    test_server()