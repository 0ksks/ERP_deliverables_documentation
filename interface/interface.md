# User
## login

`POST` **/user/login**
`BODY TYPE` raw (JSON)
`Headers` 
**Content-Type**: application/json


|     key      |     value      |  type  |   desc   |
| :----------: | :------------: | :----: | :------: |
|  **userID**  |       1        |  int   | Not null |
| **password** | password_value | string | Not null |



### (1) success
`POST` **/user/login_success**
`STATE CODE` 201

```json
{
    "code": 201,
    "message": "success",
    "data": {
        "userID": 1,
        "role": "role_value"
    }
}
```

### (2) user not found
`POST` **/user/login_not_found**
`STATE CODE` 200
```json
{
    "code": 404,
    "message": "user not found",
    "data": {}
}
```

### (3) wrong password
`POST` **/user/login_wrong_password**
`STATE CODE` 200
```json
{
    "code": 401,
    "message": "wrong password",
    "data": {}
}
```

## register

`POST` **/user/register**
`BODY TYPE` raw (JSON)
`Headers` 
**Content-Type**: application/json

|     key      |     value      |  type  |   desc   |
| :----------: | :------------: | :----: | :------: |
| **username** | username_value | string | Not null |
| **password** | password_value | string | Not null |
|   **role**   |   role_value   | string | Not null |


### (1) success
`POST` **/user/register_success**
`STATE CODE` 201

```json
{
    "code": 201,
    "message": "success",
    "data": {
        "userID": 1
    }
}
```


## change password

`POST` **/user/change_password**
`BODY TYPE` raw (JSON)
`Headers` 
**Content-Type**: application/json

|       key       |       value        |  type  |   desc   |
| :-------------: | :----------------: | :----: | :------: |
| **oldPassword** | old_password_value | string | Not null |
| **newPassword** | new_password_value | string | Not null |
|   **userID**    |         1          |  int   | Not null |


### (1) success
`POST` **/user/change_password_success**
`STATE CODE` 201

```json
{
    "code": 201,
    "message": "success",
    "data": {}
}
```

### (2) wrong password
`POST` **/user/change_password_wrong**
`STATE CODE` 200

```json
{
    "code": 401,
    "message": "wrong password",
    "data": {}
}
```


# GoodsReceipt
## create

`POST` **/goods_receipt/create**
`BODY TYPE` raw (JSON)
`Headers` 
**Content-Type**: application/json

|         key         |        value        |  type  |   desc   |
| :-----------------: | :-----------------: | :----: | :------: |
|     **userID**      |          1          |  int   | optional |
| **purchaseOrderID** |          1          |  int   | not null |
|   **materialID**    |          1          |  int   | not null |
|   **supplierID**    |          1          |  int   | not null |
|   **receiptDate**   |     2024/01/01      |  date  | not null |
|    **quantity**     |          1          |  int   | not null |
|  **stockLocation**  | stockLocation_value | string | not null |
|      **batch**      |     batch_value     | string | not null |
|      **plant**      |     plant_value     | string | not null |
|  **movementType**   | movementType_value  | string | not null |
|  **documentDate**   |     2024/01/01      |  date  | not null |
|   **postingDate**   |     2024/01/01      |  date  | not null |


### (1) success
`POST` **/goods_receipt/create_success**
`STATE CODE` 201
```json
{
    "code": 201,
    "message": "success",
    "data": 
    {
        "goodsReceiptID": 1
    }
}
```

## update

`PATCH` **/goods_receipt/update**
`BODY TYPE` raw (JSON)
`Headers` 
**Content-Type**: application/json

|         key         |        value        |  type  |   desc   |
| :-----------------: | :-----------------: | :----: | :------: |
| **goodsReceiptID**  |          1          |  int   | not null |
|     **userID**      |          1          |  int   | optional |
| **purchaseOrderID** |          1          |  int   | optional |
|   **materialID**    |          1          |  int   | optional |
|   **supplierID**    |          1          |  int   | optional |
|   **receiptDate**   |     2024/01/01      |  date  | optional |
|    **quantity**     |          1          |  int   | optional |
|  **stockLocation**  | stockLocation_value | string | optional |
|      **batch**      |     batch_value     | string | optional |
|      **plant**      |     plant_value     | string | optional |
|  **movementType**   | movementType_value  | string | optional |
|  **documentDate**   |     2024/01/01      |  date  | optional |
|   **postingDate**   |     2024/01/01      |  date  | optional |


### (1) success
`PATCH` **/goods_receipt/update_success**
`STATE CODE` 200
```json
{
    "code": 200,
    "message": "success",
    "data": {}
}
```


### (2) goods receipt not found
`PATCH` **/goods_receipt/update_not_found**
`STATE CODE` 200
```json
{
    "code": 404,
    "message": "goods receipt not found",
    "data": []
}
```

## query

`GET` **/goods_receipt/query**
`BODY TYPE` raw (JSON)
`Headers` 
**Content-Type**: application/json

|         key         |        value        |  type  |   desc   |
| :-----------------: | :-----------------: | :----: | :------: |
| **goodsReceiptID**  |          1          |  int   | optional |
|     **userID**      |          1          |  int   | optional |
| **purchaseOrderID** |          1          |  int   | optional |
|   **materialID**    |          1          |  int   | optional |
|   **supplierID**    |          1          |  int   | optional |
|   **receiptDate**   |     2024/01/01      |  date  | optional |
|    **quantity**     |          1          |  int   | optional |
|  **stockLocation**  | stockLocation_value | string | optional |
|      **batch**      |     batch_value     | string | optional |
|      **plant**      |     plant_value     | string | optional |
|  **movementType**   | movementType_value  | string | optional |
|  **documentDate**   |     2024/01/01      |  date  | optional |
|   **postingDate**   |     2024/01/01      |  date  | optional |


### (1) success
`GET` **/goods_receipt/query_success**
`STATE CODE` 200
```json
{
    "code": 200,
    "message": "success",
    "data": [
    {
        "goodsReceiptID": 1,
        "userID": 1,
        "purchaseOrderID": 1,
        "materialID": 1,
        "supplierID": 1,
        "receiptDate": "2024/01/01",
        "quantity": 1,
        "stockLocation": "stockLocation_value1",
        "batch": "batch_value1",
        "plant": "plant_value1",
        "movementType": "movementType_value1",
        "documentDate": "2024/01/01",
        "postingDate": "2024/01/01"
    },
    {
        "goodsReceiptID": 2,
        "userID": 2,
        "purchaseOrderID": 2,
        "materialID": 2,
        "supplierID": 2,
        "receiptDate": "2024/02/02",
        "quantity": 2,
        "stockLocation": "stockLocation_value2",
        "batch": "batch_value2",
        "plant": "plant_value2",
        "movementType": "movementType_value2",
        "documentDate": "2024/02/02",
        "postingDate": "2024/02/02"
    }
]
}
```


### (2) goods receipt not found
`GET` **/goods_receipt/query_not_found**
`STATE CODE` 200
```json
{
    "code": 404,
    "message": "goods receipt not found",
    "data": []
}
```


​    
# Material
## create

`POST` **/material/create**
`BODY TYPE` raw (JSON)
`Headers` 
**Content-Type**: application/json

|           key           |           value           |  type  |   desc   |
| :---------------------: | :-----------------------: | :----: | :------: |
|       **userID**        |             1             |  int   | optional |
|    **materialName**     |    materialName_value     | string | not null |
|     **description**     |     description_value     | string | not null |
|      **baseUnit**       |      baseUnit_value       | string | not null |
|    **materialGroup**    |    materialGroup_value    | string | not null |
|      **division**       |      division_value       | string | not null |
|     **grossWeight**     |            1.1            | float  | not null |
|     **nettWeight**      |            1.1            | float  | not null |
|     **weightUnit**      |     weightUnit_value      | string | not null |
|       **volume**        |            1.1            | float  | not null |
|     **volumeUnit**      |     volumeUnit_value      | string | not null |
|    **packMaterial**     |    packMaterial_value     | string | not null |
|  **availabilityCheck**  |  availabilityCheck_value  | string | not null |
| **transportationGroup** | transportationGroup_value | string | not null |
|    **loadingGroup**     |    loadingGroup_value     | string | not null |
|       **mrpType**       |       mrpType_value       | string | not null |
|    **mrpController**    |    mrpController_value    | string | not null |
|       **lotSize**       |       lotSize_value       | string | not null |
|   **minimumLotSize**    |             1             |  int   | not null |
| **plannedDeliveryTime** |        2024/01/01         |  date  | not null |
|     **movingPrice**     |            1.1            | float  | not null |
|      **priceUnit**      |      priceUnit_value      | string | not null |
|    **standardPrice**    |            1.1            | float  | not null |


### (1) success
`POST` **/material/create_success**
`STATE CODE` 201
```json
{
    "code": 201,
    "message": "success",
    "data": 
    {
        "materialID": 1
    }
}
```

## update

`PATCH` **/material/update**
`BODY TYPE` raw (JSON)
`Headers` 
**Content-Type**: application/json

|           key           |           value           |  type  |   desc   |
| :---------------------: | :-----------------------: | :----: | :------: |
|     **materialID**      |             1             |  int   | not null |
|       **userID**        |             1             |  int   | optional |
|    **materialName**     |    materialName_value     | string | optional |
|     **description**     |     description_value     | string | optional |
|      **baseUnit**       |      baseUnit_value       | string | optional |
|    **materialGroup**    |    materialGroup_value    | string | optional |
|      **division**       |      division_value       | string | optional |
|     **grossWeight**     |            1.1            | float  | optional |
|     **nettWeight**      |            1.1            | float  | optional |
|     **weightUnit**      |     weightUnit_value      | string | optional |
|       **volume**        |            1.1            | float  | optional |
|     **volumeUnit**      |     volumeUnit_value      | string | optional |
|    **packMaterial**     |    packMaterial_value     | string | optional |
|  **availabilityCheck**  |  availabilityCheck_value  | string | optional |
| **transportationGroup** | transportationGroup_value | string | optional |
|    **loadingGroup**     |    loadingGroup_value     | string | optional |
|       **mrpType**       |       mrpType_value       | string | optional |
|    **mrpController**    |    mrpController_value    | string | optional |
|       **lotSize**       |       lotSize_value       | string | optional |
|   **minimumLotSize**    |             1             |  int   | optional |
| **plannedDeliveryTime** |        2024/01/01         |  date  | optional |
|     **movingPrice**     |            1.1            | float  | optional |
|      **priceUnit**      |      priceUnit_value      | string | optional |
|    **standardPrice**    |            1.1            | float  | optional |


### (1) success
`PATCH` **/material/update_success**
`STATE CODE` 200
```json
{
    "code": 200,
    "message": "success",
    "data": {}
}
```


### (2) material not found
`PATCH` **/material/update_not_found**
`STATE CODE` 200
```json
{
    "code": 404,
    "message": "material not found",
    "data": []
}
```

## query

`GET` **/material/query**
`BODY TYPE` raw (JSON)
`Headers` 
**Content-Type**: application/json

|           key           |           value           |  type  |   desc   |
| :---------------------: | :-----------------------: | :----: | :------: |
|     **materialID**      |             1             |  int   | optional |
|       **userID**        |             1             |  int   | optional |
|    **materialName**     |    materialName_value     | string | optional |
|     **description**     |     description_value     | string | optional |
|      **baseUnit**       |      baseUnit_value       | string | optional |
|    **materialGroup**    |    materialGroup_value    | string | optional |
|      **division**       |      division_value       | string | optional |
|     **grossWeight**     |            1.1            | float  | optional |
|     **nettWeight**      |            1.1            | float  | optional |
|     **weightUnit**      |     weightUnit_value      | string | optional |
|       **volume**        |            1.1            | float  | optional |
|     **volumeUnit**      |     volumeUnit_value      | string | optional |
|    **packMaterial**     |    packMaterial_value     | string | optional |
|  **availabilityCheck**  |  availabilityCheck_value  | string | optional |
| **transportationGroup** | transportationGroup_value | string | optional |
|    **loadingGroup**     |    loadingGroup_value     | string | optional |
|       **mrpType**       |       mrpType_value       | string | optional |
|    **mrpController**    |    mrpController_value    | string | optional |
|       **lotSize**       |       lotSize_value       | string | optional |
|   **minimumLotSize**    |             1             |  int   | optional |
| **plannedDeliveryTime** |        2024/01/01         |  date  | optional |
|     **movingPrice**     |            1.1            | float  | optional |
|      **priceUnit**      |      priceUnit_value      | string | optional |
|    **standardPrice**    |            1.1            | float  | optional |


### (1) success
`GET` **/material/query_success**
`STATE CODE` 200
```json
{
    "code": 200,
    "message": "success",
    "data": [
    {
        "materialID": 1,
        "userID": 1,
        "materialName": "materialName_value1",
        "description": "description_value1",
        "baseUnit": "baseUnit_value1",
        "materialGroup": "materialGroup_value1",
        "division": "division_value1",
        "grossWeight": 1.1,
        "nettWeight": 1.1,
        "weightUnit": "weightUnit_value1",
        "volume": 1.1,
        "volumeUnit": "volumeUnit_value1",
        "packMaterial": "packMaterial_value1",
        "availabilityCheck": "availabilityCheck_value1",
        "transportationGroup": "transportationGroup_value1",
        "loadingGroup": "loadingGroup_value1",
        "mrpType": "mrpType_value1",
        "mrpController": "mrpController_value1",
        "lotSize": "lotSize_value1",
        "minimumLotSize": 1,
        "plannedDeliveryTime": "2024/01/01",
        "movingPrice": 1.1,
        "priceUnit": "priceUnit_value1",
        "standardPrice": 1.1
    },
    {
        "materialID": 2,
        "userID": 2,
        "materialName": "materialName_value2",
        "description": "description_value2",
        "baseUnit": "baseUnit_value2",
        "materialGroup": "materialGroup_value2",
        "division": "division_value2",
        "grossWeight": 2.2,
        "nettWeight": 2.2,
        "weightUnit": "weightUnit_value2",
        "volume": 2.2,
        "volumeUnit": "volumeUnit_value2",
        "packMaterial": "packMaterial_value2",
        "availabilityCheck": "availabilityCheck_value2",
        "transportationGroup": "transportationGroup_value2",
        "loadingGroup": "loadingGroup_value2",
        "mrpType": "mrpType_value2",
        "mrpController": "mrpController_value2",
        "lotSize": "lotSize_value2",
        "minimumLotSize": 2,
        "plannedDeliveryTime": "2024/02/02",
        "movingPrice": 2.2,
        "priceUnit": "priceUnit_value2",
        "standardPrice": 2.2
    }
]
}
```


### (2) material not found
`GET` **/material/query_not_found**
`STATE CODE` 200
```json
{
    "code": 404,
    "message": "material not found",
    "data": []
}
```


​    
# PurchaseOrder
## create

`POST` **/purchase_order/create**
`BODY TYPE` raw (JSON)
`Headers` 
**Content-Type**: application/json

|            key             |            value             |  type  |   desc   |
| :------------------------: | :--------------------------: | :----: | :------: |
|         **userID**         |              1               |  int   | optional |
|       **supplierID**       |              1               |  int   | not null |
|       **materialID**       |              1               |  int   | not null |
|       **orderDate**        |          2024/01/01          |  date  | not null |
|      **deliveryDate**      |          2024/01/01          |  date  | not null |
|        **quantity**        |              1               |  int   | not null |
|        **netPrice**        |             1.1              | float  | not null |
|        **currency**        |        currency_value        | string | not null |
|    **purchasingGroup**     |    purchasingGroup_value     | string | not null |
| **purchasingOrganization** | purchasingOrganization_value | string | not null |
|         **plant**          |         plant_value          | string | not null |
|      **paymentTerms**      |      paymentTerms_value      | string | not null |


### (1) success
`POST` **/purchase_order/create_success**
`STATE CODE` 201
```json
{
    "code": 201,
    "message": "success",
    "data": 
    {
        "purchaseOrderID": 1
    }
}
```

## update

`PATCH` **/purchase_order/update**
`BODY TYPE` raw (JSON)
`Headers` 
**Content-Type**: application/json

|            key             |            value             |  type  |   desc   |
| :------------------------: | :--------------------------: | :----: | :------: |
|    **purchaseOrderID**     |              1               |  int   | not null |
|         **userID**         |              1               |  int   | optional |
|       **supplierID**       |              1               |  int   | optional |
|       **materialID**       |              1               |  int   | optional |
|       **orderDate**        |          2024/01/01          |  date  | optional |
|      **deliveryDate**      |          2024/01/01          |  date  | optional |
|        **quantity**        |              1               |  int   | optional |
|        **netPrice**        |             1.1              | float  | optional |
|        **currency**        |        currency_value        | string | optional |
|    **purchasingGroup**     |    purchasingGroup_value     | string | optional |
| **purchasingOrganization** | purchasingOrganization_value | string | optional |
|         **plant**          |         plant_value          | string | optional |
|      **paymentTerms**      |      paymentTerms_value      | string | optional |


### (1) success
`PATCH` **/purchase_order/update_success**
`STATE CODE` 200
```json
{
    "code": 200,
    "message": "success",
    "data": {}
}
```


### (2) purchase order not found
`PATCH` **/purchase_order/update_not_found**
`STATE CODE` 200
```json
{
    "code": 404,
    "message": "purchase order not found",
    "data": []
}
```

## query

`GET` **/purchase_order/query**
`BODY TYPE` raw (JSON)
`Headers` 
**Content-Type**: application/json

|            key             |            value             |  type  |   desc   |
| :------------------------: | :--------------------------: | :----: | :------: |
|    **purchaseOrderID**     |              1               |  int   | optional |
|         **userID**         |              1               |  int   | optional |
|       **supplierID**       |              1               |  int   | optional |
|       **materialID**       |              1               |  int   | optional |
|       **orderDate**        |          2024/01/01          |  date  | optional |
|      **deliveryDate**      |          2024/01/01          |  date  | optional |
|        **quantity**        |              1               |  int   | optional |
|        **netPrice**        |             1.1              | float  | optional |
|        **currency**        |        currency_value        | string | optional |
|    **purchasingGroup**     |    purchasingGroup_value     | string | optional |
| **purchasingOrganization** | purchasingOrganization_value | string | optional |
|         **plant**          |         plant_value          | string | optional |
|      **paymentTerms**      |      paymentTerms_value      | string | optional |


### (1) success
`GET` **/purchase_order/query_success**
`STATE CODE` 200
```json
{
    "code": 200,
    "message": "success",
    "data": [
    {
        "purchaseOrderID": 1,
        "userID": 1,
        "supplierID": 1,
        "materialID": 1,
        "orderDate": "2024/01/01",
        "deliveryDate": "2024/01/01",
        "quantity": 1,
        "netPrice": 1.1,
        "currency": "currency_value1",
        "purchasingGroup": "purchasingGroup_value1",
        "purchasingOrganization": "purchasingOrganization_value1",
        "plant": "plant_value1",
        "paymentTerms": "paymentTerms_value1"
    },
    {
        "purchaseOrderID": 2,
        "userID": 2,
        "supplierID": 2,
        "materialID": 2,
        "orderDate": "2024/02/02",
        "deliveryDate": "2024/02/02",
        "quantity": 2,
        "netPrice": 2.2,
        "currency": "currency_value2",
        "purchasingGroup": "purchasingGroup_value2",
        "purchasingOrganization": "purchasingOrganization_value2",
        "plant": "plant_value2",
        "paymentTerms": "paymentTerms_value2"
    }
]
}
```


### (2) purchase order not found
`GET` **/purchase_order/query_not_found**
`STATE CODE` 200
```json
{
    "code": 404,
    "message": "purchase order not found",
    "data": []
}
```


​    
# Stock
## create

`POST` **/stock/create**
`BODY TYPE` raw (JSON)
`Headers` 
**Content-Type**: application/json

|            key            |            value            |  type  |   desc   |
| :-----------------------: | :-------------------------: | :----: | :------: |
|        **userID**         |              1              |  int   | optional |
|      **materialID**       |              1              |  int   | not null |
|         **plant**         |         plant_value         | string | not null |
|    **storageLocation**    |    storageLocation_value    | string | not null |
|       **quantity**        |              1              |  int   | not null |
|     **unitOfMeasure**     |     unitOfMeasure_value     | string | not null |
|       **stockType**       |       stockType_value       | string | not null |
|     **valuationType**     |     valuationType_value     | string | not null |
|         **batch**         |         batch_value         | string | not null |
| **specialStockIndicator** | specialStockIndicator_value | string | not null |
|      **companyCode**      |      companyCode_value      | string | not null |


### (1) success
`POST` **/stock/create_success**
`STATE CODE` 201
```json
{
    "code": 201,
    "message": "success",
    "data": 
    {
        "stockID": 1
    }
}
```

## update

`PATCH` **/stock/update**
`BODY TYPE` raw (JSON)
`Headers` 
**Content-Type**: application/json

|            key            |            value            |  type  |   desc   |
| :-----------------------: | :-------------------------: | :----: | :------: |
|        **StockID**        |              1              |  int   | not null |
|        **userID**         |              1              |  int   | optional |
|      **materialID**       |              1              |  int   | optional |
|         **plant**         |         plant_value         | string | optional |
|    **storageLocation**    |    storageLocation_value    | string | optional |
|       **quantity**        |              1              |  int   | optional |
|     **unitOfMeasure**     |     unitOfMeasure_value     | string | optional |
|       **stockType**       |       stockType_value       | string | optional |
|     **valuationType**     |     valuationType_value     | string | optional |
|         **batch**         |         batch_value         | string | optional |
| **specialStockIndicator** | specialStockIndicator_value | string | optional |
|      **companyCode**      |      companyCode_value      | string | optional |


### (1) success
`PATCH` **/stock/update_success**
`STATE CODE` 200
```json
{
    "code": 200,
    "message": "success",
    "data": {}
}
```


### (2) stock not found
`PATCH` **/stock/update_not_found**
`STATE CODE` 200
```json
{
    "code": 404,
    "message": "stock not found",
    "data": []
}
```

## query

`GET` **/stock/query**
`BODY TYPE` raw (JSON)
`Headers` 
**Content-Type**: application/json

|            key            |            value            |  type  |   desc   |
| :-----------------------: | :-------------------------: | :----: | :------: |
|        **StockID**        |              1              |  int   | optional |
|        **userID**         |              1              |  int   | optional |
|      **materialID**       |              1              |  int   | optional |
|         **plant**         |         plant_value         | string | optional |
|    **storageLocation**    |    storageLocation_value    | string | optional |
|       **quantity**        |              1              |  int   | optional |
|     **unitOfMeasure**     |     unitOfMeasure_value     | string | optional |
|       **stockType**       |       stockType_value       | string | optional |
|     **valuationType**     |     valuationType_value     | string | optional |
|         **batch**         |         batch_value         | string | optional |
| **specialStockIndicator** | specialStockIndicator_value | string | optional |
|      **companyCode**      |      companyCode_value      | string | optional |


### (1) success
`GET` **/stock/query_success**
`STATE CODE` 200
```json
{
    "code": 200,
    "message": "success",
    "data": [
    {
        "StockID": 1,
        "userID": 1,
        "materialID": 1,
        "plant": "plant_value1",
        "storageLocation": "storageLocation_value1",
        "quantity": 1,
        "unitOfMeasure": "unitOfMeasure_value1",
        "stockType": "stockType_value1",
        "valuationType": "valuationType_value1",
        "batch": "batch_value1",
        "specialStockIndicator": "specialStockIndicator_value1",
        "companyCode": "companyCode_value1"
    },
    {
        "StockID": 2,
        "userID": 2,
        "materialID": 2,
        "plant": "plant_value2",
        "storageLocation": "storageLocation_value2",
        "quantity": 2,
        "unitOfMeasure": "unitOfMeasure_value2",
        "stockType": "stockType_value2",
        "valuationType": "valuationType_value2",
        "batch": "batch_value2",
        "specialStockIndicator": "specialStockIndicator_value2",
        "companyCode": "companyCode_value2"
    }
]
}
```


### (2) stock not found
`GET` **/stock/query_not_found**
`STATE CODE` 200
```json
{
    "code": 404,
    "message": "stock not found",
    "data": []
}
```


​    
# Supplier
## create

`POST` **/supplier/create**
`BODY TYPE` raw (JSON)
`Headers` 
**Content-Type**: application/json

|          key           |          value           |  type  |   desc   |
| :--------------------: | :----------------------: | :----: | :------: |
|       **userID**       |            1             |  int   | optional |
|    **supplierName**    |    supplierName_value    | string | not null |
|      **address**       |      address_value       | string | not null |
| **communicationLang**  | communicationLang_value  | string | not null |
|     **taxNumber**      |            1             |  int   | not null |
|    **companyCode**     |    companyCode_value     | string | not null |
| **reconciliationAcct** | reconciliationAcct_value | string | not null |
|  **checkDoubleVoice**  |  checkDoubleVoice_value  | string | not null |
|     **clerkName**      |     clerkName_value      | string | not null |
|   **purchasingOrg**    |   purchasingOrg_value    | string | not null |
|   **orderCurrency**    |   orderCurrency_value    | string | not null |
|    **paymentTerms**    |    paymentTerms_value    | string | not null |
|  **partnerFunctions**  |  partnerFunctions_value  | string | not null |
|   **streetAddress**    |   streetAddress_value    | string | not null |
|     **postalCode**     |     postalCode_value     | string | not null |
|      **country**       |      country_value       | string | not null |
|       **region**       |       region_value       | string | not null |
|        **city**        |        city_value        | string | not null |
|    **contactInfo**     |    contactInfo_value     | string | not null |


### (1) success
`POST` **/supplier/create_success**
`STATE CODE` 201
```json
{
    "code": 201,
    "message": "success",
    "data": 
    {
        "supplierID": 1
    }
}
```

## update

`PATCH` **/supplier/update**
`BODY TYPE` raw (JSON)
`Headers` 
**Content-Type**: application/json

|          key           |          value           |  type  |   desc   |
| :--------------------: | :----------------------: | :----: | :------: |
|     **supplierID**     |            1             |  int   | not null |
|       **userID**       |            1             |  int   | optional |
|    **supplierName**    |    supplierName_value    | string | optional |
|      **address**       |      address_value       | string | optional |
| **communicationLang**  | communicationLang_value  | string | optional |
|     **taxNumber**      |            1             |  int   | optional |
|    **companyCode**     |    companyCode_value     | string | optional |
| **reconciliationAcct** | reconciliationAcct_value | string | optional |
|  **checkDoubleVoice**  |  checkDoubleVoice_value  | string | optional |
|     **clerkName**      |     clerkName_value      | string | optional |
|   **purchasingOrg**    |   purchasingOrg_value    | string | optional |
|   **orderCurrency**    |   orderCurrency_value    | string | optional |
|    **paymentTerms**    |    paymentTerms_value    | string | optional |
|  **partnerFunctions**  |  partnerFunctions_value  | string | optional |
|   **streetAddress**    |   streetAddress_value    | string | optional |
|     **postalCode**     |     postalCode_value     | string | optional |
|      **country**       |      country_value       | string | optional |
|       **region**       |       region_value       | string | optional |
|        **city**        |        city_value        | string | optional |
|    **contactInfo**     |    contactInfo_value     | string | optional |


### (1) success
`PATCH` **/supplier/update_success**
`STATE CODE` 200
```json
{
    "code": 200,
    "message": "success",
    "data": {}
}
```


### (2) supplier not found
`PATCH` **/supplier/update_not_found**
`STATE CODE` 200
```json
{
    "code": 404,
    "message": "supplier not found",
    "data": []
}
```

## query

`GET` **/supplier/query**
`BODY TYPE` raw (JSON)
`Headers` 
**Content-Type**: application/json

|          key           |          value           |  type  |   desc   |
| :--------------------: | :----------------------: | :----: | :------: |
|     **supplierID**     |            1             |  int   | optional |
|       **userID**       |            1             |  int   | optional |
|    **supplierName**    |    supplierName_value    | string | optional |
|      **address**       |      address_value       | string | optional |
| **communicationLang**  | communicationLang_value  | string | optional |
|     **taxNumber**      |            1             |  int   | optional |
|    **companyCode**     |    companyCode_value     | string | optional |
| **reconciliationAcct** | reconciliationAcct_value | string | optional |
|  **checkDoubleVoice**  |  checkDoubleVoice_value  | string | optional |
|     **clerkName**      |     clerkName_value      | string | optional |
|   **purchasingOrg**    |   purchasingOrg_value    | string | optional |
|   **orderCurrency**    |   orderCurrency_value    | string | optional |
|    **paymentTerms**    |    paymentTerms_value    | string | optional |
|  **partnerFunctions**  |  partnerFunctions_value  | string | optional |
|   **streetAddress**    |   streetAddress_value    | string | optional |
|     **postalCode**     |     postalCode_value     | string | optional |
|      **country**       |      country_value       | string | optional |
|       **region**       |       region_value       | string | optional |
|        **city**        |        city_value        | string | optional |
|    **contactInfo**     |    contactInfo_value     | string | optional |


### (1) success
`GET` **/supplier/query_success**
`STATE CODE` 200
```json
{
    "code": 200,
    "message": "success",
    "data": [
    {
        "supplierID": 1,
        "userID": 1,
        "supplierName": "supplierName_value1",
        "address": "address_value1",
        "communicationLang": "communicationLang_value1",
        "taxNumber": 1,
        "companyCode": "companyCode_value1",
        "reconciliationAcct": "reconciliationAcct_value1",
        "checkDoubleVoice": "checkDoubleVoice_value1",
        "clerkName": "clerkName_value1",
        "purchasingOrg": "purchasingOrg_value1",
        "orderCurrency": "orderCurrency_value1",
        "paymentTerms": "paymentTerms_value1",
        "partnerFunctions": "partnerFunctions_value1",
        "streetAddress": "streetAddress_value1",
        "postalCode": "postalCode_value1",
        "country": "country_value1",
        "region": "region_value1",
        "city": "city_value1",
        "contactInfo": "contactInfo_value1"
    },
    {
        "supplierID": 2,
        "userID": 2,
        "supplierName": "supplierName_value2",
        "address": "address_value2",
        "communicationLang": "communicationLang_value2",
        "taxNumber": 2,
        "companyCode": "companyCode_value2",
        "reconciliationAcct": "reconciliationAcct_value2",
        "checkDoubleVoice": "checkDoubleVoice_value2",
        "clerkName": "clerkName_value2",
        "purchasingOrg": "purchasingOrg_value2",
        "orderCurrency": "orderCurrency_value2",
        "paymentTerms": "paymentTerms_value2",
        "partnerFunctions": "partnerFunctions_value2",
        "streetAddress": "streetAddress_value2",
        "postalCode": "postalCode_value2",
        "country": "country_value2",
        "region": "region_value2",
        "city": "city_value2",
        "contactInfo": "contactInfo_value2"
    }
]
}
```


### (2) supplier not found
`GET` **/supplier/query_not_found**
`STATE CODE` 200
```json
{
    "code": 404,
    "message": "supplier not found",
    "data": []
}
```




# DocumentFlow
## display

`GET` **/document_flow/display**
`BODY TYPE` raw (JSON)
`Headers` 
**Content-Type**: application/json

|         key         | value | type  |   desc   |
| :-----------------: | :---: | :---: | :------: |
| **purchaseOrderID** |   1   |  int  | optional |
| **goodsReceiptID**  |   1   |  int  | optional |
|     **userID**      |   1   |  int  | optional |


### (1) finished
`GET` **/document_flow/display_success/finished**
`STATE CODE` 200
```json
{
    "code": 200,
    "message": "success",
    "data": [
    {
        "purchaseOrderID":1,
        "goodsReceiptID":1,
        "userID":1
    },
    {
        "purchaseOrderID":2,
        "goodsReceiptID":2,
        "userID":2
    }
]
}
```

### (2) unfinished
`GET` **/document_flow/display_success/unfinished**
`STATE CODE` 200
```json
{
    "code": 200,
    "message": "success",
    "data": [
    {
        "purchaseOrderID":1,
        "goodsReceiptID":1,
        "userID":1
    },
    {
        "purchaseOrderID":2,
        "goodsReceiptID":2,
        "userID":2
    }
]
}
```

### (3) document flow not found
`GET` **/document_flow/display_not_found**
`STATE CODE` 200
```json
{
    "code": 404,
    "message": "document flow not found",
    "data": []
}
```