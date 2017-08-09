# docusign.WorkspacesApi

All URIs are relative to *https://www.docusign.net/restapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace**](WorkspacesApi.md#create_workspace) | **POST** /v2/accounts/{accountId}/workspaces | Create a Workspace
[**create_workspace_file**](WorkspacesApi.md#create_workspace_file) | **POST** /v2/accounts/{accountId}/workspaces/{workspaceId}/folders/{folderId}/files | Creates a workspace file.
[**delete_workspace**](WorkspacesApi.md#delete_workspace) | **DELETE** /v2/accounts/{accountId}/workspaces/{workspaceId} | Delete Workspace
[**delete_workspace_folder_items**](WorkspacesApi.md#delete_workspace_folder_items) | **DELETE** /v2/accounts/{accountId}/workspaces/{workspaceId}/folders/{folderId} | Deletes workspace one or more specific files/folders from the given folder or root.
[**get_workspace**](WorkspacesApi.md#get_workspace) | **GET** /v2/accounts/{accountId}/workspaces/{workspaceId} | Get Workspace
[**get_workspace_file**](WorkspacesApi.md#get_workspace_file) | **GET** /v2/accounts/{accountId}/workspaces/{workspaceId}/folders/{folderId}/files/{fileId} | Get Workspace File
[**list_workspace_file_pages**](WorkspacesApi.md#list_workspace_file_pages) | **GET** /v2/accounts/{accountId}/workspaces/{workspaceId}/folders/{folderId}/files/{fileId}/pages | List File Pages
[**list_workspace_folder_items**](WorkspacesApi.md#list_workspace_folder_items) | **GET** /v2/accounts/{accountId}/workspaces/{workspaceId}/folders/{folderId} | List Workspace Folder Contents
[**list_workspaces**](WorkspacesApi.md#list_workspaces) | **GET** /v2/accounts/{accountId}/workspaces | List Workspaces
[**update_workspace**](WorkspacesApi.md#update_workspace) | **PUT** /v2/accounts/{accountId}/workspaces/{workspaceId} | Update Workspace
[**update_workspace_file**](WorkspacesApi.md#update_workspace_file) | **PUT** /v2/accounts/{accountId}/workspaces/{workspaceId}/folders/{folderId}/files/{fileId} | Update Workspace File Metadata


# **create_workspace**
> Workspace create_workspace(account_id, workspace=workspace)

Create a Workspace

Creates a new workspace.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.WorkspacesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
workspace = docusign.Workspace() # Workspace |  (optional)

try: 
    # Create a Workspace
    api_response = api_instance.create_workspace(account_id, workspace=workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **workspace** | [**Workspace**](Workspace.md)|  | [optional] 

### Return type

[**Workspace**](Workspace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace_file**
> WorkspaceItem create_workspace_file(account_id, folder_id, workspace_id)

Creates a workspace file.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.WorkspacesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
folder_id = 'folder_id_example' # str | The ID of the folder being accessed.
workspace_id = 'workspace_id_example' # str | Specifies the workspace ID GUID.

try: 
    # Creates a workspace file.
    api_response = api_instance.create_workspace_file(account_id, folder_id, workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->create_workspace_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **folder_id** | **str**| The ID of the folder being accessed. | 
 **workspace_id** | **str**| Specifies the workspace ID GUID. | 

### Return type

[**WorkspaceItem**](WorkspaceItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace**
> Workspace delete_workspace(account_id, workspace_id)

Delete Workspace

Deletes an existing workspace (logically).

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.WorkspacesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
workspace_id = 'workspace_id_example' # str | Specifies the workspace ID GUID.

try: 
    # Delete Workspace
    api_response = api_instance.delete_workspace(account_id, workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->delete_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **workspace_id** | **str**| Specifies the workspace ID GUID. | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_folder_items**
> delete_workspace_folder_items(account_id, folder_id, workspace_id, workspace_item_list=workspace_item_list)

Deletes workspace one or more specific files/folders from the given folder or root.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.WorkspacesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
folder_id = 'folder_id_example' # str | The ID of the folder being accessed.
workspace_id = 'workspace_id_example' # str | Specifies the workspace ID GUID.
workspace_item_list = docusign.WorkspaceItemList() # WorkspaceItemList |  (optional)

try: 
    # Deletes workspace one or more specific files/folders from the given folder or root.
    api_instance.delete_workspace_folder_items(account_id, folder_id, workspace_id, workspace_item_list=workspace_item_list)
except ApiException as e:
    print("Exception when calling WorkspacesApi->delete_workspace_folder_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **folder_id** | **str**| The ID of the folder being accessed. | 
 **workspace_id** | **str**| Specifies the workspace ID GUID. | 
 **workspace_item_list** | [**WorkspaceItemList**](WorkspaceItemList.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace**
> Workspace get_workspace(account_id, workspace_id)

Get Workspace

Retrives properties about a workspace given a unique workspaceId. 

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.WorkspacesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
workspace_id = 'workspace_id_example' # str | Specifies the workspace ID GUID.

try: 
    # Get Workspace
    api_response = api_instance.get_workspace(account_id, workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **workspace_id** | **str**| Specifies the workspace ID GUID. | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_file**
> get_workspace_file(account_id, file_id, folder_id, workspace_id, is_download=is_download, pdf_version=pdf_version)

Get Workspace File

Retrieves a workspace file (the binary).

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.WorkspacesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
file_id = 'file_id_example' # str | Specifies the room file ID GUID.
folder_id = 'folder_id_example' # str | The ID of the folder being accessed.
workspace_id = 'workspace_id_example' # str | Specifies the workspace ID GUID.
is_download = 'is_download_example' # str | When set to **true**, the Content-Disposition header is set in the response. The value of the header provides the filename of the file. Default is **false**. (optional)
pdf_version = 'pdf_version_example' # str | When set to **true** the file returned as a PDF. (optional)

try: 
    # Get Workspace File
    api_instance.get_workspace_file(account_id, file_id, folder_id, workspace_id, is_download=is_download, pdf_version=pdf_version)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspace_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **file_id** | **str**| Specifies the room file ID GUID. | 
 **folder_id** | **str**| The ID of the folder being accessed. | 
 **workspace_id** | **str**| Specifies the workspace ID GUID. | 
 **is_download** | **str**| When set to **true**, the Content-Disposition header is set in the response. The value of the header provides the filename of the file. Default is **false**. | [optional] 
 **pdf_version** | **str**| When set to **true** the file returned as a PDF. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspace_file_pages**
> PageImages list_workspace_file_pages(account_id, file_id, folder_id, workspace_id, count=count, dpi=dpi, max_height=max_height, max_width=max_width, start_position=start_position)

List File Pages

Retrieves a workspace file as rasterized pages.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.WorkspacesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
file_id = 'file_id_example' # str | Specifies the room file ID GUID.
folder_id = 'folder_id_example' # str | The ID of the folder being accessed.
workspace_id = 'workspace_id_example' # str | Specifies the workspace ID GUID.
count = 'count_example' # str | The maximum number of results to be returned by this request. (optional)
dpi = 'dpi_example' # str | Number of dots per inch for the resulting image. The default if not used is 94. The range is 1-310. (optional)
max_height = 'max_height_example' # str | Sets the maximum height (in pixels) of the returned image. (optional)
max_width = 'max_width_example' # str | Sets the maximum width (in pixels) of the returned image. (optional)
start_position = 'start_position_example' # str | The position within the total result set from which to start returning values. The value **thumbnail** may be used to return the page image. (optional)

try: 
    # List File Pages
    api_response = api_instance.list_workspace_file_pages(account_id, file_id, folder_id, workspace_id, count=count, dpi=dpi, max_height=max_height, max_width=max_width, start_position=start_position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->list_workspace_file_pages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **file_id** | **str**| Specifies the room file ID GUID. | 
 **folder_id** | **str**| The ID of the folder being accessed. | 
 **workspace_id** | **str**| Specifies the workspace ID GUID. | 
 **count** | **str**| The maximum number of results to be returned by this request. | [optional] 
 **dpi** | **str**| Number of dots per inch for the resulting image. The default if not used is 94. The range is 1-310. | [optional] 
 **max_height** | **str**| Sets the maximum height (in pixels) of the returned image. | [optional] 
 **max_width** | **str**| Sets the maximum width (in pixels) of the returned image. | [optional] 
 **start_position** | **str**| The position within the total result set from which to start returning values. The value **thumbnail** may be used to return the page image. | [optional] 

### Return type

[**PageImages**](PageImages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspace_folder_items**
> WorkspaceFolderContents list_workspace_folder_items(account_id, folder_id, workspace_id, count=count, include_files=include_files, include_sub_folders=include_sub_folders, include_thumbnails=include_thumbnails, include_user_detail=include_user_detail, start_position=start_position, workspace_user_id=workspace_user_id)

List Workspace Folder Contents

Retrieves workspace folder contents, which can include sub folders and files.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.WorkspacesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
folder_id = 'folder_id_example' # str | The ID of the folder being accessed.
workspace_id = 'workspace_id_example' # str | Specifies the workspace ID GUID.
count = 'count_example' # str | The maximum number of results to be returned by this request. (optional)
include_files = 'include_files_example' # str | When set to **true**, file information is returned in the response along with folder information. The default is **false**. (optional)
include_sub_folders = 'include_sub_folders_example' # str | When set to **true**, information about the sub-folders of the current folder is returned. The default is **false**. (optional)
include_thumbnails = 'include_thumbnails_example' # str | When set to **true**, thumbnails are returned as part of the response.  The default is **false**. (optional)
include_user_detail = 'include_user_detail_example' # str | Set to **true** to return extended details about the user. The default is **false**. (optional)
start_position = 'start_position_example' # str | The position within the total result set from which to start returning values. (optional)
workspace_user_id = 'workspace_user_id_example' # str | If set, then the results are filtered to those associated with the specified userId. (optional)

try: 
    # List Workspace Folder Contents
    api_response = api_instance.list_workspace_folder_items(account_id, folder_id, workspace_id, count=count, include_files=include_files, include_sub_folders=include_sub_folders, include_thumbnails=include_thumbnails, include_user_detail=include_user_detail, start_position=start_position, workspace_user_id=workspace_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->list_workspace_folder_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **folder_id** | **str**| The ID of the folder being accessed. | 
 **workspace_id** | **str**| Specifies the workspace ID GUID. | 
 **count** | **str**| The maximum number of results to be returned by this request. | [optional] 
 **include_files** | **str**| When set to **true**, file information is returned in the response along with folder information. The default is **false**. | [optional] 
 **include_sub_folders** | **str**| When set to **true**, information about the sub-folders of the current folder is returned. The default is **false**. | [optional] 
 **include_thumbnails** | **str**| When set to **true**, thumbnails are returned as part of the response.  The default is **false**. | [optional] 
 **include_user_detail** | **str**| Set to **true** to return extended details about the user. The default is **false**. | [optional] 
 **start_position** | **str**| The position within the total result set from which to start returning values. | [optional] 
 **workspace_user_id** | **str**| If set, then the results are filtered to those associated with the specified userId. | [optional] 

### Return type

[**WorkspaceFolderContents**](WorkspaceFolderContents.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspaces**
> WorkspaceList list_workspaces(account_id)

List Workspaces

Gets information about the Workspaces that have been created.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.WorkspacesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.

try: 
    # List Workspaces
    api_response = api_instance.list_workspaces(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->list_workspaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 

### Return type

[**WorkspaceList**](WorkspaceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace**
> Workspace update_workspace(account_id, workspace_id, workspace=workspace)

Update Workspace

Updates information about a specific workspace.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.WorkspacesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
workspace_id = 'workspace_id_example' # str | Specifies the workspace ID GUID.
workspace = docusign.Workspace() # Workspace |  (optional)

try: 
    # Update Workspace
    api_response = api_instance.update_workspace(account_id, workspace_id, workspace=workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->update_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **workspace_id** | **str**| Specifies the workspace ID GUID. | 
 **workspace** | [**Workspace**](Workspace.md)|  | [optional] 

### Return type

[**Workspace**](Workspace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace_file**
> WorkspaceItem update_workspace_file(account_id, file_id, folder_id, workspace_id)

Update Workspace File Metadata

Updates workspace item metadata for one or more specific files/folders.

### Example 
```python
from __future__ import print_statement
import time
import docusign
from docusign.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = docusign.WorkspacesApi()
account_id = 'account_id_example' # str | The external account number (int) or account ID Guid.
file_id = 'file_id_example' # str | Specifies the room file ID GUID.
folder_id = 'folder_id_example' # str | The ID of the folder being accessed.
workspace_id = 'workspace_id_example' # str | Specifies the workspace ID GUID.

try: 
    # Update Workspace File Metadata
    api_response = api_instance.update_workspace_file(account_id, file_id, folder_id, workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->update_workspace_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The external account number (int) or account ID Guid. | 
 **file_id** | **str**| Specifies the room file ID GUID. | 
 **folder_id** | **str**| The ID of the folder being accessed. | 
 **workspace_id** | **str**| Specifies the workspace ID GUID. | 

### Return type

[**WorkspaceItem**](WorkspaceItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

