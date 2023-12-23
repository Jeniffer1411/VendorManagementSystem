import pandas, os

path = os.getcwd()  # to get the project path

def getVendorCreateDetails():
    df = pandas.read_csv('testData/vendorData/vendorsDetailsToCreate.csv')
    data_list = df.to_dict(orient='records')
    return data_list # data will be returned as dictionary

def getVendorUpdateDetails():
    df = pandas.read_csv('testData/vendorData/vendorDetailsToUpdate.csv')
    data_list = df.to_dict(orient='records')
    return data_list # data will be returned as dictionary

def getVendorDeleteDetails():
    df = pandas.read_csv('testData/vendorData/vendorDetailsToDelete.csv')
    data_list = df.to_dict(orient='records')
    return data_list # data will be returned as dictionary

def getVendorDetails():
    df = pandas.read_csv('testData/vendorData/vendorDetailsToView.csv')
    data_list = df.to_dict(orient='records')
    return data_list # data will be returned as dictionary

def getVendorPerformance():
    df = pandas.read_csv('testData/vendorData/VendorDetailsToViewPerformance.csv')
    data_list = df.to_dict(orient='records')
    return data_list # data will be returned as dictionary

# D:\Documents\All files\santhosh\PycharmProjects\PyTest\testData\puchaseOrderData\poDetailsToView.csv
def getPODetailsToView():
    df = pandas.read_csv('testData/purchaseOrderData/poDetailsToView.csv')
    data_list = df.to_dict(orient='records')
    return data_list # data will be returned as dictionary

def getPoDetailsToCreate():
    df = pandas.read_csv('testData/purchaseOrderData/poDetailsToCreate.csv')
    data_list = df.to_dict(orient='records')
    return data_list # data will be returned as dictionary

def getPODetailsToUpdate():
    df = pandas.read_csv('testData/purchaseOrderData/poDetailsToUpdate.csv') 
    data_list = df.to_dict(orient='records')
    return data_list # data will be returned as dictionary

def getPODetailsToDelete():
    df = pandas.read_csv('testData/purchaseOrderData/poDetailsToDelete.csv')
    data_list = df.to_dict(orient='records')
    return data_list # data will be returned as dictionary

def getPODetailsToUpdateAcknowledgedDate():
    df = pandas.read_csv('testData/purchaseOrderData/poDetailsToUpdataAcknowledgeDate.csv')
    data_list = df.to_dict(orient='records')
    return data_list # data will be returned as dictionary
