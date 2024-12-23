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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from infobip_api_client.models.calls_file_format import CallsFileFormat
from infobip_api_client.models.calls_recording_file_location import (
    CallsRecordingFileLocation,
)
from infobip_api_client.models.calls_sftp_upload_status import CallsSftpUploadStatus
from typing import Optional, Set
from typing_extensions import Self


class CallsRecordingFile(BaseModel):
    """
    CallsRecordingFile
    """  # noqa: E501

    id: Optional[StrictStr] = Field(default=None, description="File ID.")
    name: StrictStr = Field(description="File name.")
    file_format: CallsFileFormat = Field(alias="fileFormat")
    size: Optional[StrictInt] = Field(default=None, description="File size in bytes.")
    creation_time: Optional[datetime] = Field(
        default=None, description="File creation time.", alias="creationTime"
    )
    duration: Optional[StrictInt] = Field(
        default=None, description="File duration in seconds."
    )
    start_time: Optional[datetime] = Field(
        default=None,
        description="Date and time when the recording started.",
        alias="startTime",
    )
    end_time: Optional[datetime] = Field(
        default=None,
        description="Date and time when the recording ended.",
        alias="endTime",
    )
    location: Optional[CallsRecordingFileLocation] = None
    sftp_upload_status: Optional[CallsSftpUploadStatus] = Field(
        default=None, alias="sftpUploadStatus"
    )
    custom_data: Optional[Dict[str, StrictStr]] = Field(
        default=None, description="Custom data.", alias="customData"
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "name",
        "fileFormat",
        "size",
        "creationTime",
        "duration",
        "startTime",
        "endTime",
        "location",
        "sftpUploadStatus",
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
        """Create an instance of CallsRecordingFile from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallsRecordingFile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "fileFormat": obj.get("fileFormat"),
                "size": obj.get("size"),
                "creationTime": obj.get("creationTime"),
                "duration": obj.get("duration"),
                "startTime": obj.get("startTime"),
                "endTime": obj.get("endTime"),
                "location": obj.get("location"),
                "sftpUploadStatus": obj.get("sftpUploadStatus"),
                "customData": obj.get("customData"),
            }
        )
        return _obj
