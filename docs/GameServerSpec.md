# GameServerSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health** | [**GameServerSpecHealth**](GameServerSpecHealth.md) |  | [optional] 

## Example

```python
from agones_python_sdk.models.game_server_spec import GameServerSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GameServerSpec from a JSON string
game_server_spec_instance = GameServerSpec.from_json(json)
# print the JSON string representation of the object
print(GameServerSpec.to_json())

# convert the object into a dict
game_server_spec_dict = game_server_spec_instance.to_dict()
# create an instance of GameServerSpec from a dict
game_server_spec_from_dict = GameServerSpec.from_dict(game_server_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


