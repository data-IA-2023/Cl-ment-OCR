import requests
import os
from dotenv import load_dotenv
from array import array
from PIL import Image
import sys
import time
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes, VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


# Environment Keys and connexion ComputerVision
load_dotenv("envressources/keys.env")
subscription_key = os.environ["VISION_KEY"]
endpoint = os.environ["VISION_ENDPOINT"]
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# Variables pour requêtes HTTP vers URL ou sont stockées les factures
url = "https://invoiceocrp3.azurewebsites.net/invoices"
headers = {
    "accept": "application/json"
}

