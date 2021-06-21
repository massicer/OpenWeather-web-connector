# OpenWeather-web-connector
[OpenWeather](https://openweathermap.org/api) WebConnector developed for [Crystal](https://crystal.ai/en/) following its official [tutorial](https://webconnectors.crystal.ai/docs/latest/develop_a_webconnector/)


## Available endpoints
- `GET /test_connection`
- `POST /collections/actions/describe`
- `POST /query/actions/execute`


## Supported query
```json
{
    "query": {
        "from_": {
            "datasource_uid": "2b55dd12-9e9b-4bc1-967e-be497abdfc1f",
            "collection_uid": "openweather.cities"
        },
        "where": null,
        "order_by": [
            {
                "alias": "temp_min",
                "direction": "asc"
            },
            {
                "alias": "temp_max",
                "direction": "asc"
            }
        ],
        "limit": 1000,
        "offset": 0,
        "aggregations": [
            {
                "attribute_uri": {
                    "datasource_uid": "2b55dd12-9e9b-4bc1-967e-be497abdfc1f",
                    "collection_uid": "openweather.cities",
                    "attribute_uid": "id"
                },
                "alias": "id",
                "function_uri": {
                    "function_type": "aggregation",
                    "function_uid": "crystal.topics.data.aggregation.identity",
                    "function_params": null
                }
            },
            {
                "attribute_uri": {
                    "datasource_uid": "2b55dd12-9e9b-4bc1-967e-be497abdfc1f",
                    "collection_uid": "openweather.cities",
                    "attribute_uid": "name"
                },
                "alias": "name",
                "function_uri": {
                    "function_type": "aggregation",
                    "function_uid": "crystal.topics.data.aggregation.identity",
                    "function_params": null
                }
            },
            {
                "attribute_uri": {
                    "datasource_uid": "2b55dd12-9e9b-4bc1-967e-be497abdfc1f",
                    "collection_uid": "openweather.cities",
                    "attribute_uid": "country"
                },
                "alias": "country",
                "function_uri": {
                    "function_type": "aggregation",
                    "function_uid": "crystal.topics.data.aggregation.identity",
                    "function_params": null
                }
            },
            {
                "attribute_uri": {
                    "datasource_uid": "2b55dd12-9e9b-4bc1-967e-be497abdfc1f",
                    "collection_uid": "openweather.cities",
                    "attribute_uid": "temp_min"
                },
                "alias": "temp_min",
                "function_uri": {
                    "function_type": "aggregation",
                    "function_uid": "crystal.topics.data.aggregation.identity",
                    "function_params": null
                }
            },
            {
                "attribute_uri": {
                    "datasource_uid": "2b55dd12-9e9b-4bc1-967e-be497abdfc1f",
                    "collection_uid": "openweather.cities",
                    "attribute_uid": "temp_max"
                },
                "alias": "temp_max",
                "function_uri": {
                    "function_type": "aggregation",
                    "function_uid": "crystal.topics.data.aggregation.identity",
                    "function_params": null
                }
            }
        ]
    }
}
```