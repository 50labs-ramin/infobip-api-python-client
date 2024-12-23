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
from infobip_api_client.models.message_error import MessageError
from infobip_api_client.models.message_price import MessagePrice
from infobip_api_client.models.message_status import MessageStatus
from typing import Optional, Set
from typing_extensions import Self


class EmailReport(BaseModel):
    """
    EmailReport
    """  # noqa: E501

    application_id: Optional[StrictStr] = Field(
        default=None,
        description="The Application ID sent in the email request.",
        alias="applicationId",
    )
    entity_id: Optional[StrictStr] = Field(
        default=None,
        description="The Entity ID sent in the email request.",
        alias="entityId",
    )
    bulk_id: Optional[StrictStr] = Field(
        default=None,
        description="The ID that uniquely identifies bulks of request.",
        alias="bulkId",
    )
    message_id: Optional[StrictStr] = Field(
        default=None,
        description="The ID that uniquely identifies the sent email request.",
        alias="messageId",
    )
    to: Optional[StrictStr] = Field(
        default=None, description="The recipient email address."
    )
    sent_at: Optional[datetime] = Field(
        default=None,
        description="Tells when the email was initiated. Has the following format: `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.",
        alias="sentAt",
    )
    done_at: Optional[datetime] = Field(
        default=None,
        description="Tells when the email request was processed by Infobip.",
        alias="doneAt",
    )
    message_count: Optional[StrictInt] = Field(
        default=None, description="Email request count.", alias="messageCount"
    )
    price: Optional[MessagePrice] = None
    status: Optional[MessageStatus] = None
    error: Optional[MessageError] = None
    __properties: ClassVar[List[str]] = [
        "applicationId",
        "entityId",
        "bulkId",
        "messageId",
        "to",
        "sentAt",
        "doneAt",
        "messageCount",
        "price",
        "status",
        "error",
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
        """Create an instance of EmailReport from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict["price"] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict["status"] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict["error"] = self.error.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EmailReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "applicationId": obj.get("applicationId"),
                "entityId": obj.get("entityId"),
                "bulkId": obj.get("bulkId"),
                "messageId": obj.get("messageId"),
                "to": obj.get("to"),
                "sentAt": obj.get("sentAt"),
                "doneAt": obj.get("doneAt"),
                "messageCount": obj.get("messageCount"),
                "price": MessagePrice.from_dict(obj["price"])
                if obj.get("price") is not None
                else None,
                "status": MessageStatus.from_dict(obj["status"])
                if obj.get("status") is not None
                else None,
                "error": MessageError.from_dict(obj["error"])
                if obj.get("error") is not None
                else None,
            }
        )
        return _obj
