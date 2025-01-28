# GameServerObjectMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**resource_version** | **str** |  | [optional] 
**generation** | **str** |  | [optional] 
**creation_timestamp** | **str** |  | [optional] 
**deletion_timestamp** | **str** |  | [optional] 
**annotations** | **Dict[str, str]** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 

## Example

```python
from agones_python_sdk.models.game_server_object_meta import GameServerObjectMeta

# TODO update the JSON string below
json = "{}"
# create an instance of GameServerObjectMeta from a JSON string
game_server_object_meta_instance = GameServerObjectMeta.from_json(json)
# print the JSON string representation of the object
print(GameServerObjectMeta.to_json())

# convert the object into a dict
game_server_object_meta_dict = game_server_object_meta_instance.to_dict()
# create an instance of GameServerObjectMeta from a dict
game_server_object_meta_from_dict = GameServerObjectMeta.from_dict(game_server_object_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


