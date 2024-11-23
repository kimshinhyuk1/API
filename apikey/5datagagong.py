# 기존 데이터
data_dict = {
    "response": {
        "header": {
            "resultCode": "00",
            "resultMsg": "NORMAL SERVICE."
        },
        "body": {
            "items": {
                "item": {
                    "dateName": "설날",
                    "locdate": "20240101",
                    "isHoliday": "Y"
                }
            }
        }
    }
}

# 가공된 데이터
processed_data = {
    "공휴일 이름": data_dict["response"]["body"]["items"]["item"]["dateName"],
    "날짜": data_dict["response"]["body"]["items"]["item"]["locdate"],
    "공휴일 여부": data_dict["response"]["body"]["items"]["item"]["isHoliday"]
}
processed_data["연도"] = processed_data["날짜"][:4]  # 날짜에서 연도 추출

print(processed_data)
