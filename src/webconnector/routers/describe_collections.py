import logging
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel
from igenius_adapters_sdk.entities.collection import (
    Collection,
    AttributesSchema,
    Attribute,
    AttributeType,
)

logger = logging.getLogger("webconnector")
logger.setLevel("INFO")

router = APIRouter()


class DescribeCollectionsResponse(BaseModel):
    collections: List[Collection]


class DescribeCollectionsError(Exception):
    pass


@router.post(
    "/collections/actions/describe",
    responses={200: {"description": "Successful response"}},
    response_model=DescribeCollectionsResponse,
)
def describe_collections():
    tc_id_attr = Attribute(
        uid="id",
        type=AttributeType.CATEGORICAL,
        filterable=True,
        sortable=True,
    )
    tc_name_attr = Attribute(
        uid="name",
        type=AttributeType.CATEGORICAL,
        filterable=True,
        sortable=True,
    )
    tc_country_attr = Attribute(
        uid="country",
        type=AttributeType.CATEGORICAL,
        filterable=True,
        sortable=True,
    )
    tc_min_temp_attr = Attribute(
        uid="temp_min",
        type=AttributeType.NUMERIC,
        filterable=True,
        sortable=True,
    )
    tc_max_temp_attr = Attribute(
        uid="temp_max",
        type=AttributeType.NUMERIC,
        filterable=True,
        sortable=True,
    )
    cities_schema = AttributesSchema(
        attributes=[
            tc_id_attr,
            tc_name_attr,
            tc_country_attr,
            tc_min_temp_attr,
            tc_max_temp_attr,
        ]
    )
    top_cities = Collection(
        uid="openweather.cities", attributes_schema=cities_schema
    )
    collections = [top_cities]
    return {
        "collections": collections,
    }