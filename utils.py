import requests


def search_item_position(item_id, keyword):
    page = 0
    while True:
        page += 1
        url = f"https://search.wb.ru/exactmatch/ru/common/v4/search?appType=1&curr=rub&dest=12358283&page={page}&query={keyword}&regions=80,115,38,4,64,83,33,68,70,69,30,86,40,1,66,110,22,31,48,114&resultset=catalog&sort=popular&spp=22&suppressSpellcheck=false"
        try:
            response = requests.get(url)
            item_list = response.json()['data']['products']
            if not item_list:
                return
            item_index = 0
            for item in item_list:
                item_index += 1
                position = page * 100 + item_index
                if item['id'] == int(item_id):
                    result = [page, item_index]
                    return result
        except:
            break