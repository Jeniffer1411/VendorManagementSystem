from rest_framework import serializers
from .models import Vendor, PurchaseOrder


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ["id", "vendor_name", "vendor_contact_details", "vendor_address", "vendor_code"]
    
    def validate(self, data):
        specialLetters = '~!@#$%^&*()<>?|\/'
        if any(char in specialLetters for char in data['vendor_name']):
            raise serializers.ValidationError("No Special characters Allowed in Names")

        if len(data['vendor_contact_details']) < 10:
            raise serializers.ValidationError("Contact Details should have 10 numbers")
        
        return data

class PurchaseSerializer(serializers.ModelSerializer):
    # vendor = VendorSerializer()

    class Meta:
        model = PurchaseOrder
        fields = "__all__"
        depth = 1
        # exclude = ["vendor"]
         
    def validate(self, data):
        if len(data['items']) < 1:
            raise serializers.ValidationError("Minimum 1 item Required!")
        
        return data

class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ["on_time_delivery_rate", "quality_rating_avg", "average_response_time", "fulfillment_rate"]