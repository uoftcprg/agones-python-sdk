# SdkGameServerStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**addresses** | [**List[StatusAddress]**](StatusAddress.md) |  | [optional] 
**ports** | [**List[StatusPort]**](StatusPort.md) |  | [optional] 
**players** | [**StatusPlayerStatus**](StatusPlayerStatus.md) |  | [optional] 
**counters** | [**Dict[str, StatusCounterStatus]**](StatusCounterStatus.md) |  | [optional] 
**lists** | [**Dict[str, StatusListStatus]**](StatusListStatus.md) |  | [optional] 

## Example

```python
from agones_python_sdk.models.sdk_game_server_status import SdkGameServerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SdkGameServerStatus from a JSON string
sdk_game_server_status_instance = SdkGameServerStatus.from_json(json)
# print the JSON string representation of the object
print(SdkGameServerStatus.to_json())

# convert the object into a dict
sdk_game_server_status_dict = sdk_game_server_status_instance.to_dict()
# create an instance of SdkGameServerStatus from a dict
sdk_game_server_status_from_dict = SdkGameServerStatus.from_dict(sdk_game_server_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


