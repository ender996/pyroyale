# pyroyale.PlayersApi

All URIs are relative to *https://api.clashroyale.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player**](PlayersApi.md#get_player) | **GET** /players/{playerTag} | Get player information
[**get_player_battles**](PlayersApi.md#get_player_battles) | **GET** /players/{playerTag}/battlelog | Get log of recent battles for a player
[**get_player_upcoming_chests**](PlayersApi.md#get_player_upcoming_chests) | **GET** /players/{playerTag}/upcomingchests | Get information about player&#39;s upcoming chests


# **get_player**
> PlayerDetail get_player(player_tag)

Get player information

Get information about a single player by player tag. Player tags can befound either in game or by from clan member lists. Note that player tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example player tag '#2ABC' would become '%232ABC' in the URL. 

### Example

* Api Key Authentication (JWT):
```python
from __future__ import print_function
import time
import pyroyale
from pyroyale.rest import ApiException
from pprint import pprint
configuration = pyroyale.Configuration()
# Configure API key authorization: JWT
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to https://api.clashroyale.com/v1
configuration.host = "https://api.clashroyale.com/v1"
# Create an instance of the API class
api_instance = pyroyale.PlayersApi(pyroyale.ApiClient(configuration))
player_tag = 'player_tag_example' # str | Tag of the player to retrieve. 

try:
    # Get player information
    api_response = api_instance.get_player(player_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_tag** | **str**| Tag of the player to retrieve.  | 

### Return type

[**PlayerDetail**](PlayerDetail.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Client provided incorrect parameters for the request. |  -  |
**404** | Resource was not found. |  -  |
**429** | Request was throttled, because amount of requests was above the threshold defined for the used API token.  |  -  |
**500** | Unknown error happened when handling the request.  |  -  |
**503** | Service is temprorarily unavailable because of maintenance.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_battles**
> list[BattleLogEntry] get_player_battles(player_tag)

Get log of recent battles for a player

Get list of recent battle results for a player. 

### Example

* Api Key Authentication (JWT):
```python
from __future__ import print_function
import time
import pyroyale
from pyroyale.rest import ApiException
from pprint import pprint
configuration = pyroyale.Configuration()
# Configure API key authorization: JWT
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to https://api.clashroyale.com/v1
configuration.host = "https://api.clashroyale.com/v1"
# Create an instance of the API class
api_instance = pyroyale.PlayersApi(pyroyale.ApiClient(configuration))
player_tag = 'player_tag_example' # str | Tag of the player whose information to retrieve. 

try:
    # Get log of recent battles for a player
    api_response = api_instance.get_player_battles(player_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_player_battles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_tag** | **str**| Tag of the player whose information to retrieve.  | 

### Return type

[**list[BattleLogEntry]**](BattleLogEntry.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Client provided incorrect parameters for the request. |  -  |
**404** | Resource was not found. |  -  |
**429** | Request was throttled, because amount of requests was above the threshold defined for the used API token.  |  -  |
**500** | Unknown error happened when handling the request.  |  -  |
**503** | Service is temprorarily unavailable because of maintenance.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_upcoming_chests**
> ChestList get_player_upcoming_chests(player_tag)

Get information about player's upcoming chests

Get list of reward chests that the player will receive next in the game. 

### Example

* Api Key Authentication (JWT):
```python
from __future__ import print_function
import time
import pyroyale
from pyroyale.rest import ApiException
from pprint import pprint
configuration = pyroyale.Configuration()
# Configure API key authorization: JWT
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to https://api.clashroyale.com/v1
configuration.host = "https://api.clashroyale.com/v1"
# Create an instance of the API class
api_instance = pyroyale.PlayersApi(pyroyale.ApiClient(configuration))
player_tag = 'player_tag_example' # str | Tag of the player whose information to retrieve. 

try:
    # Get information about player's upcoming chests
    api_response = api_instance.get_player_upcoming_chests(player_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_player_upcoming_chests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_tag** | **str**| Tag of the player whose information to retrieve.  | 

### Return type

[**ChestList**](ChestList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Client provided incorrect parameters for the request. |  -  |
**404** | Resource was not found. |  -  |
**429** | Request was throttled, because amount of requests was above the threshold defined for the used API token.  |  -  |
**500** | Unknown error happened when handling the request.  |  -  |
**503** | Service is temprorarily unavailable because of maintenance.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

