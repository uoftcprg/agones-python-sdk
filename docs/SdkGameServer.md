# SdkGameServer

A GameServer Custom Resource Definition object We will only export those resources that make the most sense. Can always expand to more as needed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_meta** | [**GameServerObjectMeta**](GameServerObjectMeta.md) |  | [optional] 
**spec** | [**GameServerSpec**](GameServerSpec.md) |  | [optional] 
**status** | [**SdkGameServerStatus**](SdkGameServerStatus.md) |  | [optional] 

## Example

```python
from agones_python_sdk.models.sdk_game_server import SdkGameServer

# TODO update the JSON string below
json = "{}"
# create an instance of SdkGameServer from a JSON string
sdk_game_server_instance = SdkGameServer.from_json(json)
# print the JSON string representation of the object
print(SdkGameServer.to_json())

# convert the object into a dict
sdk_game_server_dict = sdk_game_server_instance.to_dict()
# create an instance of SdkGameServer from a dict
sdk_game_server_from_dict = SdkGameServer.from_dict(sdk_game_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


