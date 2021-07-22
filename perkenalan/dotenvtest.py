from dotenv import load_dotenv
import os

load_dotenv()
uname = os.getenv("user_Name")
key = os.getenv("active_Key")
def print_env():
    print(f'uname: {uname}')
    print(f'key : {key}')

if __name__ == "__main__":
    print_env()
