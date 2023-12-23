import pytest, requests
from testData.testDataDetails import getVendorCreateDetails, getVendorUpdateDetails, getVendorDeleteDetails, getVendorDetails, getVendorPerformance
from json.decoder import JSONDecodeError


@pytest.mark.VendorApi
@pytest.mark.usefixtures('setup')
class TestApiVendor:
    
    def test_getAllVendorsApi(self):
        responce = requests.get(self.base_url+"vendors/")
        for vendor in responce.json():
            print(vendor)
        assert responce.status_code == 200
    
    @pytest.mark.parametrize('data',getVendorDetails())
    def test_getParticularVendorApi(self, data):
        vendor_id = int(data.get('vendor_id'))
        response = requests.get(f'{self.base_url}vendors/{vendor_id}/')
        if response.status_code == 500:
            print("Server error")
        else:
            try:
                json_data = response.json()
                print(json_data)
            except JSONDecodeError:
                print("Invalid JSON response: ", response.text)
        
    @pytest.mark.parametrize('data',getVendorCreateDetails())
    def test_postVendorApi(self,data):
        vendor = {
            "vendor_name" : data.get('vendor_name'),
            "vendor_contact_details" : data.get('vendor_contact'),
            "vendor_address" : data.get('vendor_address'),
            "vendor_code" : data.get('vendor_code')
        }
        response = requests.post(self.base_url+"vendors/",json=vendor)
        if response.status_code == 500:
            print("Server error")
        else:
            try:
                json_data = response.json()
                print(json_data)
            except JSONDecodeError:
                print("Invalid JSON response: ", response.text)
    
    @pytest.mark.parametrize('data',getVendorUpdateDetails())
    def test_updateVendorApi(self,data):
        vendor_id = int(data.get('vendor_id'))
        vendor = {
            "vendor_name" : data.get('vendor_name'),
            "vendor_contact_details" : data.get('vendor_contact'),
            "vendor_address" : data.get('vendor_address'),
            "vendor_code" : data.get('vendor_code')
        }
        response = requests.put(f'{self.base_url}vendors/{vendor_id}/', json=vendor)
        if response.status_code == 500:
            print("Server error")
        else:
            try:
                json_data = response.json()
                print(json_data)
            except JSONDecodeError:
                print("Invalid JSON response: ", response.text)
    
    @pytest.mark.parametrize('data',getVendorDeleteDetails())
    def test_deleteVendorApi(self, data):
        vendor_id = data.get('vendor_id')
        response = requests.delete(f'{self.base_url}vendors/{vendor_id}/')
        if response.status_code == 500:
            print("Server error")
        else:
            try:
                json_data = response.json()
                print(json_data)
            except JSONDecodeError:
                print("Invalid JSON response: ", response.text)
        
    @pytest.mark.parametrize('data',getVendorPerformance())
    def test_vednorPerformanceApi(self, data):
        vendor_id = data.get('vendor_id')
        response = requests.get(f'{self.base_url}vendors/{vendor_id}/performance/')
        if response.status_code == 500:
            print("Server error")
        else:
            try:
                json_data = response.json()
                print(json_data)
            except JSONDecodeError:
                print("Invalid JSON response: ", response.text)
        