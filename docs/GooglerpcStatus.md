# GooglerpcStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**details** | [**List[ProtobufAny]**](ProtobufAny.md) |  | [optional] 

## Example

```python
from agones_python_sdk.models.googlerpc_status import GooglerpcStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GooglerpcStatus from a JSON string
googlerpc_status_instance = GooglerpcStatus.from_json(json)
# print the JSON string representation of the object
print(GooglerpcStatus.to_json())

# convert the object into a dict
googlerpc_status_dict = googlerpc_status_instance.to_dict()
# create an instance of GooglerpcStatus from a dict
googlerpc_status_from_dict = GooglerpcStatus.from_dict(googlerpc_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


