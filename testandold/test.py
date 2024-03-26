import os, requests, json

from dotenv import load_dotenv

VISION_KEY=os.getenv('VISION_KEY')
VISION_ENDPOINT=os.getenv('VISION_ENDPOINT')
VISION_URL=f"{VISION_ENDPOINT}/computervision/imageanalysis:analyze?features=caption,read&model-version=latest&language=en&api-version=2024-02-01"

headers = {'Accept': 'application/json'
         , 'Ocp-Apim-Subscription-Key': VISION_KEY
         , 'Content-Type': 'application/json'}
IMAGE_URL = 'https://invoiceocrp3.azurewebsites.net/invoices/FAC_2019_0002-521208'
r = requests.post(VISION_URL, headers=headers, json={'url': IMAGE_URL}) # IMAGE_URL : URL de l'image...
print(json.dumps(r.json(), indent=2))