from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint
import pandas as pd

sandbox_key = "OmUzZjJjOWU0YWM3Y2U1NTYyYzQyODdkM2I4MzdiODE5"
production_key = "OjU4ZTEyMjFjZDVlOGNjMjA2ZDEwNzBkOGNlZDU1MDU5"

intrinio_sdk.ApiClient().configuration.api_key["api_key"] = sandbox_key


def callCompanies(company_api):

    latest_filing_date = ""  # date | Return companies whose latest 10-Q or 10-K was filed on or after this date (optional)
    sic = ""  # str | Return companies with the given Standard Industrial Classification code (optional)
    template = ""  # str | Return companies with the given financial statement template (optional)
    sector = ""  # str | Return companies in the given industry sector (optional)
    industry_category = (
        ""  # str | Return companies in the given industry category (optional)
    )
    industry_group = ""  # str | Return companies in the given industry group (optional)
    has_fundamentals = (
        True  # bool | Return only companies that have fundamentals when True (optional)
    )
    has_stock_prices = (
        True  # bool | Return only companies that have stock prices when True (optional)
    )
    page_size = 100  # int | The number of results to return (optional) (default to 100)
    next_page = (
        ""  # str | Gets the next page of data from a previous API call (optional)
    )

    try:
        api_response = company_api.get_all_companies(
            latest_filing_date=latest_filing_date,
            sic=sic,
            template=template,
            sector=sector,
            industry_category=industry_category,
            industry_group=industry_group,
            has_fundamentals=has_fundamentals,
            has_stock_prices=has_stock_prices,
            page_size=page_size,
            next_page=next_page,
        )

        df = pd.DataFrame(api_response.companies_dict)
        print(df)
    except ApiException as e:
        print("Exception when calling CompanyApi->get_all_companies: %s\n" % e)


def callCompanySearch(company_api):

    query = "Apple"  # str | Search parameters
    page_size = 100  # int | The number of results to return (optional) (default to 100)

    try:
        api_response = company_api.search_companies(query, page_size=page_size)
        df = pd.DataFrame(api_response.companies_dict)
        print(df)
    except ApiException as e:
        print("Exception when calling CompanyApi->search_companies: %s\r\n" % e)


def callCompanyLookup(company_api):

    identifier = "AAPL"  # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)

    try:
        api_response = company_api.get_company(identifier)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CompanyApi->get_company: %s\r\n" % e)


def callCompanyAllSecurities(company_api):
    identifier = "AAPL"  # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
    next_page = (
        ""  # str | Gets the next page of data from a previous API call (optional)
    )

    try:
        api_response = company_api.get_company_securities(
            identifier, next_page=next_page
        )
        pprint(api_response)
        df = pd.DataFrame(api_response.securities_dict)
        print(df)
    except ApiException as e:
        print("Exception when calling CompanyApi->get_company_securities: %s\r\n" % e)


def callCompanyAllNews(company_api):

    identifier = "AAPL"  # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
    page_size = 100  # int | The number of results to return (optional) (default to 100)
    next_page = (
        ""  # str | Gets the next page of data from a previous API call (optional)
    )

    try:
        api_response = company_api.get_company_news(
            identifier, page_size=page_size, next_page=next_page
        )
        df = pd.DataFrame(api_response.news_dict)
        print(df)
    except ApiException as e:
        print("Exception when calling CompanyApi->get_company_news: %s\r\n" % e)


def callCompanyAllFilings(company_api):
    identifier = "AAPL"  # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
    report_type = ""  # str | Filter by report type [see - https://docs.intrinio.com/documentation/sec_filing_report_types]. Separate values with commas to return multiple report types. (optional)
    start_date = "2015-01-01"  # date | Filed on or after the given date (optional)
    end_date = ""  # date | Filed before or after the given date (optional)
    page_size = 100  # int | The number of results to return (optional) (default to 100)
    next_page = (
        ""  # str | Gets the next page of data from a previous API call (optional)
    )

    try:
        api_response = company_api.get_company_filings(
            identifier,
            report_type=report_type,
            start_date=start_date,
            end_date=end_date,
            page_size=page_size,
            next_page=next_page,
        )
        pprint(api_response)
        df = pd.DataFrame(api_response.filings_dict)
        print(df)
    except ApiException as e:
        print("Exception when calling CompanyApi->get_company_filings: %s\r\n" % e)


def callCompanyIPOs(company_api):

    ticker = ""  # str | Return IPOs with the given ticker (typically the IPO for the company) (optional)
    status = ""  # str | Return IPOs with the given status. Upcoming IPOs are scheduled to occur in the future. Priced IPOs have occured and the company should be trading publicly. Withdrawn IPOs were planned to occurr but were withdrawn beforehand (optional)
    start_date = ""  # date | Return IPOs on or after the given date (optional)
    end_date = ""  # date | Return IPOs on or before the given date (optional)
    offer_amount_greater_than = "~null"  # int | Return IPOs with an offer dollar amount greater than the given amount (optional)
    offer_amount_less_than = "~null"  # int | Return IPOs with an offer dollar amount less than the given amount (optional)
    page_size = 100  # int | The number of results to return (optional) (default to 100)
    next_page = (
        ""  # str | Gets the next page of data from a previous API call (optional)
    )

    try:
        api_response = company_api.get_company_ipos(
            ticker=ticker,
            status=status,
            start_date=start_date,
            end_date=end_date,
            page_size=page_size,
            next_page=next_page,
        )
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CompanyApi->get_company_ipos: %s\r\n" % e)


def callCompanyDataPoint(company_api):

    identifier = "AAPL"  # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
    tag = "marketcap"  # str | An Intrinio data tag ID or code reference [see - https://data.intrinio.com/data-tags]

    try:
        api_response = company_api.get_company_data_point_number(identifier, tag)
        pprint(api_response)
    except ApiException as e:
        print(
            "Exception when calling CompanyApi->get_company_data_point_number: %s\r\n"
            % e
        )


def callCompanyHistoricalData(company_api):
    identifier = "AAPL"  # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
    tag = "marketcap"  # str | An Intrinio data tag ID or code reference [see - https://data.intrinio.com/data-tags]
    frequency = "daily"  # str | Return historical data in the given frequency (optional) (default to daily)
    type = ""  # str | Return historical data for given fiscal period type (optional)
    start_date = (
        "2018-01-01"  # date | Return historical data on or after this date (optional)
    )
    end_date = ""  # date | Return historical data on or before this date (optional)
    sort_order = (
        "desc"  # str | Sort by date `asc` or `desc` (optional) (default to desc)
    )
    page_size = 100  # int | The number of results to return (optional) (default to 100)
    next_page = (
        ""  # str | Gets the next page of data from a previous API call (optional)
    )

    try:
        api_response = company_api.get_company_historical_data(
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
        # TODO plot time-series
    except ApiException as e:
        print(
            "Exception when calling CompanyApi->get_company_historical_data: %s\r\n" % e
        )
