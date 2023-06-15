from datetime import datetime, timezone, timedelta
import os

hello = 'Hello, World!'

if __name__ == '__main__':
    print(hello)
    print(datetime.now(timezone.utc) + timedelta(hours=9))
    print(os.getcwd())
