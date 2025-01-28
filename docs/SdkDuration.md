# SdkDuration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **str** |  | [optional] 

## Example

```python
from agones_python_sdk.models.sdk_duration import SdkDuration

# TODO update the JSON string below
json = "{}"
# create an instance of SdkDuration from a JSON string
sdk_duration_instance = SdkDuration.from_json(json)
# print the JSON string representation of the object
print(SdkDuration.to_json())

# convert the object into a dict
sdk_duration_dict = sdk_duration_instance.to_dict()
# create an instance of SdkDuration from a dict
sdk_duration_from_dict = SdkDuration.from_dict(sdk_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


