from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseSerializer, VendorPerformanceSerializer
from .calculate_metrics import updateResponseTime, VendorPerformanceUpdateError

class VendorApi(APIView):
    def get(self,request,vendor_id=None):
        if vendor_id is not None:
            try:
                data = Vendor.objects.get(id = vendor_id)
                serializer = VendorSerializer(data)
                return Response(serializer.data,status=200)
            except:
                return Response({'message':"Vendor_id Doesn't Exist"},status=404)
        else:
            data = Vendor.objects.all()
            serializer = VendorSerializer(data, many=True)
            return Response(serializer.data,status=200)
        
    def post(self,request):
        data = request.data
        serializer = VendorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':"Vendor Profile Created", 'Data':serializer.data},status=200)
        else:
            return Response(serializer.errors,status=400)
        
    def put(self,request,vendor_id=None):
        try:
            data = request.data
            if vendor_id is not None:
                vendor = Vendor.objects.get(id = vendor_id)
                serializer = VendorSerializer(vendor, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message':"Vendor Profile Updated", 'Data':serializer.data},status=200)
                else:
                    return Response(serializer.errors,status=400)
            else:
                return Response({'message':'Vendor id is not Given'},status=404)
        except:
            return Response({'meesage':"Vendor id doesn't Exist"},status=404)
        
    def patch(self, request, vendor_id=None):
        try:
            data = request.data
            if vendor_id is not None:
                vendor = Vendor.objects.get(id=vendor_id)
                serializer = VendorSerializer(vendor, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message':"Vendor Profile Updated", 'Data':serializer.data},status=200)
                else:
                    return Response(serializer.errors,status=500)
            else:
                return Response({'message':"Vendor Id is not Given"},status=400)
            
        except:
            return Response({'message':"Vendor id doesn't Exist"},status=404)
        
    def delete(self,request,vendor_id=None):
        try:
            vendor = Vendor.objects.get(id=vendor_id)
            vendor.delete() 
            return Response({'message':"Deleted Successfully"},status=200)
        except:
            return Response({'message':"It doesn't Exist"},status=404)

class PurchaseOrderApi(APIView):
    def get(self, request, po_number=None):
        if po_number is not None:
            try:
                data = PurchaseOrder.objects.get(po_number=po_number)
                serializer = PurchaseSerializer(data)
                return Response(serializer.data, status=200)
            except:
                return Response({'message':"Purchase Order Doesn't exist"}, status=404)
        else:
            data = PurchaseOrder.objects.all()
            serializer = PurchaseSerializer(data, many=True)
            return Response(serializer.data, status=200)
        
    def post(self,request):
        try:
            data = request.data
            serializer = PurchaseSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':"Purchase Order Created", 'Data':serializer.data}, status=200)
            else:
                return Response(serializer.errors, status=400)
        except VendorPerformanceUpdateError:
            return Response({"Error":"Vendor Not Found To Update Performance, Please give vendor to PO"}, status=404)
        
    def put(self,request,po_number=None):
        try:
            data = request.data
            if po_number is not None:
                purchase = PurchaseOrder.objects.get(po_number = po_number)
                serializer = PurchaseSerializer(purchase, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message':"Purchase Order Updated", 'Data':serializer.data}, status=200)
                else:
                    return Response(serializer.errors, status=400)
            else:
                return Response({'message':'Purchase Number is not Given'}, status=400)
            
        except VendorPerformanceUpdateError:
            return Response({"Error":"Vendor Not Found To Update Performance, Please give vendor to PO"}, status=404)
        
        except:
            return Response({'meesage':"Purchase Number doesn't Exist"}, status=404)
             
    def delete(self,request,po_number=None):
        try:
            purchase = PurchaseOrder.objects.get(po_number=po_number)
            purchase.delete() 
            return Response({'message':"Deleted Successfully"}, status=200)
        except:
            return Response({'message':"It doesn't Exist"}, status=404)
        
@api_view(["GET"])
def vendorPerformance(request, vendor_id = None):
    if vendor_id is not None:
        try:
            vendor = Vendor.objects.get(id=vendor_id)
            print(vendor.id)
            serializer = VendorPerformanceSerializer(vendor)
            return Response(serializer.data,status=200)
        except:
            return Response({'message': "Id doesn't Exists"},status=400)
        
@api_view(["POST"])       
def purchaseOrderAcknowledged(request,po_number=None):
    try:
        data = request.data
        print(data)
        if po_number is not None:
            po = PurchaseOrder.objects.get(po_number=po_number)
            serializer = PurchaseSerializer(po, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                updateResponseTime(po.vendor)
                return Response({'message': "Acknowledged Date has Updated", "Data":serializer.data},status=200)
            else:
                return Response(serializer.errors,status=400)
        else:
            return Response({"message":"Purchase Order doesn't given"},status=400)
    except:
        return Response({"message":"Purchase Order doesn't Exist"},status=404)
