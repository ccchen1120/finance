from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint
import pandas as pd


def callSecurities(security_api):

    active = True  # bool | When True, return securities that are active. When False, return securities that are not active. A security is considered active if it has traded or has had a corporate action in the past 30 days, and has not been merged into another security (such as due to ticker changes or corporate restructurings). (optional)
    delisted = False  # bool | When True, return securities that have been delisted from their exchange. Note that there may be a newer security for the same company that has been relisted on a differente exchange. When False, return securities that have not been delisted. (optional)
    code = ""  # str | Return securities classified with the given code reference [see - https://docs.intrinio.com/documentation/security_codes]. (optional)
    currency = ""  # str | Return securities traded in the given 3-digit ISO 4217 currency code reference [see - https://en.wikipedia.org/wiki/ISO_4217]. (optional)
    ticker = ""  # str | Return securities traded with the given ticker. Note that securities across the world (and through time) may trade with the same ticker but represent different companies. Use this in conjuction with other parameters for more specificity. (optional)
    name = ""  # str | Return securities with the given text in their name (not case sensitive). (optional)
    composite_mic = ""  # str | Return securities classified under the composite exchange with the given Market Identification Code (MIC). A composite exchange may or may not be a real exchange.  For example, the USCOMP exchange (our only composite exchange to date) is a combination of exchanges with the following MICs: ARCX, XASE, XPOR, FINR, XCIS, XNAS, XNYS, BATS.  This composite grouping is done for user convenience.  At this time, all US securities are classified under the composite exchange with MIC USCOMP.  To query for specific US exchanges, use the exchange_mic parameter below.  (optional)
    exchange_mic = ""  # str | The MIC code of the exchange where the security is actually traded. (optional)
    stock_prices_after = ""  # date | Return securities with end-of-day stock prices on or after this date. (optional)
    stock_prices_before = ""  # date | Return securities with end-of-day stock prices on or before this date. (optional)
    cik = ""  # str | Return securities belonging to the company with the given Central Index Key (CIK). (optional)
    figi = ""  # str | Return securities with the given Exchange Level FIGI reference [see - https://www.openfigi.com/about]. (optional)
    composite_figi = ""  # str | Return securities with the given Country Composite FIGI reference [see - https://www.openfigi.com/about]. (optional)
    share_class_figi = ""  # str | Return securities with the given Global Share Class FIGI reference [see - https://www.openfigi.com/about]. (optional)
    figi_unique_id = ""  # str | Return securities with the given FIGI Unique ID reference [see - https://www.openfigi.com/about]. (optional)
    include_non_figi = False  # bool | When True, include securities that do not have a FIGI. By default, this is False. If this parameter is not specified, only securities with a FIGI are returned. (optional) (default to False)
    page_size = 100  # int | The number of results to return (optional) (default to 100)
    next_page = (
        ""  # str | Gets the next page of data from a previous API call (optional)
    )

    try:
        api_response = security_api.get_all_securities(
            active=active,
            delisted=delisted,
            code=code,
            currency=currency,
            ticker=ticker,
            name=name,
            composite_mic=composite_mic,
            exchange_mic=exchange_mic,
            stock_prices_after=stock_prices_after,
            stock_prices_before=stock_prices_before,
            cik=cik,
            figi=figi,
            composite_figi=composite_figi,
            share_class_figi=share_class_figi,
            figi_unique_id=figi_unique_id,
            include_non_figi=include_non_figi,
            page_size=page_size,
            next_page=next_page,
        )
        df = pd.DataFrame(api_response.securities_dict)
        print(df)
    except ApiException as e:
        print("Exception when calling SecurityApi->get_all_securities: %s\r\n" % e)


def callSecurityScreen(security_api):

    logic = (
        intrinio_sdk.SecurityScreenGroup()
    )  # SecurityScreenGroup | The logic to screen with, consisting of operators, clauses, and nested groups. See screener documentation [see - https://docs.intrinio.com/documentation/screener_v2] for details on how to construct conditions. (optional)
    order_column = (
        "marketcap"  # str | Results returned sorted by this column (optional)
    )
    order_direction = "asc"  # str | Sort order to use with the order_column (optional) (default to asc)
    primary_only = (
        False  # bool | Return only primary securities (optional) (default to False)
    )
    page_size = 100  # int | The number of results to return. Maximum for this endpoint is 50000. (optional) (default to 100)

    try:
        api_response = security_api.screen_securities(
            logic=logic,
            order_column=order_column,
            order_direction=order_direction,
            primary_only=primary_only,
            page_size=page_size,
        )
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityApi->screen_securities: %s\r\n" % e)


def callSecuritySearch(security_api):

    query = "Apple"  # str |
    page_size = 100  # int | The number of results to return (optional) (default to 100)

    try:
        api_response = security_api.search_securities(query, page_size=page_size)
        df = pd.DataFrame(api_response.securities_dict)
        print(df)
    except ApiException as e:
        print("Exception when calling SecurityApi->search_securities: %s\r\n" % e)


def callSecurityLookup(security_api):

    identifier = (
        "AAPL"  # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
    )

    try:
        api_response = security_api.get_security_by_id(identifier)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityApi->get_security_by_id: %s\r\n" % e)


def callSecurityStockPrice(security_api):

    identifier = (
        "AAPL"  # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
    )
    start_date = "2018-01-01"  # date | Return prices on or after the date (optional)
    end_date = "2019-01-01"  # date | Return prices on or before the date (optional)
    frequency = "daily"  # str | Return stock prices in the given frequency (optional) (default to daily)
    page_size = 200  # int | The number of results to return (optional) (default to 100)
    next_page = (
        ""  # str | Gets the next page of data from a previous API call (optional)
    )

    try:
        api_response = security_api.get_security_stock_prices(
            identifier,
            start_date=start_date,
            end_date=end_date,
            frequency=frequency,
            page_size=page_size,
            next_page=next_page,
        )
        df = pd.DataFrame(api_response.stock_prices_dict)
        print(df)
    except ApiException as e:
        print(
            "Exception when calling SecurityApi->get_security_stock_prices: %s\r\n" % e
        )


def callSecurityRealTimeStockPrice(security_api):

    identifier = (
        "AAPL"  # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
    )
    source = ""  # str | Return the realtime price from the specified data source. If no source is specified, the best source available is used. (optional)

    try:
        api_response = security_api.get_security_realtime_price(
            identifier, source=source
        )
        # df = pd.DataFrame(api_response.realtime_price_dict)
        pprint(api_response)
    except ApiException as e:
        print(
            "Exception when calling SecurityApi->get_security_realtime_price: %s\r\n"
            % e
        )


def callSecurityStockPriceAdjustments(security_api):

    identifier = (
        "AAPL"  # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
    )
    start_date = (
        "2000-01-01"  # date | Return price adjustments on or after the date (optional)
    )
    end_date = (
        "2019-01-01"  # date | Return price adjustments on or before the date (optional)
    )
    page_size = 100  # int | The number of results to return (optional) (default to 100)
    next_page = (
        ""  # str | Gets the next page of data from a previous API call (optional)
    )

    try:
        api_response = security_api.get_security_stock_price_adjustments(
            identifier,
            start_date=start_date,
            end_date=end_date,
            page_size=page_size,
            next_page=next_page,
        )
        pprint(api_response)
        df = pd.DataFrame(api_response.stock_price_adjustments_dict)
        print(df)
    except ApiException as e:
        print(
            "Exception when calling SecurityApi->get_security_stock_price_adjustments: %s\r\n"
            % e
        )


def callSecurityDataPoint(security_api):

    identifier = (
        "AAPL"  # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
    )
    tag = "close_price"  # str | An Intrinio data tag ID or code reference [see - https://data.intrinio.com/data-tags]

    try:
        api_response = security_api.get_security_data_point_number(identifier, tag)
        pprint(api_response)
    except ApiException as e:
        print(
            "Exception when calling SecurityApi->get_security_data_point_number: %s\r\n"
            % e
        )


def callSecurityHistoricalData(security_api):

    identifier = (
        "AAPL"  # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
    )
    tag = "adj_close_price"  # str | An Intrinio data tag ID or code reference [see - https://data.intrinio.com/data-tags]
    frequency = "daily"  # str | Return historical data in the given frequency (optional) (default to daily)
    type = ""  # str | Filter by type, when applicable (optional)
    start_date = (
        "2018-01-01"  # date | Get historical data on or after this date (optional)
    )
    end_date = ""  # date | Get historical date on or before this date (optional)
    sort_order = (
        "desc"  # str | Sort by date `asc` or `desc` (optional) (default to desc)
    )
    page_size = 100  # int | The number of results to return (optional) (default to 100)
    next_page = (
        ""  # str | Gets the next page of data from a previous API call (optional)
    )

    try:
        api_response = security_api.get_security_historical_data(
            identifier,
            tag,
            frequency=frequency,
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
            "Exception when calling SecurityApi->get_security_historical_data: %s\r\n"
            % e
        )


def callSecurityLatestDividendRecord(security_api):

    identifier = (
        "AAPL"  # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
    )

    try:
        api_response = security_api.get_security_latest_dividend_record(identifier)
        pprint(api_response)
    except ApiException as e:
        print(
            "Exception when calling SecurityApi->get_security_latest_dividend_record: %s\r\n"
            % e
        )


def callSecurityLatestEarningsRecord(security_api):

    identifier = (
        "AAPL"  # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
    )

    try:
        api_response = security_api.get_security_latest_earnings_record(identifier)
        pprint(api_response)
    except ApiException as e:
        print(
            "Exception when calling SecurityApi->get_security_latest_earnings_record: %s\r\n"
            % e
        )


def callSecurityZacksEPSSurprises(security_api):

    identifier = (
        "AAPL"  # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
    )
    page_size = 100  # int | The number of results to return (optional) (default to 100)
    next_page = (
        ""  # str | Gets the next page of data from a previous API call (optional)
    )

    try:
        api_response = security_api.get_security_zacks_eps_surprises(
            identifier, page_size=page_size, next_page=next_page
        )
        df = pd.DataFrame(api_response.eps_surprises_dict)
        print(df)
    except ApiException as e:
        print(
            "Exception when calling SecurityApi->get_security_zacks_eps_surprises: %s\r\n"
            % e
        )


def callSecurityZacksAnalystRatings(security_api):
    identifier = (
        "AAPL"  # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
    )
    start_date = ""  # str | Limit ratings to those on or after this date (optional)
    end_date = ""  # str | Limit ratings to those on or before this date (optional)
    mean_greater = "~null"  # float | Return only records with a mean (average) higher than this value (optional)
    mean_less = "~null"  # float | Return only records with a mean (average) lower than this value (optional)
    strong_buys_greater = "~null"  # int | Return only records with more than this many Strong Buy recommendations (optional)
    strong_buys_less = "~null"  # int | Return only records with fewer than this many Strong Buy recommendations (optional)
    buys_greater = "~null"  # int | Return only records with more than this many Buy recommendations (optional)
    buys_less = "~null"  # int | Return only records with fewer than this many Buy recommendations (optional)
    holds_greater = "~null"  # int | Return only records with more than this many Hold recommendations (optional)
    holds_less = "~null"  # int | Return only records with fewer than this many Hold recommendations (optional)
    sells_greater = "~null"  # int | Return only records with more than this many Sell recommendations (optional)
    sells_less = "~null"  # int | Return only records with fewer than this many Sell recommendations (optional)
    strong_sells_greater = "~null"  # int | Return only records with more than this many Strong Sell recommendations (optional)
    strong_sells_less = "~null"  # int | Return only records with fewer than this many Strong Sell recommendations (optional)
    total_greater = "~null"  # int | Return only records with more than this many recommendations, regardless of type (optional)
    total_less = "~null"  # int | Return only records with fewer than this many recommendations, regardless of type (optional)
    page_size = 100  # int | The number of results to return (optional) (default to 100)

    try:
        api_response = security_api.get_security_zacks_analyst_ratings(
            identifier, start_date=start_date, end_date=end_date, page_size=page_size,
        )
        df = pd.DataFrame(api_response.analyst_ratings_dict)
        print(df)
    except ApiException as e:
        print(
            "Exception when calling SecurityApi->get_security_zacks_analyst_ratings: %s\r\n"
            % e
        )
