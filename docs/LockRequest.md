# LockRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lock_duration_in_seconds** | **str** | The number of seconds to lock the envelope for editing.  Must be greater than 0 seconds. | [optional] 
**locked_by_app** | **str** | A friendly name of the application used to lock the envelope.  Will be used in error messages to the user when lock conflicts occur. | [optional] 
**lock_type** | **str** | The type of envelope lock.  Currently \&quot;edit\&quot; is the only supported type. | [optional] 
**template_password** | **str** |  | [optional] 
**use_scratch_pad** | **str** | Reserved for future use.  Indicates whether a scratchpad is used for editing information.   | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


