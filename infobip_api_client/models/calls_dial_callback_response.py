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

from pydantic import ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from infobip_api_client.models.callback_response import CallbackResponse
from infobip_api_client.models.calls_announcements import CallsAnnouncements
from infobip_api_client.models.calls_recording import CallsRecording
from typing import Optional, Set
from typing_extensions import Self


class CallsDialCallbackResponse(CallbackResponse):
    """
    CallsDialCallbackResponse
    """  # noqa: E501

    phone_number: StrictStr = Field(
        description="Destination phone number to call.", alias="phoneNumber"
    )
    caller_id: StrictStr = Field(
        description="Caller ID displayed to a called party.", alias="callerId"
    )
    announcements: Optional[CallsAnnouncements] = None
    recording: Optional[CallsRecording] = None
    client_reference_id: Optional[StrictStr] = Field(
        default=None,
        description="A user-defined reference ID for associating with a number masking session. This ID will appear in subsequent status requests and, if the session is recorded and our SFTP facility is used, will name the recording file. **Note:** In the case of recording, please limit this field to `200` characters as generated file name uses this field, call ID and extension, and if total file name is bigger than 256 characters, saving of the recording file will fail.",
        alias="clientReferenceId",
    )
    __properties: ClassVar[List[str]] = [
        "command",
        "phoneNumber",
        "callerId",
        "announcements",
        "recording",
        "clientReferenceId",
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
        """Create an instance of CallsDialCallbackResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of announcements
        if self.announcements:
            _dict["announcements"] = self.announcements.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recording
        if self.recording:
            _dict["recording"] = self.recording.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallsDialCallbackResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "command": obj.get("command"),
                "phoneNumber": obj.get("phoneNumber"),
                "callerId": obj.get("callerId"),
                "announcements": CallsAnnouncements.from_dict(obj["announcements"])
                if obj.get("announcements") is not None
                else None,
                "recording": CallsRecording.from_dict(obj["recording"])
                if obj.get("recording") is not None
                else None,
                "clientReferenceId": obj.get("clientReferenceId"),
            }
        )
        return _obj
