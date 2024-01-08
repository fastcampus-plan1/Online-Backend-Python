import requests

def get_weather_data():
    url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList"
    params = {
        "serviceKey": "Bq0l9/ERQCCvnzlvO1w3HjM0r/0P+hQVG1hZGhq5T4XLiDLTY/KSazsy5oQRRhwXVwZ9YnpM8AvNR1iSUObYTQ==",
        "dataType": "JSON",
        "numOfRows": 10,
        "pageNo": 1,
        "dataCd": "ASOS",
        "dateCd": "DAY",
        "startDt": "20240101",
        "endDt": "20240106",
        "stnIds": "108"
    }

    response = requests.get(url, params=params)
    data = response.json()

    """
    {
        "response":{
            "header":{
                "resultCode":"00",
                "resultMsg":"NORMAL_SERVICE"
            },
            "body":{
                "dataType":"JSON",
                "items":{
                    "item":[
                    {
                        "stnId":"108",
                        "stnNm":"서울",
                        "tm":"2022-01-01",
                        "avgTa":"-4.3",
                        "minTa":"-10.2",
                        "minTaHrmt":"0710",
                        "maxTa":"2.3",
                        "maxTaHrmt":"1544",
                        "mi10MaxRn":"",
                        "mi10MaxRnHrmt":"",
                        "hr1MaxRn":"",
                        "hr1MaxRnHrmt":"",
                        "sumRnDur":"",
                        "sumRn":"",
                        "maxInsWs":"4.5",
                        "maxInsWsWd":"70",
                        "maxInsWsHrmt":"0923",
                        "maxWs":"2.8",
                        "maxWsWd":"20",
                        "maxWsHrmt":"0819",
                        "avgWs":"1.5",
                        "hr24SumRws":"1335",
                        "maxWd":"50",
                        "avgTd":"-14.4",
                        "minRhm":"31",
                        "minRhmHrmt":"1329",
                        "avgRhm":"46.3",
                        "avgPv":"2.1",
                        "avgPa":"1019.8",
                        "maxPs":"1034.0",
                        "maxPsHrmt":"0247",
                        "minPs":"1027.3",
                        "minPsHrmt":"2351",
                        "avgPs":"1030.9",
                        "ssDur":"9.6",
                        "sumSsHr":"9.0",
                        "hr1MaxIcsrHrmt":"1200",
                        "hr1MaxIcsr":"1.82",
                        "sumGsr":"10.39",
                        "ddMefs":"",
                        "ddMefsHrmt":"",
                        "ddMes":"",
                        "ddMesHrmt":"",
                        "sumDpthFhsc":"",
                        "avgTca":"1.4",
                        "avgLmac":"1.4",
                        "avgTs":"-3.7",
                        "minTg":"-15.4",
                        "avgCm5Te":"-0.9",
                        "avgCm10Te":"-1.0",
                        "avgCm20Te":"-0.3",
                        "avgCm30Te":"0.9",
                        "avgM05Te":"2.7",
                        "avgM10Te":"6.6",
                        "avgM15Te":"10.1",
                        "avgM30Te":"15.1",
                        "avgM50Te":"17.2",
                        "sumLrgEv":"1.3",
                        "sumSmlEv":"1.8",
                        "n99Rn":"0.3",
                        "iscs":"",
                        "sumFogDur":""
                    }
                    ]
                },
                "pageNo":1,
                "numOfRows":2,
                "totalCount":1
            }
        }
    }
    """

    
    if data["response"]["header"]["resultCode"] == "00":
        item_list = data["response"]["body"]["items"]["item"]
        dict_list = []
        for item in item_list:
            print(item)
            item_dict = {}
            item_dict["date"] = item["tm"]
            item_dict["min_temp"] = item["minTa"]
            item_dict["max_temp"] = item["maxTa"]
            item_dict["cloud_amount"] = item["avgTca"]
            item_dict["max_snow"] = item["ddMes"]
            item_dict["rain"] = item["sumRn"]
            dict_list.append(item_dict)

        return dict_list
    else:
        return None



