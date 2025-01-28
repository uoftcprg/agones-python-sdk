# StatusPlayerStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **str** |  | [optional] 
**capacity** | **str** |  | [optional] 
**ids** | **List[str]** |  | [optional] 

## Example

```python
from agones_python_sdk.models.status_player_status import StatusPlayerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of StatusPlayerStatus from a JSON string
status_player_status_instance = StatusPlayerStatus.from_json(json)
# print the JSON string representation of the object
print(StatusPlayerStatus.to_json())

# convert the object into a dict
status_player_status_dict = status_player_status_instance.to_dict()
# create an instance of StatusPlayerStatus from a dict
status_player_status_from_dict = StatusPlayerStatus.from_dict(status_player_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


