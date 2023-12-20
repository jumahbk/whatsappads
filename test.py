import requests

headers = {
    'Authorization': 'Bearer EAAHlPsvlZAjABAHAgvQNymGIvftHtORF4CLyJdkayXskqDYjZCdgDTjqFrW5fZC4UIrfgUVxAcmmuOnTblxBi5ylZBnqUDTwiYAiF5ZBnoxQdA7MZAs80SnWalZCPGz51Fs2qZBfgJFk3yFhPo2AxViRocPuZBxbR4e9PhoRUE8yWBwEVABWQu1Oj',
    'Content-Type': 'application/json',
}

json_data = {
    'messaging_product': 'whatsapp',
    'recipient_type': 'individual',
    'to': '545267344',
    'type': 'template',
    'template': {
        'name': 'national_day_offers',
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
                            'link': 'https://www.medartclinics.com/iphone/kh/free.jpg',
                        },
                    },
                ],
            },
        ],
    },
}

response = requests.post('https://graph.facebook.com/v17.0/105367738941421/messages', headers=headers, json=json_data)
print(response.json())
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{\n  "messaging_product": "whatsapp",\n  "recipient_type": "individual",\n  "to": "0555862924",\n  "type": "template",\n  "template": {\n    "name": 
#"national_day_offers",\n    "language": {\n      "code": "AR"\n    },\n    "components": [\n      {\n        "type": "header",\n        "parameters": [\n          {\n            
#"type": "image",\n            "image": {\n              "link": "https://www.medartclinics.com/iphone/kh/free.jpg"\n            }\n          }\n        ]\n      }\n    
#]\n  }\n}'
#response = requests.post('https://graph.facebook.com/v17.0/105367738941421/messages', headers=headers, data=data)
