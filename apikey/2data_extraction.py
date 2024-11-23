# 필요한 데이터만 추출
header = data_dict["response"]["header"]
body_items = data_dict["response"]["body"]["items"]["item"]

# 헤더 출력
print(f"결과 코드: {header['resultCode']}, 결과 메시지: {header['resultMsg']}")

# 본문 데이터 출력
print("본문 데이터:")
print(f"날짜명: {body_items['dateName']}, 날짜: {body_items['locdate']}, 공휴일 여부: {body_items['isHoliday']}")
