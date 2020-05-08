from company import *

if __name__ == "__main__":

    company_api = intrinio_sdk.CompanyApi()

    # callCompanies(company_api)
    # callCompanySearch(company_api)
    # callCompanyLookup(company_api)
    # callCompanyAllSecurities(company_api)
    # callCompanyAllNews(company_api)
    # callCompanyAllFilings(company_api)

    # callCompanyIPOs(company_api)
    # callCompanyDataPoint(company_api)
    callCompanyHistoricalData(company_api)
