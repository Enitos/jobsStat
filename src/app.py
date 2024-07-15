import json, requests
import aiohttp
import asyncio

async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data 


async def main():
    url = "https://api-omt.gov.cv/jobs"
    base_url="https://api-omt.gov.cv"
    save_file = open("jobs_maio.json", "w", encoding='utf-8')
    results = []
    while url is not None:
        data = await fetch_json(url)
        results += data['data']
        next_url = data['pagination']['next']
        if next_url is not None:
            url = base_url+next_url
        else:
            url = None
    json.dump(results, save_file, ensure_ascii=False, indent=6)
    return results

asyncio.run(main())
# url = "https://api-omt.gov.cv/jobs"
# base_url="https://api-omt.gov.cv"
# results = []
# while url is not None:
#     data = await fetch_json(url)
#     results += data['data']
#     next_url = data['pagination']['next']
#     if next_url is not None:
#         url = base_url+next_url