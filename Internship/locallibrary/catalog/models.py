from django.db import models

# Create your models here.
class mvContactPerson(models.Model):
    ContactID = models.IntegerField()
    ContactName = models.CharField()
    ContactDepartment = models.CharField()
    ContactAddress = models.CharField()
    ContactEmail = models.CharField()
    ContactPhone1 = models.CharField()
    ContactPhone2 = models.CharField()
    ContactFax = models.CharField()
    ContactIM = models.CharField()
    ContactIsPrimary = models.BooleanField()
    mvContacts = models.Arrayfield(models.ForeignKey(mvSupplierClient, on_delete=models.CASCADE, default=-1))


class mvSupplierClient(models.Model):
    SupplierClientID = models.IntegerField(blank=True)
    SupplierClient_CHOICES = (
        "Both", "Supplier",
        "Client", "SupplierOrClientOrBoth",
    )
    ProductType = models.CharField(max_length=6, choices=SupplierClient_CHOICES, blank=True)
    SupplierClientName = models.Charfield()
    SupplierClientBillingAddress = models.Charfield(blank=True)
    SupplierClientShippingAddress1 = models.Charfield(blank=True)
    SupplierClientShippingAddress2 = models.Charfield(blank=True)
    SupplierClientPhone1 = models.Charfield(blank=True)
    SupplierClientPhone2 = models.Charfield(blank=True)
    SupplierClientFax = models.Charfield(blank=True)
    SupplierClientIM = models.Charfield(blank=True)
    SupplierClientEmail = models.Charfield(blank=True)
    SupplierClientTaxID = models.Charfield(blank=True)
    SupplierClientCurrency = models.Charfield(blank=True)
    SupplierClientPayment_CHOICES = (
        "None", "DueOnReceipt",
        "Net10", "Net15",
        "Net30", "Net60",
        "Net90", "CustomPaymentTerms1",
        "CustomPaymentTerms2", "OtherPaymentTerms",
    )
    SupplierClientPaymentTermsEnum = models.Charfield(max_length=6, choices=SupplierClientPayment_CHOICES, blank=True)
    SupplierClientComments = models.Charfield(blank=True)
    SupplierClientCustomField1 = models.Charfield(blank=True)
    SupplierClientCustomField2 = models.Charfield(blank=True)
    SupplierClientCustomField3 = models.Charfield(blank=True)
    SupplierClientCustomField4 = models.Charfield(blank=True)
    SupplierClientCustomField5 = models.Charfield(blank=True)
    SupplierClientOption1 = models.Booleanfield(blank=True)
    SupplierClientOption2 = models.Booleanfield(blank=True)
    SupplierClientOption3 = models.Booleanfield(blank=True)
    SupplierClientOption4 = models.Booleanfield(blank=True)
    SupplierClientOption5 = models.Booleanfield(blank=True)
    SupplierClientCreationDate = models.Datefield(blank=True)
    mvContacts = models.Arrayfield(models.ForeignKey(mvContactPerson, on_delete=models.CASCADE, default=-1))


class mvProductCategory(models.Model):
    ProductCategoryID = models.IntegerField(blank=True)
    ProductCategoryName = models.CharField()
    ProductCategoryDescription = models.CharField(blank=True)


class mvProduct(models.Model):
    ProductID = models.IntegerField(blank=True)
    Product_CHOICES = (
        "BuyFromSupplier", "Service",
        "ManufactureFromWorkOrder", "BuyFromSupplierOrManufactureFromWorkOrder",
        "TimeRestrictedService", "Undefined",
    )
    ProductType = models.CharField(max_length=6, choices=Product_CHOICES, blank=True)
    ProductSKU = models.CharField(max_length=50)
    ProductEAN = models.CharField(blank=True)
    ProductDescription = models.CharField(max_length=50)
    ProductVersion = models.CharField(blank=True)
    ProductLongDescription = models.CharField(blank=True)
    ProductCategoryID = models.IntegerField(blank=True)
    mvProductCategory = models.ForeignKey(mvProductCategory, on_delete=models.CASCADE, default=-1)
    ProductUnitOfMeasurement = models.CharField(blank=True)
    ProductSellingPrice = models.DoubleField(null=True)
    ProductPurchasePrice = models.DoubleField(null=True)
    ProductUnitCost = models.DoubleField(null=True)
    ProductWeight = models.DoubleField(null=True)
    ProductLength = models.DoubleField(null=True)
    ProductBreadth = models.DoubleField(null=True)
    ProductHeight = models.DoubleField(null=True)
    ProductImageURL = models.CharField(blank=True)
    ProductComments = models.CharField(blank=True)
    ProductCustomField1 = models.CharField(blank=True)
    ProductCustomField2 = models.CharField(blank=True)
    ProductCustomField3 = models.CharField(blank=True)
    ProductCustomField4 = models.CharField(blank=True)
    ProductCustomField5 = models.CharField(blank=True)
    ProductCustomField6 = models.CharField(blank=True)
    ProductCustomField7 = models.CharField(blank=True)
    ProductCustomField8 = models.CharField(blank=True)
    ProductCustomField9 = models.CharField(blank=True)
    ProductCustomField10 = models.CharField(blank=True)
    ProductMainSupplierID = models.IntegerField(blank=True)
    mvProductMainSupplier = models.ForeignKey(mvSupplierClient, on_delete=models.CASCADE, default=-1)
    ProductMainSupplierPrice = models.DoubleField(null=True)
    ProductMainSupplierSKU = models.CharField(blank=True)
    ProductMainSupplierDescription = models.CharField(blank=True)
    ProductCreationDate = models.DateField(blank=True)
    ProductOption1 = models.BooleanField(blank=True)
    ProductOption2 = models.BooleanField(blank=True)
    ProductOption3 = models.BooleanField(blank=True)
    ProductOption4 = models.BooleanField(blank=True)
    ProductOption5 = models.BooleanField(blank=True)
    IsInventorySerialised = models.BooleanField(blank=True)
    IsBatchNumbersEnabled = models.BooleanField(blank=True)
    SerialNumberPrefix = models.CharField(blank=True)
    SerialNumberLength = models.CharField(blank=True)



class ProductUpdate(models.Model):
    APIKEY = models.CharField()
    mvProduct = models.ForeignKey(mvProduct, on_delete=models.CASCADE, default=-1)
    Record_CHOICES = (
        "Insert", "Update",
        "InsertOrUpdate", "InsertOrUpdateNonEmptyFields",
    )
    mvRecordAction = models.CharField(max_length=6, choices=Record_CHOICES, blank=True)
    forceSkuUpdateEvenIfUsedInDocuments = models.BooleanField(blank=True)
    mvInsertUpdateDeleteSourceApplication = models.CharField(blank=True)