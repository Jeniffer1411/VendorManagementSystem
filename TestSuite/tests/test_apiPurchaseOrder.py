import pytest, requests
from testData.testDataDetails import getPoDetailsToCreate,getPODetailsToDelete,getPODetailsToUpdate,getPODetailsToUpdateAcknowledgedDate,getPODetailsToView
from datetime import datetime
from json.decoder import JSONDecodeError

@pytest.mark.usefixtures('setup')
@pytest.mark.ApiPO
class TestApiPo:
    
    def test_getAllPOApi(self):
        responce = requests.get(self.base_url+'purchase_orders/')
        for po in responce.json():
            print(po)
    
    @pytest.mark.parametrize('data', getPODetailsToView())
    def test_getParticularPOApi(self, data):
        po_number = int(data.get('po_number'))
        response = requests.get(f'{self.base_url}purchase_orders/{po_number}/')
        print(response.json())
    
    @pytest.mark.parametrize('data', getPoDetailsToCreate())
    def test_CreatePOApi(self,data):
        order = {
            'po_number': data.get('po_number'), 
            'vendor': data.get('vendor'),
            'order_date': data.get('order_date'),
            'delivery_date': data.get('delivery_date'), 
            'items': data.get('items'), 
            'quantity': data.get('quantity'), 
            'status': data.get('status'),
            'quality_rate': data.get('quality_rating'),
            'issue_date': data.get('issue_date'),
            'acknowledgment_date': data.get('acknowledgment_date'),
        }
        response = requests.post(self.base_url+ 'purchase_orders/', json=order)
        if response.status_code == 500:
            print("Server error")
        else:
            try:
                json_data = response.json()
                print(json_data)
            except JSONDecodeError:
                print("Invalid JSON response: ", response.text)
        
    @pytest.mark.parametrize('data', getPODetailsToUpdate())
    def test_UpdatePOApi(self,data):
        po_number = data.get('po_number')
        order = {
            'po_number': data.get('po_numberToUpdate'), 
            'vendor': data.get('vendor'),
            'order_date': data.get('order_date'),
            'delivery_date': data.get('delivery_date'), 
            'items': data.get('items'), 
            'quantity': data.get('quantity'), 
            'status': data.get('status'),
            'quality_rate': data.get('quality_rating'),
            'issue_date': data.get('issue_date'),
            'acknowledgment_date': data.get('acknowledgment_date'),
        }
        response = requests.put(f'{self.base_url}purchase_orders/{po_number}/', json=order)
        if response.status_code == 500:
            print("Server error")
        else:
            try:
                json_data = response.json()
                print(json_data)
            except JSONDecodeError:
                print("Invalid JSON response: ", response.text)
        
    @pytest.mark.parametrize('data', getPODetailsToDelete())
    def test_DeletePOApi(self,data):
        po_number = data.get('po_number')
        response = requests.delete(f'{self.base_url}purchase_orders/{po_number}/')
        if response.status_code == 500:
            print("Server error")
        else:
            try:
                json_data = response.json()
                print(json_data)
                
            except JSONDecodeError:
                print("Invalid JSON response: ", response.text)
        
    @pytest.mark.parametrize('data', getPODetailsToUpdateAcknowledgedDate())
    def test_UpdateAcknowledgedDatePOApi(self,data):
        po_number = data.get('po_number')
        acknowledge_date = {'acknowledgment_date': data.get('acknowledgment_date')}
        response = requests.post(f'{self.base_url}purchase_orders/{po_number}/acknowledge/', json=acknowledge_date)
        if response.status_code == 500:
            print("Server error")
        else:
            try:
                json_data = response.json()
                print(json_data)
            except JSONDecodeError:
                print("Invalid JSON response: ", response.text)
        