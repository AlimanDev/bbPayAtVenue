URL = 'https://www.treatwell.co.uk/checkout-api/basket'

HEADER_STR = """
Accept:
*/*
Accept-Encoding:
gzip, deflate, br
Accept-Language:
ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7
Content-Length:
144
Content-Type:
application/json
Cookie:
tw_user_id=7bab913e-f125-4cb0-9e80-0fd68800d468; _gid=GA1.3.694917945.1697094534; OptanonAlertBoxClosed=2023-10-12T07:08:54.117Z; __stripe_mid=6c50c1c6-92a5-461c-a80d-ff77342e4ff8b480b9; __qca=P0-1588799515-1697094533865; fe20-flipper-id=f12c17c9-1099-4969-ae87-12c46179f4ab; _fbp=fb.2.1697094654832.1321180772; _gcl_au=1.1.643625378.1697094656; _hjSessionUser_598977=eyJpZCI6IjA3OWIwNzkyLTAwOGQtNWJiMC04MjQxLTA1ZTA2M2E5ZGQ4MCIsImNyZWF0ZWQiOjE2OTcwOTQ1MzM4NDYsImV4aXN0aW5nIjp0cnVlfQ==; _pin_unauth=dWlkPVpqUTVaREF4WVRVdE1EUm1aQzAwTmpVeUxXSmlNMkV0TTJVME9EVmhZak0wWlRZNQ; datetimeui-flipper-id=961863a7-eb5e-45fa-a7c2-fe7c3984cf5a; _ga_THX7G9EBE3=deleted; _ga_THX7G9EBE3=GS1.1.1697099975.2.0.1697099975.0.0.0; cto_bundle=vDFHGl9ITDVEVFAwcGw1WnF3WVhSUkNlN3JScFA0T1dJR1Q0aElNSEpLTEFWdmFHZ1BscUxPbE54SDVwVkdwSjNCT1drcVZuRGk0UUF6cUJ0cjA3bWZzUDRhSXcyUUZZbTlLam5PMW1sQ2IlMkJ4TjJSUzJFamxUVyUyRkcxTmkxY1RPVVVCM0IlMkZBQWlMa2pZWHh1bW1OTEdmd2EyOVFOcjg0YkhTZ0lNTDIydUpUNUk1Sk0lM0Q; _uetsid=7ce6db8068ce11ee928e1daf215223e2; _uetvid=7ce6e64068ce11eea1e9c7ba6affae8b; _hjIncludedInSessionSample_598977=0; __stripe_sid=b3f4b508-fa3b-421a-85e9-1b1a260a73d3650ee0; _sp_ses.500d=*; _ga=GA1.1.1840440513.1697094533; _hjSession_598977=eyJpZCI6IjM4OGJjOGRjLWM2NDctNGYxNi05M2Q0LWI2NGQ0MDZhZjVmOCIsImNyZWF0ZWQiOjE2OTcxMTkyMzY1MzEsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9; _hjAbsoluteSessionInProgress=0; _sp_id.500d=b2a588d7-c15d-4d36-ad2c-85e74c1e7c58.1697094533.5.1697120138.1697114066.6c020a38-571f-484d-a811-87d3d2c7f4c8; _ga_123456789=GS1.1.1697119233.5.1.1697120740.0.0.0; _ga_X88YE4VNNY=GS1.1.1697119233.5.0.1697120740.60.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Oct+12+2023+19%3A25%3A40+GMT%2B0500+(%D0%A3%D0%B7%D0%B1%D0%B5%D0%BA%D0%B8%D1%81%D1%82%D0%B0%D0%BD%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202209.1.0&isIABGlobal=false&hosts=&consentId=a4280728-09fc-4476-ad46-959c8165add3&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=%3B&AwaitingReconsent=false
Origin:
https://www.treatwell.co.uk
Referer:
https://www.treatwell.co.uk/secure-checkout?venueId=404963&offers=%5B%7B%22offerId%22%3A3415917%2C%22fulfillment%22%3A%22APPOINTMENT%22%2C%22skus%22%3A%5B%7B%22skuId%22%3A5966215%7D%5D%7D%5D&date=2023-10-18&time=800
Sec-Ch-Ua:
"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"
Sec-Ch-Ua-Mobile:
?0
Sec-Ch-Ua-Platform:
"Windows"
Sec-Fetch-Dest:
empty
Sec-Fetch-Mode:
cors
Sec-Fetch-Site:
same-origin
User-Agent:
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36
"""