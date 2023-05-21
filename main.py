import requests
# here we imported a python library called requests which helps us to hit api's

def main():
    response = requests.get('https://api.publicapis.org/entries') # here we make a response variable which stores the value which is getted after hitting the api
    # here .get() function retuens us the reponse
    if response.status_code == 200: # if response's status_code is equal to 200, which means our reponse was success, and we have our api reponses in our response vairable
        print('Success !!')
        data = response.json() #here we converted the reponse into JSON format - Java Script Object Notation and store in data variable
        
        # here We have iterated through the entries from the response and print each key-value pair
        for entry in data['entries']:
            # these are all the key's and value
            print('API:', entry['API'])
            print('Description:', entry['Description'])
            print('Auth:', entry['Auth'])
            print('HTTPS:', entry['HTTPS'])
            print('Cors:', entry['Cors'])
            print('Link:', entry['Link'])
            print('Category:', entry['Category'])
            print('---')
       
    else:
        # here this block will run when the response code returns other than 200
        print('Error !!')

if __name__ == '__main__':
    main()
