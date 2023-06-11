from __future__ import annotations

from pydantic import BaseModel
from typing import Optional



class AmountModel(BaseModel):
	currency: str
	value: str


class StatusModel(BaseModel):
	value: str
	changedDateTime: str


class CustomFieldsModel(BaseModel):
	invoiceUid: str


class RecipientModel(BaseModel):
	requisitesType: str
	requisitesValue: str



class Response(BaseModel):
	siteId: str
	billId: str
	amount: AmountModel
	status: StatusModel
	customFields: CustomFieldsModel
	creationDateTime: str
	expirationDateTime: str
	payUrl: str
	recipientPhoneNumber: str
	recipient: RecipientModel = None





