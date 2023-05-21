import requests

def main():
    response = requests.get('https://api.publicapis.org/entries')
    if response.status_code == 200:
        print('Success !!')
    else:
        print('Error !!')

if __name__ == '__main__':
    main()
