# GameServerSpecHealth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** |  | [optional] 
**period_seconds** | **int** |  | [optional] 
**failure_threshold** | **int** |  | [optional] 
**initial_delay_seconds** | **int** |  | [optional] 

## Example

```python
from agones_python_sdk.models.game_server_spec_health import GameServerSpecHealth

# TODO update the JSON string below
json = "{}"
# create an instance of GameServerSpecHealth from a JSON string
game_server_spec_health_instance = GameServerSpecHealth.from_json(json)
# print the JSON string representation of the object
print(GameServerSpecHealth.to_json())

# convert the object into a dict
game_server_spec_health_dict = game_server_spec_health_instance.to_dict()
# create an instance of GameServerSpecHealth from a dict
game_server_spec_health_from_dict = GameServerSpecHealth.from_dict(game_server_spec_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


