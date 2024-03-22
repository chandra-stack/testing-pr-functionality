import urllib3

from urllib3 import *
dict = {
    "DEV":
        {
            1: "https://www.kent.dev.eschein.com/",
            2: "https://www.gb.dev.eschein.com/",
            3: "https://www.ie.dev.eschein.com/"
        },
    "QA":
        {
            1: "https://www.kent.qa.eschein.com/",
            2: "https://www.gb.qa.eschein.com/",
            3: "https://www.ie.qa.eschein.com/"
        },
    "TEST_URL":
        {
            1: "https://kenttest1.azurewebsites.net/",
            2: "https://kentangpoc2.azurewebsites.net/",
            3: "https://kenttest02.azurewebsites.net/",
            4: "https://kenttestang.azurewebsites.net/",
            5: "https://ietestang.azurewebsites.net/",
            6: "https://gbtestang.azurewebsites.net/",
            7: "https://hstestdev.azurewebsites.net/",
            8: "https://kentangpoc1.azurewebsites.net/",
            9: "https://kenttestdev.azurewebsites.net/"

        },
    "UAT":
        {
            1: "https://www.kent.stg.eschein.com/",
            2: "https://www.gb.stg.eschein.com/",
            3: "https://www.ie.stg.eschein.com/"
        },
    "PRE-PROD":
        {
            1: "https://www1.kentexpress.co.uk/",
            2: "https://www1.henryschein.co.uk/",
            3: "https://www1.henryschein.ie/"
        }

}


def monitor():
    l1 = list(dict.keys())
    for j in dict.keys():
        print(j,":\t")
        for i in dict[j]:
            print("\tURL:",dict[j][i], end=" ")
            print("Status Code:",request(method="GET", url=dict[j][i]).status)
            validate_statuscode(request(method="GET", url=dict[j][i]).status)
        print(end="\n")


def validate_statuscode(statuscode):
    if 200 <= statuscode <= 300:
        pass
    else:
        print("Oops!..status code didn't match")


if "__main__" == __name__:
    try:
        print('==============================================================')
        monitor()
    except Exception as e:
        print("Oops!..Something went wrong with the URL Execution")
        print(e)
    finally:
        print('==============================================================')
