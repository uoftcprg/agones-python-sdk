# StatusCounterStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **str** |  | [optional] 
**capacity** | **str** |  | [optional] 

## Example

```python
from agones_python_sdk.models.status_counter_status import StatusCounterStatus

# TODO update the JSON string below
json = "{}"
# create an instance of StatusCounterStatus from a JSON string
status_counter_status_instance = StatusCounterStatus.from_json(json)
# print the JSON string representation of the object
print(StatusCounterStatus.to_json())

# convert the object into a dict
status_counter_status_dict = status_counter_status_instance.to_dict()
# create an instance of StatusCounterStatus from a dict
status_counter_status_from_dict = StatusCounterStatus.from_dict(status_counter_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


