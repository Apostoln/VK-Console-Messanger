import vk
import sys

def main():
    TOKEN = sys.argv[1]
    session = vk.Session(access_token=TOKEN)
    api = vk.API(session, v='5.62', lang='ru', timeout=10)

if __name__ == '__main__':
    main()