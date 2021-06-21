.PHONY: install
install: # install the poetry project package itself plus its dependencies.
	poetry install


.PHONY: start
start: # start the service
	poetry run python src/main.py
	

.PHONY: submit_query
submit_query: # submit the only one implemented query
	curl --location --request POST 'localhost:8080/query/actions/execute' \
	--header 'Content-Type: application/json' \
	--data-raw '{\
			"from_": {\
				"datasource_uid": "2b55dd12-9e9b-4bc1-967e-be497abdfc1f",\
				"collection_uid": "openweather.cities"\
			},\
			"where": null,\
			"order_by": [\
				{\
					"alias": "temp_min",\
					"direction": "asc"\
				},\
				{\
					"alias": "temp_max",\
					"direction": "asc"\
				}\
			],\
			"limit": 1000,\
			"offset": 0,\
			"aggregations": [\
				{\
					"attribute_uri": {\
						"datasource_uid": "2b55dd12-9e9b-4bc1-967e-be497abdfc1f",\
						"collection_uid": "openweather.cities",\
						"attribute_uid": "id"\
					},\
					"alias": "id",\
					"function_uri": {\
						"function_type": "aggregation",\
						"function_uid": "crystal.topics.data.aggregation.identity",\
						"function_params": null\
					}\
				},\
				{\
					"attribute_uri": {\
						"datasource_uid": "2b55dd12-9e9b-4bc1-967e-be497abdfc1f",\
						"collection_uid": "openweather.cities",\
						"attribute_uid": "name"\
					},\
					"alias": "name",\
					"function_uri": {\
						"function_type": "aggregation",\
						"function_uid": "crystal.topics.data.aggregation.identity",\
						"function_params": null\
					}\
				},\
				{\
					"attribute_uri": {\
						"datasource_uid": "2b55dd12-9e9b-4bc1-967e-be497abdfc1f",\
						"collection_uid": "openweather.cities",\
						"attribute_uid": "country"\
					},\
					"alias": "country",\
					"function_uri": {\
						"function_type": "aggregation",\
						"function_uid": "crystal.topics.data.aggregation.identity",\
						"function_params": null\
					}\
				},\
				{\
					"attribute_uri": {\
						"datasource_uid": "2b55dd12-9e9b-4bc1-967e-be497abdfc1f",\
						"collection_uid": "openweather.cities",\
						"attribute_uid": "temp_min"\
					},\
					"alias": "temp_min",\
					"function_uri": {\
						"function_type": "aggregation",\
						"function_uid": "crystal.topics.data.aggregation.identity",\
						"function_params": null\
					}\
				},\
				{\
					"attribute_uri": {\
						"datasource_uid": "2b55dd12-9e9b-4bc1-967e-be497abdfc1f",\
						"collection_uid": "openweather.cities",\
						"attribute_uid": "temp_max"\
					},\
					"alias": "temp_max",\
					"function_uri": {\
						"function_type": "aggregation",\
						"function_uid": "crystal.topics.data.aggregation.identity",\
						"function_params": null\
					}\
				}\
			]\
	}'