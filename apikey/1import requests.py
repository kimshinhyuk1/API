import requests
import xmltodict
import json

# API URL 및 인증키
API_URL = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService"
API_KEY = "RBbve9EfbW8+3yQSgOR1jlvYFu2E0rgvicokQtnTiiXN2zBaxqj6JkxiPrurWYIQ1qv+KL/t2lSGJUQK/qFG6Q=="

# 요청 파라미터
params = {
    "serviceKey": API_KEY,  # 인증키
    "solYear": "2024",     # 요청 연도
    "solMonth": "11"       # 요청 월 (11월)
}

# API 호출
response = requests.get(API_URL, params=params)

# 응답 처리
if response.status_code == 200:
    print("API 호출 성공!")
    # XML 데이터를 Python 딕셔너리로 변환
    data_dict = xmltodict.parse(response.text)
    
    # 딕셔너리를 JSON 형식으로 변환 (가독성 향상)
    data_json = json.dumps(data_dict, ensure_ascii=False, indent=4)
    
    # 결과 출력
    print("응답 데이터:")
    print(data_json)
    
    # JSON 파일로 저장
    with open("api_response.json", "w", encoding="utf-8") as f:
        f.write(data_json)
        print("응답 데이터를 'api_response.json' 파일에 저장했습니다.")
else:
    print(f"API 호출 실패: {response.status_code}, {response.text}")
