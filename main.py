import requests

def main():
    response = requests.get('https://api.publicapis.org/entries')
    if response.status_code == 200:
        print('Success !!')
        data = response.json()
        for entry in data['entries']:
            print('API:', entry['API'])
            print('Description:', entry['Description'])
            print('Auth:', entry['Auth'])
            print('HTTPS:', entry['HTTPS'])
            print('Cors:', entry['Cors'])
            print('Link:', entry['Link'])
            print('Category:', entry['Category'])
            print('---')
       
    else:
        print('Error !!')

if __name__ == '__main__':
    main()
