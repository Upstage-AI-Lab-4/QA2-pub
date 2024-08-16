import api_handler
import db_operations
from datetime import datetime, timedelta

def fetch_and_store_data():
    # 오늘 날짜 가져오기
    today = datetime.today().strftime('%Y%m%d')
    
    # 김포공항 출발 및 도착 데이터 가져오기
    kac_departure = api_handler.KAC_Departure_api(today)
    kac_arrival = api_handler.KAC_Arrival_api(today)
    
    # 인천공항 출발 및 도착 데이터 가져오기
    iiac_departure = api_handler.IIAC_Departure_api()
    iiac_arrival = api_handler.IIAC_Arrival_api()
    
    # 모든 데이터 합치기
    all_flights = kac_departure + kac_arrival + iiac_departure + iiac_arrival
    
    # 데이터베이스에 저장
    db_operations.insert_data_bulk(all_flights)
    
    print(f"Total flights fetched and stored: {len(all_flights)}")

if __name__ == "__main__":
    fetch_and_store_data()
