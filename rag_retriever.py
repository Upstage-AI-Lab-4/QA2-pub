import sqlite3
import pandas as pd

def execute_sql_query(query):
    #make_sample_database()
    # CSV 파일을 읽어오기
    side_query = 'SELECT CAST(STD AS INTEGER) AS converted_STD \n FROM flights;'
    csv_file = 'flights.csv'  # CSV 파일 경로
    df = pd.read_csv(csv_file)

    # SQLite3 데이터베이스 파일에 연결
    conn = sqlite3.connect('flights.db')  # SQLite 데이터베이스 파일 경로

    # DataFrame을 SQLite3 데이터베이스로 저장
    df.to_sql('flights', conn, if_exists='replace', index=False) 
    try:
        # SQLite 데이터베이스 연결 설정
        
        cursor = conn.cursor()
        # 쿼리 실행
        #cursor.execute(side_query)
        cursor.execute(query)
        # 쿼리 실행 후 데이터가 있을 경우 fetchall()
        #if cursor.description:
        result = cursor.fetchall()
        return result
       # else:
            #connection.commit()  # 데이터베이스에 변화를 주는 쿼리의 경우
            #return "Query executed successfully"

    except sqlite3.Error as e:
        return f"Error: {e}"

    finally:
        if conn:
            cursor.close()
            conn.close()


