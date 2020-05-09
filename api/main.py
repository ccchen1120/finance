from company import *
from security import *
import intrinio_sdk

sandbox_key = "OmUzZjJjOWU0YWM3Y2U1NTYyYzQyODdkM2I4MzdiODE5"
production_key = "OjU4ZTEyMjFjZDVlOGNjMjA2ZDEwNzBkOGNlZDU1MDU5"

intrinio_sdk.ApiClient().configuration.api_key["api_key"] = sandbox_key

if __name__ == "__main__":

    """
        Company API
    """
    company_api = intrinio_sdk.CompanyApi()

    call_companies(company_api)
    # call_company_search(company_api)
    # call_company_lookup(company_api)
    # call_company_all_securities(company_api)
    # call_company_all_news(company_api)
    # call_company_all_filings(company_api)
    # call_company_ipos(company_api)
    # call_company_data_point(company_api)
    # call_company_historical_data(company_api)

    """
        Security API
    """
    security_api = intrinio_sdk.SecurityApi()
    # call_securities(security_api)
    # call_security_screen(security_api)
    # call_security_search(security_api)
    # call_security_lookup(security_api)
    # call_security_stock_price(security_api)
    # call_security_realtime_stock_price(security_api)
    # call_security_stock_price_adjustments(security_api)
    # call_security_data_point(security_api)
    # call_security_historical_data(security_api)
    # call_security_latest_dividend_record(security_api)
    # call_security_latest_earnings_record(security_api)
    # call_security_zacks_eps_surprises(security_api)
    # skip sales surprices
    # skip analyst rating snapshot
    # call_security_zacks_analyst_ratings(security_api)
