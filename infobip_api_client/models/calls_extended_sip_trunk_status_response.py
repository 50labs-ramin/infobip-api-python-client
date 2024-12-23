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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from infobip_api_client.models.calls_sip_trunk_action_status_response import (
    CallsSipTrunkActionStatusResponse,
)
from infobip_api_client.models.calls_sip_trunk_admin_status import (
    CallsSipTrunkAdminStatus,
)
from infobip_api_client.models.calls_sip_trunk_registration_status import (
    CallsSipTrunkRegistrationStatus,
)
from typing import Optional, Set
from typing_extensions import Self


class CallsExtendedSipTrunkStatusResponse(BaseModel):
    """
    CallsExtendedSipTrunkStatusResponse
    """  # noqa: E501

    admin_status: Optional[CallsSipTrunkAdminStatus] = Field(
        default=None, alias="adminStatus"
    )
    action_status: Optional[CallsSipTrunkActionStatusResponse] = Field(
        default=None, alias="actionStatus"
    )
    registration_status: Optional[CallsSipTrunkRegistrationStatus] = Field(
        default=None, alias="registrationStatus"
    )
    active_calls: Optional[StrictInt] = Field(
        default=None, description="Number of active calls.", alias="activeCalls"
    )
    __properties: ClassVar[List[str]] = [
        "adminStatus",
        "actionStatus",
        "registrationStatus",
        "activeCalls",
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
        """Create an instance of CallsExtendedSipTrunkStatusResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of action_status
        if self.action_status:
            _dict["actionStatus"] = self.action_status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallsExtendedSipTrunkStatusResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "adminStatus": obj.get("adminStatus"),
                "actionStatus": CallsSipTrunkActionStatusResponse.from_dict(
                    obj["actionStatus"]
                )
                if obj.get("actionStatus") is not None
                else None,
                "registrationStatus": obj.get("registrationStatus"),
                "activeCalls": obj.get("activeCalls"),
            }
        )
        return _obj
