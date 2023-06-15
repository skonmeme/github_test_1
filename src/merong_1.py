from datetime import datetime, timezone, timedelta
import os

if __name__ == '__main__':
    print('Hello, World!')
    print(datetime.now(timezone.utc) + timedelta(hours=9))
    print(os.getcwd())
