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
from infobip_api_client.models.calls_anonymization_type import CallsAnonymizationType
from infobip_api_client.models.calls_audio_codec import CallsAudioCodec
from infobip_api_client.models.calls_dtmf_type import CallsDtmfType
from infobip_api_client.models.calls_fax_type import CallsFaxType
from infobip_api_client.models.calls_number_presentation_format import (
    CallsNumberPresentationFormat,
)
from infobip_api_client.models.calls_selection_strategy import CallsSelectionStrategy
from infobip_api_client.models.calls_sip_options import CallsSipOptions
from infobip_api_client.models.calls_sip_trunk_type import CallsSipTrunkType
from infobip_api_client.models.calls_sip_trunk_update_request import (
    CallsSipTrunkUpdateRequest,
)
from typing import Optional, Set
from typing_extensions import Self


class CallsStaticSipTrunkUpdateRequest(CallsSipTrunkUpdateRequest):
    """
    CallsStaticSipTrunkUpdateRequest
    """  # noqa: E501

    source_hosts: Optional[List[StrictStr]] = Field(
        default=None,
        description="List of SIP trunk source hosts. If empty, destination host list must not be empty. Source hosts can be sent in 2 formats: IP address without port or domain without port.",
        alias="sourceHosts",
    )
    destination_hosts: Optional[List[StrictStr]] = Field(
        default=None,
        description="List of SIP trunk destination hosts. If empty, source host list must not be empty. Destination hosts can be sent in 3 formats: IP address with port, domain name with port or domain name without port. The port must fall in the range 1025-65535 or be 0 for SRV lookup.",
        alias="destinationHosts",
    )
    strategy: Optional[CallsSelectionStrategy] = None
    codecs: Optional[List[CallsAudioCodec]] = Field(
        default=None, description="List of audio codecs supported by a SIP trunk."
    )
    dtmf: Optional[CallsDtmfType] = None
    fax: Optional[CallsFaxType] = None
    anonymization: Optional[CallsAnonymizationType] = None
    number_format: Optional[CallsNumberPresentationFormat] = Field(
        default=None, alias="numberFormat"
    )
    sip_options: Optional[CallsSipOptions] = Field(default=None, alias="sipOptions")
    __properties: ClassVar[List[str]] = [
        "type",
        "name",
        "internationalCallsAllowed",
        "channelLimit",
        "sourceHosts",
        "destinationHosts",
        "strategy",
        "codecs",
        "dtmf",
        "fax",
        "anonymization",
        "numberFormat",
        "sipOptions",
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
        """Create an instance of CallsStaticSipTrunkUpdateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of sip_options
        if self.sip_options:
            _dict["sipOptions"] = self.sip_options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallsStaticSipTrunkUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "type": obj.get("type"),
                "name": obj.get("name"),
                "internationalCallsAllowed": obj.get("internationalCallsAllowed")
                if obj.get("internationalCallsAllowed") is not None
                else False,
                "channelLimit": obj.get("channelLimit"),
                "sourceHosts": obj.get("sourceHosts"),
                "destinationHosts": obj.get("destinationHosts"),
                "strategy": obj.get("strategy"),
                "codecs": obj.get("codecs"),
                "dtmf": obj.get("dtmf"),
                "fax": obj.get("fax"),
                "anonymization": obj.get("anonymization"),
                "numberFormat": obj.get("numberFormat"),
                "sipOptions": CallsSipOptions.from_dict(obj["sipOptions"])
                if obj.get("sipOptions") is not None
                else None,
            }
        )
        return _obj
