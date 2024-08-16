# 주요 기능 : LLM 관련 작업 처리
# 설명 : OpenAI API를 사용하여 응답 생성, 텍스트를 SQL로 변환, 결과 포맷팅 등 LLM 관련 모든 작업을 수행함
# user의 질문: User query
# 기능 1번 : User query 핸들링(어떠한 질문을 할 것인지 정확하게 기준을 정해야함)
#openai api < solar llm
# 데이터 토대로 질문 리스트-> sql 바뀌는 성능을 검증

# query_to_sql-> openai api 돈을내야해..


# 기능 4번 : 이를 database_handler.py에 전달
# 기능 5번 : 결과 포맷팅: database_handler.py에서 받은 해당 데이터 베이스를 출력(형식에 갖추어)


#RDB에 해당 user sql문을 조회하는 파일
import rag_retriever
# Query to SQL library
import config
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


# Response를 얻기 위한 library
from langchain_upstage import ChatUpstage
from langchain_core.messages import HumanMessage, SystemMessage

def query_to_sql(api_key,user_query):
    llm = ChatUpstage(api_key=api_key)
    template = """
You only have to use fixed columns' name: [flight_number,airline,flight_date, STD,Departure,Arrival]
You will use the following rules to convert the input to SQL:
Variable for flight Number: Use flight_number as the fixed variable for the flight number.
Variable for firline: Use airline as the fixed variable for the airline.
Variable for flight Date: Ensure that flight date is enclosed in quotation marks when used.
Variable for STD: Use STD as the fixed variable for the departing time or arrival time.
Airport Variables: Use Departure for the departing airport and Arrival for the arriving airport. 
And make sure Aiport's name is in Korean
If query includes '오늘', make sure flight date is today's date. The format is 'YYYY-MM-DD"
Make sure table name is flights
SELECT clause, FROM clause and WHERE clause should be in each line
When writing SQL queries, ensure that WHERE clauses and AND conditions are written on a single line without any line breaks.
Ensure that  SQL query that you make does not contain unintended text
Just make sure that only return SQL statements
You are a data scientist. Convert the following natural language query to "ONLY" SQL query
:
Query: {query}
SQL:
"""
    messages = [
    SystemMessage(content=template),
    HumanMessage(content=user_query)
    ]
    response = llm.invoke(messages)
    return response.content
def refine_sql(sql_query):
    # sql문을 rag_retriever로 보내는 역할
    # original_string = "여기는 작은따옴표(')가 포함된 문자열입니다."
    # 작은따옴표를 큰따옴표로 바꾸기
    changed_sql_query = sql_query.replace("'", '"')  
    changed_sql_query = changed_sql_query.replace("```sql", "")
    changed_sql_query = changed_sql_query.replace("```", "")
    return str(changed_sql_query)
def final_query(query,api_key):
    llm = ChatUpstage(api_key=api_key)
    messages = [
    SystemMessage(
        content=  """
            Based on Given data, Give me Information in Korean
            Just only answer flight_number with numbering when I ask "항공편"
            """
    ),
    HumanMessage(
        content= user_query
    )
    ]
    response = llm.invoke(messages)
    return response.content

if __name__== "__main__":
    user_query="8월 16일 이스타 항공에서 운행하는 항공편이 총 몇 편인지 알려줘"
    llm_api_key="up_CxnSYwc4TYOD487y9mbEKJdeVUjDy"
  
    # User query to User SQL query
    sql = query_to_sql(llm_api_key,user_query)
    print(refine_sql(sql))
    # # Get result 
    result = rag_retriever.execute_sql_query(refine_sql(sql))
    print(result)
    user_query += "Data:" + str(result)
    print(final_query(user_query,llm_api_key))

 
 
 


