from a_mainimports import *
from b_mainfunctions import récup_invoices

data = []
response = requests.get(url, headers=headers)
data = response.json()
data = data.get('invoices')

récup_invoices(data, headers)