# agones_python_sdk.SDKApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allocate**](SDKApi.md#allocate) | **POST** /allocate | Call to self Allocation the GameServer
[**get_game_server**](SDKApi.md#get_game_server) | **GET** /gameserver | Retrieve the current GameServer data
[**health**](SDKApi.md#health) | **POST** /health | Send a Empty every d Duration to declare that this GameSever is healthy
[**ready**](SDKApi.md#ready) | **POST** /ready | Call when the GameServer is ready
[**reserve**](SDKApi.md#reserve) | **POST** /reserve | Marks the GameServer as the Reserved state for Duration
[**set_annotation**](SDKApi.md#set_annotation) | **PUT** /metadata/annotation | Apply a Annotation to the backing GameServer metadata
[**set_label**](SDKApi.md#set_label) | **PUT** /metadata/label | Apply a Label to the backing GameServer metadata
[**shutdown**](SDKApi.md#shutdown) | **POST** /shutdown | Call when the GameServer is shutting down
[**watch_game_server**](SDKApi.md#watch_game_server) | **GET** /watch/gameserver | Send GameServer details whenever the GameServer is updated


# **allocate**
> object allocate(body)

Call to self Allocation the GameServer

### Example


```python
import agones_python_sdk
from agones_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = agones_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with agones_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agones_python_sdk.SDKApi(api_client)
    body = None # object | 

    try:
        # Call to self Allocation the GameServer
        api_response = api_instance.allocate(body)
        print("The response of SDKApi->allocate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDKApi->allocate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_game_server**
> SdkGameServer get_game_server()

Retrieve the current GameServer data

### Example


```python
import agones_python_sdk
from agones_python_sdk.models.sdk_game_server import SdkGameServer
from agones_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = agones_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with agones_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agones_python_sdk.SDKApi(api_client)

    try:
        # Retrieve the current GameServer data
        api_response = api_instance.get_game_server()
        print("The response of SDKApi->get_game_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDKApi->get_game_server: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SdkGameServer**](SdkGameServer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health**
> object health(body)

Send a Empty every d Duration to declare that this GameSever is healthy

### Example


```python
import agones_python_sdk
from agones_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = agones_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with agones_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agones_python_sdk.SDKApi(api_client)
    body = None # object |  (streaming inputs)

    try:
        # Send a Empty every d Duration to declare that this GameSever is healthy
        api_response = api_instance.health(body)
        print("The response of SDKApi->health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDKApi->health: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  (streaming inputs) | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ready**
> object ready(body)

Call when the GameServer is ready

### Example


```python
import agones_python_sdk
from agones_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = agones_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with agones_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agones_python_sdk.SDKApi(api_client)
    body = None # object | 

    try:
        # Call when the GameServer is ready
        api_response = api_instance.ready(body)
        print("The response of SDKApi->ready:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDKApi->ready: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reserve**
> object reserve(body)

Marks the GameServer as the Reserved state for Duration

### Example


```python
import agones_python_sdk
from agones_python_sdk.models.sdk_duration import SdkDuration
from agones_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = agones_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with agones_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agones_python_sdk.SDKApi(api_client)
    body = agones_python_sdk.SdkDuration() # SdkDuration | 

    try:
        # Marks the GameServer as the Reserved state for Duration
        api_response = api_instance.reserve(body)
        print("The response of SDKApi->reserve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDKApi->reserve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SdkDuration**](SdkDuration.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_annotation**
> object set_annotation(body)

Apply a Annotation to the backing GameServer metadata

### Example


```python
import agones_python_sdk
from agones_python_sdk.models.sdk_key_value import SdkKeyValue
from agones_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = agones_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with agones_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agones_python_sdk.SDKApi(api_client)
    body = agones_python_sdk.SdkKeyValue() # SdkKeyValue | 

    try:
        # Apply a Annotation to the backing GameServer metadata
        api_response = api_instance.set_annotation(body)
        print("The response of SDKApi->set_annotation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDKApi->set_annotation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SdkKeyValue**](SdkKeyValue.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_label**
> object set_label(body)

Apply a Label to the backing GameServer metadata

### Example


```python
import agones_python_sdk
from agones_python_sdk.models.sdk_key_value import SdkKeyValue
from agones_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = agones_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with agones_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agones_python_sdk.SDKApi(api_client)
    body = agones_python_sdk.SdkKeyValue() # SdkKeyValue | 

    try:
        # Apply a Label to the backing GameServer metadata
        api_response = api_instance.set_label(body)
        print("The response of SDKApi->set_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDKApi->set_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SdkKeyValue**](SdkKeyValue.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown**
> object shutdown(body)

Call when the GameServer is shutting down

### Example


```python
import agones_python_sdk
from agones_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = agones_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with agones_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agones_python_sdk.SDKApi(api_client)
    body = None # object | 

    try:
        # Call when the GameServer is shutting down
        api_response = api_instance.shutdown(body)
        print("The response of SDKApi->shutdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDKApi->shutdown: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_game_server**
> StreamResultOfSdkGameServer watch_game_server()

Send GameServer details whenever the GameServer is updated

### Example


```python
import agones_python_sdk
from agones_python_sdk.models.stream_result_of_sdk_game_server import StreamResultOfSdkGameServer
from agones_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = agones_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with agones_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agones_python_sdk.SDKApi(api_client)

    try:
        # Send GameServer details whenever the GameServer is updated
        api_response = api_instance.watch_game_server()
        print("The response of SDKApi->watch_game_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDKApi->watch_game_server: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StreamResultOfSdkGameServer**](StreamResultOfSdkGameServer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response.(streaming responses) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

