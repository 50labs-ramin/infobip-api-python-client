# coding: utf-8

"""
    Infobip Client API Libraries OpenAPI Specification

    OpenAPI specification containing public endpoints supported in client API libraries.

    The version of the OpenAPI document: 1.0.0
    Contact: support@infobip.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from infobip_api_client.models.call_rate import CallRate
from infobip_api_client.models.call_recording_request import CallRecordingRequest
from infobip_api_client.models.calls_bulk_call_request import CallsBulkCallRequest
from infobip_api_client.models.calls_machine_detection_request import (
    CallsMachineDetectionRequest,
)
from infobip_api_client.models.calls_retry_options import CallsRetryOptions
from infobip_api_client.models.calls_scheduling_options import CallsSchedulingOptions
from typing import Optional, Set
from typing_extensions import Self


class CallsBulkItem(BaseModel):
    """
    Bulk item list.
    """  # noqa: E501

    var_from: Optional[StrictStr] = Field(
        default=None,
        description="Caller identifier. Must be a number in the [E.164](https://en.wikipedia.org/wiki/E.164) format.",
        alias="from",
    )
    call_requests: List[CallsBulkCallRequest] = Field(
        description="Call request list.", alias="callRequests"
    )
    recording: Optional[CallRecordingRequest] = None
    machine_detection: Optional[CallsMachineDetectionRequest] = Field(
        default=None, alias="machineDetection"
    )
    max_duration: Optional[StrictInt] = Field(
        default=28800,
        description="Maximum call duration in seconds. Once exceeded, the call terminates automatically.",
        alias="maxDuration",
    )
    connect_timeout: Optional[Annotated[int, Field(le=60, strict=True)]] = Field(
        default=None,
        description="Time to wait, in seconds, before the called party answers the call. Once exceeded, the call terminates automatically.",
        alias="connectTimeout",
    )
    call_rate: Optional[CallRate] = Field(default=None, alias="callRate")
    validity_period: Optional[StrictInt] = Field(
        default=None,
        description="The call validity period in minutes. Once expired, the call is not established.",
        alias="validityPeriod",
    )
    retry_options: Optional[CallsRetryOptions] = Field(
        default=None, alias="retryOptions"
    )
    scheduling_options: Optional[CallsSchedulingOptions] = Field(
        default=None, alias="schedulingOptions"
    )
    custom_data: Optional[Dict[str, StrictStr]] = Field(
        default=None,
        description="Client-defined, bulk-level custom data.",
        alias="customData",
    )
    __properties: ClassVar[List[str]] = [
        "from",
        "callRequests",
        "recording",
        "machineDetection",
        "maxDuration",
        "connectTimeout",
        "callRate",
        "validityPeriod",
        "retryOptions",
        "schedulingOptions",
        "customData",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CallsBulkItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in call_requests (list)
        _items = []
        if self.call_requests:
            for _item in self.call_requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict["callRequests"] = _items
        # override the default output from pydantic by calling `to_dict()` of recording
        if self.recording:
            _dict["recording"] = self.recording.to_dict()
        # override the default output from pydantic by calling `to_dict()` of machine_detection
        if self.machine_detection:
            _dict["machineDetection"] = self.machine_detection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of call_rate
        if self.call_rate:
            _dict["callRate"] = self.call_rate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of retry_options
        if self.retry_options:
            _dict["retryOptions"] = self.retry_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scheduling_options
        if self.scheduling_options:
            _dict["schedulingOptions"] = self.scheduling_options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallsBulkItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "from": obj.get("from"),
                "callRequests": [
                    CallsBulkCallRequest.from_dict(_item)
                    for _item in obj["callRequests"]
                ]
                if obj.get("callRequests") is not None
                else None,
                "recording": CallRecordingRequest.from_dict(obj["recording"])
                if obj.get("recording") is not None
                else None,
                "machineDetection": CallsMachineDetectionRequest.from_dict(
                    obj["machineDetection"]
                )
                if obj.get("machineDetection") is not None
                else None,
                "maxDuration": obj.get("maxDuration")
                if obj.get("maxDuration") is not None
                else 28800,
                "connectTimeout": obj.get("connectTimeout"),
                "callRate": CallRate.from_dict(obj["callRate"])
                if obj.get("callRate") is not None
                else None,
                "validityPeriod": obj.get("validityPeriod"),
                "retryOptions": CallsRetryOptions.from_dict(obj["retryOptions"])
                if obj.get("retryOptions") is not None
                else None,
                "schedulingOptions": CallsSchedulingOptions.from_dict(
                    obj["schedulingOptions"]
                )
                if obj.get("schedulingOptions") is not None
                else None,
                "customData": obj.get("customData"),
            }
        )
        return _obj
