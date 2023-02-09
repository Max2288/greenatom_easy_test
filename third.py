import requests
from bs4 import BeautifulSoup


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
}


def find_tags(url: str):
    req = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(req.text, "lxml")
    pars_result = {"all": 0, "with_attrs": 0}
    # ВАЖНО ЗАМЕТИТЬ ЧТО ЕСТЬ ПУСТЫЕ АТРИБУТЫ НАПРИМЕР: {'href': ''}, данный атрибут пустой, его данный парсинг не учитывает!
    for sub_heading in soup.find_all():
        if sub_heading.attrs.values():
            pars_result["with_attrs"] += 1
        pars_result["all"] += 1
    return pars_result


print(find_tags('https://greenatom.ru'))
