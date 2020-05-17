import json
from pprint import pprint

a = {
    "1.FirstName": "Gildong",
    "2.LastName": "Hong",
    "3.Age": 20,
    "4.University": "Yonsei University",
    "5.Courses": [
        {
            "Major": "Statistics",
            "Classes": ["Probability",
                        "Generalized Linear Model",
                        "Categorical Data Analysis"]
        },
        {
            "Minor": "ComputerScience",
            "Classes": ["Data Structure",
                        "Programming",
                        "Algorithms"]
        }
    ]
}

if __name__ == '__main__':
    b = json.dumps(a, indent=4)
    print(b)
    print(type(b))
    # c = json.loads(b)
    # print(type(c))
    # print(c)

    # with open('json_file.json', 'w') as f:
    #     json.dump(a, fp=f, indent=4)

    # with open('json_file.json', 'r') as f:
    #     d = json.load(f)
    # print(type(d))
    # pprint(d)

    # with open('ex.txt', 'w') as f:
    #     for i in range(10):
    #         f.write(str(i) + '\n')
    #
    # with open('ex.txt', 'r') as f:
    #     e = f.readline()
    # print(e)
"""
open 모드
r: 읽기 모드. 파일이 없으면 Error.
r+: 읽기, 덮어쓰기 모드. 파일이 없으면 Error.
w: 쓰기 모드. 파일이 없으면 새로 만든다.
w+: 읽기, 지우고 새로 쓰기 모드. 파일이 없으면 새로 만든다.
a: 기존의 내용에 덧붙여 추가 쓰기 모드. 파일이 없으면 새로 만든다.
"""