import http.client
import json
from typing import Any, Dict, List
import os

from fastapi import APIRouter, Header
from igenius_adapters_sdk.entities.query import Query
from pydantic import BaseModel  


APP_ID = os.environ.get('OPEN_WEATHER_API_KEY')

router = APIRouter()


class ConnectionParamsRequest(BaseModel):
    token: str


class ExecuteQueryError(Exception):
    pass


class ExecuteQueryResponse(BaseModel):
    records: List[Dict[str, Any]]


@router.post(
    "/query/actions/execute",
    responses={200: {"description": "Successful response"}},
    response_model=ExecuteQueryResponse,
)
def execute_query(
    query: Query,
    x_api_key: str = Header(None),
):
    fields = [
        aggregation.attribute_uri.attribute_uid for aggregation in query.aggregations
    ]

    with open("./assets/city.list.json") as json_file:
        data = [
            {"id": record["id"], "name": record["name"], "country": record["country"]}
            for record in json.load(json_file)[:10]
        ]

    records = []
    for city in data:
        conn = http.client.HTTPSConnection("api.openweathermap.org")
        conn.request("GET", f"/data/2.5/weather?id={city['id']}&appid={APP_ID}", "", {})
        res = conn.getresponse()
        response_data = res.read()
        response = json.loads(response_data.decode("utf-8"))

        complete_record = {
            "id": city["id"],
            "name": city["name"],
            "country": city["country"],
            "temp_min": response.get("main", {}).get("temp_min", 0),
            "temp_max": response.get("main", {}).get("temp_max", 0),
        }

        record = {key: complete_record[key] for key in fields}
        records.append(record)

    if query.order_by:
        for sorting_option in query.order_by:
            records = sorted(
                records,
                key=lambda k: k[sorting_option.alias],
                reverse=True if sorting_option.direction == "desc" else False,
            )

    return {"records": records}