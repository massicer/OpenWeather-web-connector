import logging
from typing import Union

from fastapi import APIRouter
from pydantic import BaseModel

logger = logging.getLogger("webconnector")
logger.setLevel("INFO")

router = APIRouter()


class CheckConnectionResponse(BaseModel):
    outcome: str


class CheckConnectionFailResponse(CheckConnectionResponse):
    details: str


@router.get(
    "/test_connection",
    responses={
        200: {
            "description": (
                "Successful response, the Web Connector is ready to accept requests."
            )
        }
    },
    response_model=Union[CheckConnectionFailResponse, CheckConnectionResponse],
)
def test_connection():
    logger.info("Checking connection...")

    return {"outcome": "success"}