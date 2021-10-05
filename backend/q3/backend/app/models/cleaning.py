from typing import Optional
from enum import Enum
import datetime

from app.models.core import IDModelMixin, CoreModel


class CleaningType(str, Enum):
    dust_up = "dust_up"
    spot_clean = "spot_clean"
    full_clean = "full_clean"


class CleaningBase(CoreModel):
    """
    All common characteristics of our Cleaning resource
    """
    data: str = str(datetime.datetime.now().date())
    hora: str = datetime.datetime.now().hour
    cleaning_type: Optional[CleaningType] = "spot_clean"


class CleaningCreate(CleaningBase):
    data:  str = str(datetime.datetime.now().date())
    hora: str


class CleaningUpdate(CleaningBase):
    cleaning_type: Optional[CleaningType]


class CleaningInDB(IDModelMixin, CleaningBase):
    data:  str = str(datetime.datetime.now().date())
    hora: str
    cleaning_type: CleaningType


class CleaningPublic(IDModelMixin, CleaningBase):
    pass

