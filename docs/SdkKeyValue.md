# SdkKeyValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from agones_python_sdk.models.sdk_key_value import SdkKeyValue

# TODO update the JSON string below
json = "{}"
# create an instance of SdkKeyValue from a JSON string
sdk_key_value_instance = SdkKeyValue.from_json(json)
# print the JSON string representation of the object
print(SdkKeyValue.to_json())

# convert the object into a dict
sdk_key_value_dict = sdk_key_value_instance.to_dict()
# create an instance of SdkKeyValue from a dict
sdk_key_value_from_dict = SdkKeyValue.from_dict(sdk_key_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


