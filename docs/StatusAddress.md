# StatusAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**address** | **str** |  | [optional] 

## Example

```python
from agones_python_sdk.models.status_address import StatusAddress

# TODO update the JSON string below
json = "{}"
# create an instance of StatusAddress from a JSON string
status_address_instance = StatusAddress.from_json(json)
# print the JSON string representation of the object
print(StatusAddress.to_json())

# convert the object into a dict
status_address_dict = status_address_instance.to_dict()
# create an instance of StatusAddress from a dict
status_address_from_dict = StatusAddress.from_dict(status_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


