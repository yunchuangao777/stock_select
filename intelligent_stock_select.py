from openai import AzureOpenAI
import pandas as pd
from web_search_tavily import web_info_search
import os
from urllib.request import urlopen
import certifi
import json
import datetime

pd.set_option("display.max_columns", None)

# Set up OpenAI GPT
endpoint = "https://qb-openai-prod.openai.azure.com/"
model_name = "gpt-4o-mini"
deployment = "gpt-4o-mini"

subscription_key = "13f80d1a54e14e308d8bd151455a756e"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

# FMP code
BASE_URL = os.getenv("THETADATA_BASE_URL", "http://127.0.0.1:25510/v2")
fmp_api_key = '5e00669b034f65774bb1a08cae2781e9'

# ----------------------------------------------------------------------------------------------------------------------
# Calls GPT and returns crypto related stocks;
def get_crypto_stock_list():

    response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Your job is to find the stocks which are requested by user input."
                               "Return the stock names and tickers only.",
                },
                {
                    "role": "user",
                    "content": "Find top 10 crypto-related stocks. Find stocks in US market only.",
                }
            ],
            max_tokens= 4096,
            temperature= 1.0,
            top_p= 1.0,
            model= deployment,

    )

    answer = response.choices[0].message.content

    return {'msg':'top crypto stock list', 'data':answer}


# ----------------------------------------------------------------------------------------------------------------------
# Calls GPT and returns the answers;
# Ask GPT to extract stock names and tickers;
def get_pelosi_stock_list():

    df_web_info = web_info_search(_query="Find all stock names and tickers from Congressman Pelosi's US stock investment portfolio since 2025")
    # df_web_info = web_info_search(_query="Find 8 top Nancy Pelosi stocks to buy.")

    str_input = ''

    for idx in range(len(df_web_info)):
        str_input += df_web_info.iloc[idx]['title']
        str_input += '.'
        str_input += df_web_info.iloc[idx]['content']
        str_input += '.'

    response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Your job is to find the stocks from user input."
                               "Return the stock names and tickers only.",
                },
                {
                    "role": "user",
                    "content": str_input,
                }
            ],
            max_tokens= 4096,
            temperature= 1.0,
            top_p= 1.0,
            model= deployment,

    )

    answer = response.choices[0].message.content

    return {'msg':'pelosi 2025 stock list', 'data':answer}


# ----------------------------------------------------------------------------------------------------------------------
# Calls GPT and returns two sigma stock positions;
def get_twosigma_stock_list():

    df_web_info = web_info_search(_query="Find Two Sigma's top stock and ETF positions as of July 2025, accoding to stockzoa.com.")

    str_input = ''

    for idx in range(len(df_web_info)):
        str_input += df_web_info.iloc[idx]['title']
        str_input += '.'
        str_input += df_web_info.iloc[idx]['content']
        str_input += '.'

    response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Your job is to find the stocks from user input."
                               "Return the stock names and tickers only.",
                },
                {
                    "role": "user",
                    "content": str_input,
                }
            ],
            max_tokens= 4096,
            temperature= 1.0,
            top_p= 1.0,
            model= deployment,

    )

    answer = response.choices[0].message.content

    return {'msg':'two sigma stock list', 'data':answer}


# ----------------------------------------------------------------------------------------------------------------------
# Calls GPT and returns AI concept stocks;
def get_ai_concept_stock_list():

    df_web_info = web_info_search(_query="Find AI concept stocks as of July 2025, accoding to stockzoa.com.")

    str_input = ''

    for idx in range(len(df_web_info)):
        str_input += df_web_info.iloc[idx]['title']
        str_input += '.'
        str_input += df_web_info.iloc[idx]['content']
        str_input += '.'

    response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Your job is to find the stocks from user input."
                               "Return the stock names and tickers only.",
                },
                {
                    "role": "user",
                    "content": str_input,
                }
            ],
            max_tokens= 4096,
            temperature= 1.0,
            top_p= 1.0,
            model= deployment,

    )

    answer = response.choices[0].message.content

    return {'msg':'AI concept stock list', 'data':answer}

# ----------------------------------------------------------------------------------------------------------------------
# Calls GPT and returns Ethereum concept stocks;
def get_ethereum_concept_stock_list():

    df_web_info = web_info_search(_query="Find top 10 Ethereum concept stocks as of July 2025, accoding to stockzoa.com.")

    str_input = ''

    for idx in range(len(df_web_info)):
        str_input += df_web_info.iloc[idx]['title']
        str_input += '.'
        str_input += df_web_info.iloc[idx]['content']
        str_input += '.'

    response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Your job is to find the stocks from user input."
                               "Return the stock names and tickers only.",
                },
                {
                    "role": "user",
                    "content": str_input,
                }
            ],
            max_tokens= 4096,
            temperature= 1.0,
            top_p= 1.0,
            model= deployment,

    )

    answer = response.choices[0].message.content

    return {'msg':'Ethereum concept stock list', 'data':answer}

# ----------------------------------------------------------------------------------------------------------------------
# Calls GPT and returns Ethereum concept stocks;
def get_trump_stock_list():

    df_web_info = web_info_search(_query="Find top 10 Trump's stock list as of July 2025, accoding to stockzoa.com.")

    str_input = ''

    for idx in range(len(df_web_info)):
        str_input += df_web_info.iloc[idx]['title']
        str_input += '.'
        str_input += df_web_info.iloc[idx]['content']
        str_input += '.'

    response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Your job is to find the stocks from user input."
                               "Return the stock names and tickers only.",
                },
                {
                    "role": "user",
                    "content": str_input,
                }
            ],
            max_tokens= 4096,
            temperature= 1.0,
            top_p= 1.0,
            model= deployment,

    )

    answer = response.choices[0].message.content

    return {'msg':'Trump stock list', 'data':answer}

# ----------------------------------------------------------------------------------------------------------------------
def get_jsonparsed_data(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")

    return json.loads(data)


# ----------------------------------------------------------------------------------------------------------------------
def get_fmp_big_gainers():

    url = f"https://financialmodelingprep.com/stable/biggest-gainers?apikey={fmp_api_key}"
    data = pd.DataFrame(get_jsonparsed_data(url))

    return data


# ----------------------------------------------------------------------------------------------------------------------
def get_fmp_big_losers():

    url = f"https://financialmodelingprep.com/stable/biggest-losers?apikey={fmp_api_key}"
    data = pd.DataFrame(get_jsonparsed_data(url))

    return data

# ----------------------------------------------------------------------------------------------------------------------
def get_fmp_top_trades_stocks():

    url = f"https://financialmodelingprep.com/stable/most-actives?apikey={fmp_api_key}"
    data = pd.DataFrame(get_jsonparsed_data(url))

    return data

# ----------------------------------------------------------------------------------------------------------------------
def get_fmp_earning_transcript(_symbol='AAPL'):

    # Get year
    _year = datetime.datetime.now().year

    list_quarter = ['4','3','2','1']
    _idx = 0

    data = pd.DataFrame()

    while len(data) == 0:
        _quarter = list_quarter[_idx]
        _idx += 1

        # Get earning transcript list
        url = f"https://financialmodelingprep.com/stable/earning-call-transcript?symbol={_symbol}&year={_year}&quarter={_quarter}&apikey={fmp_api_key}"
        data = pd.DataFrame(get_jsonparsed_data(url))

    if len(data)==0:
        return pd.DataFrame()
    else:
        return data

# ----------------------------------------------------------------------------------------------------------------------
def get_fmp_company_profile(_symbol='AAPL'):

    url = f"https://financialmodelingprep.com/stable/profile?symbol={_symbol}&apikey={fmp_api_key}"
    data = pd.DataFrame(get_jsonparsed_data(url))

    return data


# ----------------------------------------------------------------------------------------------------------------------
def get_fmp_stock_news(_symbol='TSLA', _line=3):

    # Get top lines of news;
    data = []

    # Get first three pages of news; sometimes there is no news on first page;
    for _page in range(10):
        url = f"https://financialmodelingprep.com/stable/news/stock-latest?page={_page}&limit=250&apikey={fmp_api_key}"
        data_tmp = pd.DataFrame(get_jsonparsed_data(url))
        data_tmp = data_tmp[data_tmp['symbol']==_symbol]

        data.append(data_tmp)
    
    # Concat the news;
    data = pd.concat(data)
    data = data.head(_line)
    
    return data

# ----------------------------------------------------------------------------------------------------------------------
def get_fmp_insider_trades(_symbol='TSLA', _line=10):

    # Get top lines of insider trades;
    data = []

    # Get first three pages of tardes; sometimes there is no trade on first page;
    for _page in range(10):
        url = f"https://financialmodelingprep.com/stable/insider-trading/search?page={_page}&limit=200&symbol={_symbol}&apikey={fmp_api_key}"
        data_tmp = pd.DataFrame(get_jsonparsed_data(url))

        data.append(data_tmp)
    
    # Concat the trades;
    data = pd.concat(data)
    data = data.head(_line)
    
    return data

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    answer = get_fmp_insider_trades()
    print(answer)
