from fastapi import APIRouter
from models.index import News


newsApi = APIRouter()
news = News()


@newsApi.get('/news/', tags=['News'])
async def all_news():
    return "Welcome to Sri Lankan News Api"


@newsApi.get('/news/dailymirror', tags=['News'])
async def daily_mirror():
    return news.daily_mirror()


@newsApi.get('/news/tamilmirror', tags=['News'])
async def tamil_mirror():
    return news.tamil_mirror()


@newsApi.get('/news/newswire', tags=['News'])
async def newswire():
    return news.newswire()


@newsApi.get('/news/newsfirst/ta', tags=['News'])
async def newsfirsttamil():
    return news.newsfirsttamil()


@newsApi.get('/news/newsfirst/en', tags=['News'])
async def newsfirstenglish():
    return news.newsfirstenglish()


@newsApi.get('/news/newsfirst/sin', tags=['News'])
async def newsfirstsinhala():
    return news.newsfirstsinhala()


@newsApi.get('/news/adaderana/en', tags=['News'])
async def adaderana():
    return news.adaderanaenglish()


@newsApi.get('/news/hiru', tags=['News'])
async def hiru():
    return news.hiru()


@newsApi.get('/news/search/{keyword}', tags=['News'])
async def search(keyword: str):
    newsItems = []
    for n in news.newswire():
        newsItems.append(n)
    for n in news.daily_mirror():
        newsItems.append(n)
    for n in news.tamil_mirror():
        newsItems.append(n)
    for n in news.newsfirsttamil():
        newsItems.append(n)
    for n in news.newsfirstsinhala():
        newsItems.append(n)
    for n in news.newsfirstenglish():
        newsItems.append(n)
    for n in news.adaderanaenglish():
        newsItems.append(n)
    for n in news.hiru():
        newsItems.append(n)

    i = 0
    result = []
    for n in newsItems:
        if keyword.lower() in n['title'].lower():
            result.append(n)
            i += 1
        else:
            if keyword.lower() in n['description'].lower():
                result.append(n)
                i += 1

    output = {'count': i, "result": result}

    return output
