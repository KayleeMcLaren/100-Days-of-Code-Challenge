
import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

# URL for Amazon product you want to track the price of
url = "https://www.amazon.com/Sennheiser-Game-ONE-Gaming-Headset/dp/B00KK8ZLEC/ref=sxin_15?asc_contentid=amzn1.osa.29b3fa6d-7914-4b93-8f9b-98238d438181.ATVPDKIKX0DER.en_US&asc_contenttype=article&ascsubtag=amzn1.osa.29b3fa6d-7914-4b93-8f9b-98238d438181.ATVPDKIKX0DER.en_US&creativeASIN=B00KK8ZLEC&cv_ct_cx=gaming+headsets&cv_ct_id=amzn1.osa.29b3fa6d-7914-4b93-8f9b-98238d438181.ATVPDKIKX0DER.en_US&cv_ct_pg=search&cv_ct_we=asin&cv_ct_wn=osp-single-source-pecos-desktop&dchild=1&keywords=gaming+headsets&linkCode=oas&pd_rd_i=B00KK8ZLEC&pd_rd_r=7504de68-de1e-47f1-9220-5849dea7e4c5&pd_rd_w=JP2Hx&pd_rd_wg=qNcIL&pf_rd_i=23508887011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=05ad5af5-c700-4e1b-92d5-aeafaae3e0ed&pf_rd_r=08WXS2EFPHKS3M5Q3XCY&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1633347381&sr=1-1-c26ac7f6-b43f-4741-a772-17cad7536576&tag=tgl0a3-20"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,en-ZA;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

# Get the price of the product
price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

# Get the name of the product
title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 125

# Check product price and send email if lower than BUY_PRICE
if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
        
