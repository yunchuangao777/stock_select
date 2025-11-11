#!C:\Users\gaoyu\Documents\vsc\stock_select\stock_select_env\Scripts\python.exe
import requests
import pandas as pd

def web_info_search(_query='',
                    _chunk_per_source=3,
                    _max_result=10,
                    _days=10,
                    _include_domains=[],
                    _exclude_domains=[]):

    url = "https://api.tavily.com/search"

    payload = {
        "query": _query,
        "topic": "general",  # news
        "search_depth": "basic",  # advanced
        "chunks_per_source": _chunk_per_source,
        "max_results": _max_result,
        "time_range": None,
        "days": _days,
        "include_answer": True,
        "include_raw_content": False,
        "include_images": False,
        "include_image_descriptions": False,
        "include_domains": _include_domains,
        "exclude_domains": _exclude_domains
    }
    headers = {
        "Authorization": "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",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    df_response  = pd.json_normalize(response.json()['results'])

    return df_response
