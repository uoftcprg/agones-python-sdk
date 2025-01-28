# StatusListStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from agones_python_sdk.models.status_list_status import StatusListStatus

# TODO update the JSON string below
json = "{}"
# create an instance of StatusListStatus from a JSON string
status_list_status_instance = StatusListStatus.from_json(json)
# print the JSON string representation of the object
print(StatusListStatus.to_json())

# convert the object into a dict
status_list_status_dict = status_list_status_instance.to_dict()
# create an instance of StatusListStatus from a dict
status_list_status_from_dict = StatusListStatus.from_dict(status_list_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


