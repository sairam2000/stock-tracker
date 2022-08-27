# stock-tracker
Django + Django-Rest-Framework + Django-Channels + Redis + Celery + Celery-beat + Docker + Docker-Compose


# API endpoints
## GET
`Nifty-50 stocks` http://localhost:8000/getStocks/ <br/>

Response
```
{
    "stocks": [
        "APOLLOHOSP.NS",
        "BAJAJ-AUTO.NS",
        "BAJAJFINSV.NS",
        "BAJFINANCE.NS",
        "BHARTIARTL.NS",
        "BRITANNIA.NS",
        "CIPLA.NS",
        "COALINDIA.NS",
        "HDFCLIFE.NS",
        "HEROMOTOCO.NS",
        "HINDALCO.NS",
        "ICICIBANK.NS",
        "INDUSINDBK.NS",
        "ITC.NS",
        "KOTAKBANK.NS",
        "LT.NS",
        "MARUTI.NS",
        "MM.NS",
        "NESTLEIND.NS",
        "NTPC.NS",
        "ONGC.NS",
        "RELIANCE.NS",
        "SHREECEM.NS",
        "TATACONSUM.NS",
        "TATASTEEL.NS",
        "TCS.NS",
        "TECHM.NS",
        "TITAN.NS",
        "ULTRACEMCO.NS",
        "WIPRO.NS"
    ]
}
```


## POST
`Live Stock Prices` http://localhost:8000/getStocksPrice/ <br/>

Request body
```
{
     "stocks": [ "RELIANCE.NS", "CIPLA.NS"]
}
```

Response
```
{
    "stockPrices": {
        "CIPLA.NS": {
            "language": "en-US",
            "region": "US",
            "quoteType": "EQUITY",
            "typeDisp": "Equity",
            "quoteSourceName": "Delayed Quote",
            "triggerable": true,
            "customPriceAlertConfidence": "HIGH",
            "currency": "INR",
            "exchange": "NSI",
            "shortName": "CIPLA LTD",
            "longName": "Cipla Limited",
            "messageBoardId": "finmb_882504",
            "exchangeTimezoneName": "Asia/Kolkata",
            "exchangeTimezoneShortName": "IST",
            "gmtOffSetMilliseconds": 19800000,
            "marketState": "CLOSED",
            "market": "in_market",
            "esgPopulated": false,
            "regularMarketChangePercent": -0.4825749,
            "regularMarketPrice": 1020.8,
            "firstTradeDateMilliseconds": 820467900000,
            "priceHint": 2,
            "regularMarketChange": -4.950012,
            "regularMarketTime": 1661507998,
            "regularMarketDayHigh": 1035.7,
            "regularMarketDayRange": "1018.5 - 1035.7",
            "regularMarketDayLow": 1018.5,
            "regularMarketVolume": 1264040,
            "regularMarketPreviousClose": 1025.75,
            "bid": 0.0,
            "ask": 0.0,
            "bidSize": 0,
            "askSize": 0,
            "fullExchangeName": "NSE",
            "financialCurrency": "INR",
            "regularMarketOpen": 1030.9,
            "averageDailyVolume3Month": 1539545,
            "averageDailyVolume10Day": 1167530,
            "fiftyTwoWeekLowChange": 170.79999,
            "fiftyTwoWeekLowChangePercent": 0.20094116,
            "fiftyTwoWeekRange": "850.0 - 1083.0",
            "fiftyTwoWeekHighChange": -62.200012,
            "fiftyTwoWeekHighChangePercent": -0.05743307,
            "fiftyTwoWeekLow": 850.0,
            "fiftyTwoWeekHigh": 1083.0,
            "earningsTimestamp": 1659092340,
            "earningsTimestampStart": 1666695540,
            "earningsTimestampEnd": 1667044800,
            "trailingAnnualDividendRate": 0.0,
            "trailingPE": 33.37038,
            "trailingAnnualDividendYield": 0.0,
            "epsTrailingTwelveMonths": 30.59,
            "epsForward": 47.34,
            "epsCurrentYear": 38.47,
            "priceEpsCurrentYear": 26.534962,
            "sharesOutstanding": 806995968,
            "bookValue": 258.321,
            "fiftyDayAverage": 978.181,
            "fiftyDayAverageChange": 42.618958,
            "fiftyDayAverageChangePercent": 0.043569602,
            "twoHundredDayAverage": 959.61426,
            "twoHundredDayAverageChange": 61.18573,
            "twoHundredDayAverageChangePercent": 0.06376076,
            "marketCap": 823781490688,
            "forwardPE": 21.56316,
            "priceToBook": 3.9516723,
            "sourceInterval": 15,
            "exchangeDataDelayedBy": 15,
            "averageAnalystRating": "1.9 - Buy",
            "tradeable": false,
            "cryptoTradeable": false,
            "symbol": "CIPLA.NS"
        },
        "RELIANCE.NS": {
            "language": "en-US",
            "region": "US",
            "quoteType": "EQUITY",
            "typeDisp": "Equity",
            "quoteSourceName": "Delayed Quote",
            "triggerable": true,
            "customPriceAlertConfidence": "HIGH",
            "currency": "INR",
            "regularMarketChangePercent": -0.5338063,
            "firstTradeDateMilliseconds": 820467900000,
            "priceHint": 2,
            "regularMarketChange": -14.050049,
            "regularMarketTime": 1661508000,
            "regularMarketDayHigh": 2650.0,
            "regularMarketDayRange": "2607.0 - 2650.0",
            "regularMarketDayLow": 2607.0,
            "regularMarketVolume": 4956404,
            "regularMarketPreviousClose": 2632.05,
            "bid": 0.0,
            "ask": 0.0,
            "bidSize": 0,
            "askSize": 0,
            "fullExchangeName": "NSE",
            "financialCurrency": "INR",
            "regularMarketOpen": 2633.0,
            "averageDailyVolume3Month": 7730451,
            "averageDailyVolume10Day": 4010324,
            "fiftyTwoWeekLowChange": 438.0,
            "fiftyTwoWeekLowChangePercent": 0.20091744,
            "fiftyTwoWeekRange": "2180.0 - 2856.15",
            "fiftyTwoWeekHighChange": -238.1499,
            "fiftyTwoWeekHighChangePercent": -0.083381444,
            "fiftyTwoWeekLow": 2180.0,
            "fiftyTwoWeekHigh": 2856.15,
            "trailingAnnualDividendRate": 0.0,
            "trailingPE": 29.980648,
            "trailingAnnualDividendYield": 0.0,
            "epsTrailingTwelveMonths": 87.323,
            "epsForward": 71.85,
            "sharesOutstanding": 6765989888,
            "bookValue": 1132.233,
            "fiftyDayAverage": 2520.432,
            "fiftyDayAverageChange": 97.568115,
            "fiftyDayAverageChangePercent": 0.03871087,
            "twoHundredDayAverage": 2502.933,
            "twoHundredDayAverageChange": 115.066895,
            "twoHundredDayAverageChangePercent": 0.04597282,
            "marketCap": 17713361584128,
            "forwardPE": 36.437023,
            "priceToBook": 2.312245,
            "sourceInterval": 15,
            "exchangeDataDelayedBy": 15,
            "averageAnalystRating": "2.1 - Buy",
            "tradeable": false,
            "cryptoTradeable": false,
            "exchange": "NSI",
            "shortName": "RELIANCE INDS",
            "longName": "Reliance Industries Limited",
            "messageBoardId": "finmb_878373",
            "exchangeTimezoneName": "Asia/Kolkata",
            "exchangeTimezoneShortName": "IST",
            "gmtOffSetMilliseconds": 19800000,
            "market": "in_market",
            "esgPopulated": false,
            "regularMarketPrice": 2618.0,
            "marketState": "CLOSED",
            "symbol": "RELIANCE.NS"
        }
    }
}
```

## WEB-SOCKETS
`Get Latest Prices For Every 10 Seconds`  <br/>
```
ws = new WebSocket('ws://localhost:8000/ws/stock/track/?stocks=RELIANCE.NS&stocks=BAJAJFINSV.NS')
ws.onmessage = (e) => {console.log(e.data)}
```


