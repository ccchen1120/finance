from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint
import pandas as pd


def call_indices(index_api):

    page_size = 200  # int | The number of results to return (optional) (default to 100)
    next_page = (
        ""  # str | Gets the next page of data from a previous API call (optional)
    )

    try:
        api_response = index_api.get_all_stock_market_indices(
            page_size=page_size, next_page=next_page
        )
        df = pd.DataFrame(api_response.indices_dict)
        print(df)
    except ApiException as e:
        print(
            "Exception when calling IndexApi->get_all_stock_market_indices: %s\r\n" % e
        )


def call_index_lookup(index_api):

    identifier = "$DJI"  # str | An Index Identifier (symbol, Intrinio ID)

    try:
        api_response = index_api.get_stock_market_index_by_id(identifier)
        pprint(api_response)
    except ApiException as e:
        print(
            "Exception when calling IndexApi->get_stock_market_index_by_id: %s\r\n" % e
        )


def call_index_data_point(index_api):

    identifier = "$DJI"  # str | An Index Identifier (symbol, Intrinio ID)
    tag = "level"  # str | An Intrinio data tag ID or code-name

    try:
        api_response = index_api.get_stock_market_index_data_point_number(
            identifier, tag
        )
        pprint(api_response)
    except ApiException as e:
        print(
            "Exception when calling IndexApi->get_stock_market_index_data_point_number: %s\r\n"
            % e
        )


def call_index_historical_data(index_api):

    identifier = "$DJI"  # str | An Index Identifier (symbol, Intrinio ID)
    tag = "level"  # str | An Intrinio data tag ID or code-name
    type = ""  # str | Filter by type, when applicable (optional)
    start_date = (
        "2018-01-01"  # date | Get historical data on or after this date (optional)
    )
    end_date = ""  # date | Get historical data on or before this date (optional)
    sort_order = (
        "desc"  # str | Sort by date `asc` or `desc` (optional) (default to desc)
    )
    page_size = 100  # int | The number of results to return (optional) (default to 100)
    next_page = (
        ""  # str | Gets the next page of data from a previous API call (optional)
    )

    try:
        api_response = index_api.get_stock_market_index_historical_data(
            identifier,
            tag,
            type=type,
            start_date=start_date,
            end_date=end_date,
            sort_order=sort_order,
            page_size=page_size,
            next_page=next_page,
        )
        df = pd.DataFrame(api_response.historical_data_dict)
        print(df)
    except ApiException as e:
        print(
            "Exception when calling IndexApi->get_stock_market_index_historical_data: %s\r\n"
            % e
        )


def call_index_economic_indices(index_api):

    page_size = 100  # int | The number of results to return (optional) (default to 100)
    next_page = (
        ""  # str | Gets the next page of data from a previous API call (optional)
    )

    try:
        api_response = index_api.get_all_economic_indices(
            page_size=page_size, next_page=next_page
        )
        df = pd.DataFrame(api_response.indices_dict)
        print(df)
    except ApiException as e:
        print("Exception when calling IndexApi->get_all_economic_indices: %s\r\n" % e)


def call_index_economic_data_point(index_api):
    identifier = "$GDP"  # str | An Index Identifier (symbol, Intrinio ID)
    tag = "level"  # str | An Intrinio data tag reference [see - https://data.intrinio.com/data-tags/economic]

    try:
        api_response = index_api.get_economic_index_data_point_number(identifier, tag)
        pprint(api_response)
    except ApiException as e:
        print(
            "Exception when calling IndexApi->get_economic_index_data_point_number: %s\r\n"
            % e
        )


def call_index_economic_historical_data(index_api):
    identifier = "$GDP"  # str | An Index Identifier (symbol, Intrinio ID)
    tag = "level"  # str | An Intrinio data tag reference [see - https://data.intrinio.com/data-tags/economic]
    type = ""  # str | Filter by type, when applicable (optional)
    start_date = (
        "2010-01-01"  # date | Get historical data on or after this date (optional)
    )
    end_date = ""  # date | Get historical data on or before this date (optional)
    sort_order = (
        "desc"  # str | Sort by date `asc` or `desc` (optional) (default to desc)
    )
    page_size = 100  # int | The number of results to return (optional) (default to 100)
    next_page = (
        ""  # str | Gets the next page of data from a previous API call (optional)
    )

    try:
        api_response = index_api.get_economic_index_historical_data(
            identifier,
            tag,
            type=type,
            start_date=start_date,
            end_date=end_date,
            sort_order=sort_order,
            page_size=page_size,
            next_page=next_page,
        )
        df = pd.DataFrame(api_response.historical_data_dict)
        print(df)
    except ApiException as e:
        print(
            "Exception when calling IndexApi->get_economic_index_historical_data: %s\r\n"
            % e
        )


def call_index_sic_indices(index_api):

    page_size = 100  # int | The number of results to return (optional) (default to 100)
    next_page = (
        ""  # str | Gets the next page of data from a previous API call (optional)
    )

    try:
        api_response = index_api.get_all_sic_indices(
            page_size=page_size, next_page=next_page
        )
        df = pd.DataFrame(api_response.indices_dict)
        print(df)
    except ApiException as e:
        print("Exception when calling IndexApi->get_all_sic_indices: %s\r\n" % e)
