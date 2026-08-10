from collector.data_reader.domestic_stock_data_reader import domestic_stock_data_reader
from collector.data_reader.index_data_reader import index_data_reader
from collector.data_reader.price_data_reader import price_data_reader
from collector.data_reader.standard_interest_data_reader import standard_interest_data_reader
from collector.data_reader.double_price_data_reader import double_price_data_reader

from collector.chart_maker.domestic_stock_chart_maker import domestic_stock_chart_maker
from collector.chart_maker.domestic_stock_day_candle_chart_maker import domestic_stock_day_candle_chart_maker
from collector.chart_maker.index_chart_maker import index_chart_maker
from collector.chart_maker.index_day_candle_chart_maker import index_day_candle_chart_maker
from collector.chart_maker.price_chart_maker import price_chart_maker
from collector.chart_maker.standard_interest_chart_maker import standard_interest_chart_maker
from collector.chart_maker.double_price_data_chart_maker import double_price_data_chart_maker

from notion.get_all_pages import get_all_pages
from notion.config import NOTION_INFO_DB_ID

for day in [90, 365, 365*5]:
    for page in get_all_pages(NOTION_INFO_DB_ID):
    
        ticker_data = page["properties"]["티커"]["rich_text"]
    
        if not ticker_data:
            continue
    
        ticker = ticker_data[0]["plain_text"]
    
        name_data = page["properties"]["종목"]["title"]
        name = name_data[0]["text"]["content"]

        price_name = {
            "KRX 금현물": "KRX_Gold"
        }
        
        if name in ["KRX 금현물"]:
            name = price_name[name]
            price_chart_maker(price_data_reader(day, name))              

        else:
            domestic_stock_chart_maker(domestic_stock_data_reader(day, ticker), name)
            domestic_stock_day_candle_chart_maker(domestic_stock_data_reader(day, ticker), name)          

price_chart_maker(price_data_reader(365*5, "USD-KRW"))

index_chart_maker(index_data_reader(365*5, "KOSPI"))
index_day_candle_chart_maker(index_data_reader(365*5, "KOSPI"))

double_price_data_chart_maker(double_price_data_reader(365*5, "International_Gold", "Dolar_Index"))
