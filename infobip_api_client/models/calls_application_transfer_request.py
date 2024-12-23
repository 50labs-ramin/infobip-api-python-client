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
from infobip_api_client.models.platform import Platform
from typing import Optional, Set
from typing_extensions import Self


class CallsApplicationTransferRequest(BaseModel):
    """
    CallsApplicationTransferRequest
    """  # noqa: E501

    destination_calls_configuration_id: StrictStr = Field(
        description="ID of the calls configuration to which the call is to be transferred.",
        alias="destinationCallsConfigurationId",
    )
    platform: Optional[Platform] = None
    timeout: Optional[StrictInt] = Field(
        default=30,
        description="Time to wait, in seconds, for the receiving application to accept the transfer.",
    )
    custom_data: Optional[Dict[str, StrictStr]] = Field(
        default=None,
        description="Optional parameter to update a call's custom data.",
        alias="customData",
    )
    __properties: ClassVar[List[str]] = [
        "destinationCallsConfigurationId",
        "platform",
        "timeout",
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
        """Create an instance of CallsApplicationTransferRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of platform
        if self.platform:
            _dict["platform"] = self.platform.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallsApplicationTransferRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "destinationCallsConfigurationId": obj.get(
                    "destinationCallsConfigurationId"
                ),
                "platform": Platform.from_dict(obj["platform"])
                if obj.get("platform") is not None
                else None,
                "timeout": obj.get("timeout") if obj.get("timeout") is not None else 30,
                "customData": obj.get("customData"),
            }
        )
        return _obj
