# StatusPort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**port** | **int** |  | [optional] 

## Example

```python
from agones_python_sdk.models.status_port import StatusPort

# TODO update the JSON string below
json = "{}"
# create an instance of StatusPort from a JSON string
status_port_instance = StatusPort.from_json(json)
# print the JSON string representation of the object
print(StatusPort.to_json())

# convert the object into a dict
status_port_dict = status_port_instance.to_dict()
# create an instance of StatusPort from a dict
status_port_from_dict = StatusPort.from_dict(status_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


