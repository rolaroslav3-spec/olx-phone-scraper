import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "uk-UA,uk;q=0.9,en;q=0.8"
}

def parse_olx_phones():
    url = "https://www.olx.ua/uk/list/q-телефон/?search%5Bfilter_float_price:from%5D=1000"

    # Создаем скрейпер, который умеет проходить защиту Cloudflare
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url, headers=HEADERS)
    print("Заходим на OLX...")

    if response.status_code != 200:
        print(f"Ошибка доступа к сайту: статус {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.find_all("div", attrs={"data-cy": "l-card"})
    print(f"Найдено карточек на странице: {len(cards)}")

    items_data = []

    for card in cards:
        title_el = card.find("h4")
        title = title_el.text.strip() if title_el else "Без названия"

        link_el = card.find("a", attrs={"data-testid": "card-title-link"})
        link = link_el["href"] if link_el else ""
        if link and link.startswith("/"):
            link = "https://www.olx.ua" + link  # Добавили букву 'a'

        price_el = card.find("p", attrs={"data-testid": "ad-price"})
        price = price_el.text.strip() if price_el else "Цена не указана"

        items_data.append({
            "Название": title,  # С большой буквы
            "Ссылка": link,
            "Цена": price
        })

    return items_data


def save_to_excel(data, filename="olx_phones.xlsx"):
    if not data:
        print("Данные отсутствуют")
        return

    df = pd.DataFrame(data)
    df = df[["Цена", "Название", "Ссылка"]]  # Без лишних пробелов
    df.to_excel(filename, index=False)
    print(f"Готово! Данные успешно сохранены в файл: {filename}")


if __name__ == "__main__":
    phones_data = parse_olx_phones()
    save_to_excel(phones_data)