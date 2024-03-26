from a_mainimports import *

def récup_invoices(data, headers):
    lastDate = data[-1]['dt']
    flag = False
    
    while not flag:
        urldata = f"https://invoiceocrp3.azurewebsites.net/invoices?start_date={lastDate}"
        responseData = requests.get(urldata, headers=headers)
        
        if responseData.status_code == 200:
            adddata = responseData.json().get('invoices', [])
            
            if not adddata:
                flag = True
            else:
                data.extend(adddata)
                lastDate = data[-1]['dt']
                print(lastDate, data[-1])
        else:
            print(f"Erreur: {responseData.status_code} - {responseData.reason}")
            flag = True

