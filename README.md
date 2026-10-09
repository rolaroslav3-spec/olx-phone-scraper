# OLX Phone Listings Scraper

Простой и эффективный парсер объявлений о продаже телефонов с сайта OLX.ua с автоматическим сохранением данных в Excel.

## Технологии

- Python 3
- CloudScraper (обход защиты Cloudflare)
- BeautifulSoup4 (парсинг HTML)
- Pandas / OpenPyXL (формирование `.xlsx` файлов)

## Что делает скрипт

1. Обходит базовую защиту сайта от ботов с помощью `cloudscraper`.
2. Извлекает названия объявлений, цены и прямые ссылки на карточки товаров.
3. Безопасно обрабатывает отсутствующие элементы без сбоев в работе.
4. Структурирует данные и сохраняет их в Excel-файл (`olx_phones.xlsx`).

## Быстрый запуск

1. Клонировать репозиторий:
   ```bash
   git clone [https://github.com/rolaroslav3-spec/olx-phone-scraper.git](https://github.com/rolaroslav3-spec/olx-phone-scraper.git)
