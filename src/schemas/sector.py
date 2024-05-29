from pydantic import BaseModel, Field


class Sector(BaseModel):
    sector: str = Field(..., title="Sector name", serialization_alias="sector")
    day_return: str = Field(..., title="Day return", serialization_alias="dayReturn")
    ytd_return: str = Field(..., title="Year to date return", serialization_alias="ytdReturn")
    year_return: str = Field(..., title="Year return", serialization_alias="yearReturn")
    three_year_return: str = Field(..., title="Three year return", serialization_alias="threeYearReturn")
    five_year_return: str = Field(..., title="Five year return", serialization_alias="fiveYearReturn")

    def dict(self, *args, **kwargs):
        base_dict = super().dict(*args, **kwargs, exclude_none=True, by_alias=True)
        return {k: v for k, v in base_dict.items() if v is not None}
