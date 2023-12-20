import csv
import requests
import random

urls = [
    "https://medartclinics.com/iphone/kh/wall/ww.jpg",
 
]


def send_msg(tonum, url):


    headers = {
        'Authorization': 'Bearer EAAHlPsvlZAjABAHAgvQNymGIvftHtORF4CLyJdkayXskqDYjZCdgDTjqFrW5fZC4UIrfgUVxAcmmuOnTblxBi5ylZBnqUDTwiYAiF5ZBnoxQdA7MZAs80SnWalZCPGz51Fs2qZBfgJFk3yFhPo2AxViRocPuZBxbR4e9PhoRUE8yWBwEVABWQu1Oj',
        'Content-Type': 'application/json',
    }

    json_data = {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'to': tonum,
        'type': 'template',
        'template': {
            'name': 'wall',
            'language': {
                'code': 'AR',
            },
            'components': [
                {
                    'type': 'header',
                    'parameters': [
                        {
                            'type': 'image',
                            'image': {
                                'link': url,
                            },
                        },
                    ],
                },
            ],
        },
    }

    response = requests.post('https://graph.facebook.com/v17.0/105367738941421/messages', headers=headers, json=json_data)
    print(response.json())
    
def perform_action(phone_number , url):
    # Replace the following line with any action you want to perform
    send_msg(phone_number , url)
    print(phone_number)
    print(url)
def read_phone_numbers_from_csv(file_path):
    phone_numbers = []

    with open(file_path, 'r') as file:
        reader = csv.reader(file)

        # Assuming phone numbers are in the first column of the CSV
        for row in reader:
            phone_numbers.append(row[0])

    return phone_numbers

def main():
    # Replace 'phone_numbers.csv' with your CSV file's path
    csv_file_path = 'wa.csv'
    
    phone_numbers = read_phone_numbers_from_csv(csv_file_path)
    zz = 0
    for phone_number in phone_numbers:
        zz = zz+1
        print(zz)
        perform_action(phone_number, random.choice(urls))

if __name__ == '__main__':
    main()

