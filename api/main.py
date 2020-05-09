from company import *
from security import *

sandbox_key = "OmUzZjJjOWU0YWM3Y2U1NTYyYzQyODdkM2I4MzdiODE5"
production_key = "OjU4ZTEyMjFjZDVlOGNjMjA2ZDEwNzBkOGNlZDU1MDU5"

intrinio_sdk.ApiClient().configuration.api_key["api_key"] = sandbox_key

if __name__ == "__main__":

    """
        Company API
    """
    company_api = intrinio_sdk.CompanyApi()

    # callCompanies(company_api)
    # callCompanySearch(company_api)
    # callCompanyLookup(company_api)
    # callCompanyAllSecurities(company_api)
    # callCompanyAllNews(company_api)
    # callCompanyAllFilings(company_api)
    # callCompanyIPOs(company_api)
    # callCompanyDataPoint(company_api)
    # callCompanyHistoricalData(company_api)

    """
        Security API
    """
    security_api = intrinio_sdk.SecurityApi()
    # callSecurities(security_api)
    # callSecurityScreen(security_api)
    # callSecuritySearch(security_api)
    # callSecurityLookup(security_api)
    # callSecurityLookup(security_api)
    # callSecurityStockPrice(security_api)
    # callSecurityRealTimeStockPrice(security_api)
    # callSecurityStockPriceAdjustments(security_api)
    # callSecurityDataPoint(security_api)
    # callSecurityHistoricalData(security_api)
    # callSecurityLatestDividendRecord(security_api)
    # callSecurityLatestEarningsRecord(security_api)
    # callSecurityZacksEPSSurprises(security_api)
    # skip sales surprices
    # skip analyst rating snapshot
    callSecurityZacksAnalystRatings(security_api)
