import json

try:
    with open("output.json", "r", encoding="utf-8") as f:
        # 파일 내용을 문자열로 읽기
        content = f.read()
        print("파일 내용 확인:")
        print(content)  # JSON 파일 내용을 출력

        # JSON 데이터를 딕셔너리로 변환
        data_dict = json.loads(content)
        print("JSON 데이터 로드 성공!")
        print(data_dict)
except json.JSONDecodeError as e:
    print(f"JSONDecodeError: {e}")
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
except Exception as e:
    print(f"오류 발생: {e}")
