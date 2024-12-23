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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class NumberMaskingSetupResponse(BaseModel):
    """
    NumberMaskingSetupResponse
    """  # noqa: E501

    key: Optional[StrictStr] = Field(
        default=None,
        description="Use to connect masking configuration with Voice-enabled number.",
    )
    name: Optional[StrictStr] = Field(
        default=None,
        description="Unique configuration name. Alphanumeric, max length 100.",
    )
    callback_url: Optional[StrictStr] = Field(
        default=None,
        description="Client's URL that will be called on each inbound call to related Number masking Voice number in order to get instructions of how to handle incoming calls. Instructions are a result of mapping logic implemented on your side according to your business case.",
        alias="callbackUrl",
    )
    status_url: Optional[StrictStr] = Field(
        default=None,
        description="Client's URL for status report delivery after the call is finished.",
        alias="statusUrl",
    )
    backup_callback_url: Optional[StrictStr] = Field(
        default=None,
        description="If callbackUrl is unavailable this one will be called instead.",
        alias="backupCallbackUrl",
    )
    backup_status_url: Optional[StrictStr] = Field(
        default=None,
        description="If statusUrl is unavailable this one will be called instead.",
        alias="backupStatusUrl",
    )
    description: Optional[StrictStr] = Field(
        default=None, description="Masking configuration description"
    )
    insert_date_time: Optional[datetime] = Field(
        default=None,
        description="Date and time when masking configuration is created.",
        alias="insertDateTime",
    )
    update_date_time: Optional[datetime] = Field(
        default=None,
        description="Date and time when masking configuration was last modified.",
        alias="updateDateTime",
    )
    __properties: ClassVar[List[str]] = [
        "key",
        "name",
        "callbackUrl",
        "statusUrl",
        "backupCallbackUrl",
        "backupStatusUrl",
        "description",
        "insertDateTime",
        "updateDateTime",
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
        """Create an instance of NumberMaskingSetupResponse from a JSON string"""
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
        """Create an instance of NumberMaskingSetupResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "key": obj.get("key"),
                "name": obj.get("name"),
                "callbackUrl": obj.get("callbackUrl"),
                "statusUrl": obj.get("statusUrl"),
                "backupCallbackUrl": obj.get("backupCallbackUrl"),
                "backupStatusUrl": obj.get("backupStatusUrl"),
                "description": obj.get("description"),
                "insertDateTime": obj.get("insertDateTime"),
                "updateDateTime": obj.get("updateDateTime"),
            }
        )
        return _obj
