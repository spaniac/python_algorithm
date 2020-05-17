import pickle


"""
pickle은 python objects를 text 형식의 파일로 저장 및 불러오기를 지원하는 모듈.
"""
li = ['a', 'b', 'c']
with open('list.txt', 'wb') as f:
    pickle.dump(li, f)

with open('list.txt', 'rb') as f:
    data = pickle.load(f)

print(data)
print(type(data))