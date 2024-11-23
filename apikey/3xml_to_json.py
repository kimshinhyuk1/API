import xmltodict
import json

# XML 데이터 예제
xml_data = """
<response>
    <header>
        <resultCode>00</resultCode>
        <resultMsg>NORMAL SERVICE.</resultMsg>
    </header>
    <body>
        <items>
            <item>
                <dateName>설날</dateName>
                <locdate>20240101</locdate>
                <isHoliday>Y</isHoliday>
            </item>
        </items>
    </body>
</response>
"""

print("Step 1: XML 데이터를 Python 딕셔너리로 변환 중...")
try:
    data_dict = xmltodict.parse(xml_data)
    print("Step 2: 변환 성공!")
except Exception as e:
    print(f"Step 2 Error: {e}")
    exit()

print("Step 3: 딕셔너리를 JSON으로 변환 중...")
try:
    data_json = json.dumps(data_dict, ensure_ascii=False, indent=4)
    print("Step 4: 변환 성공!")
except Exception as e:
    print(f"Step 4 Error: {e}")
    exit()

print("Step 5: JSON 파일로 저장 중...")
try:
    with open("output.json", "w", encoding="utf-8") as f:
        f.write(data_json)
        print("Step 6: 파일 저장 성공!")
except Exception as e:
    print(f"Step 6 Error: {e}")
    exit()

print("변환된 JSON 데이터:")
print(data_json)
