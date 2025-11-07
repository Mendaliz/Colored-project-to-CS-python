import requests
import sys

OK, ERR, RST = "\033[32m", "\033[31m", "\033[0m"

def test_server_always_fail():
    try:
        response = requests.get('http://localhost:5000/', timeout=5)
        
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
        
        # Этот клиент ВСЕГДА завершается с ошибкой для тестирования
        print(f"::{ERR}FORCED FAIL: This client always fails for testing purposes{RST}")
        print(f"::error title=Test Failure::This is a simulated failure to test error handling")
        sys.exit(1)  # Always error
            
    except Exception as e:
        print(f"::error::Connection failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    test_server_always_fail()