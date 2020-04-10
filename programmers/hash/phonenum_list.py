def solution(phone_book):
    phone_book = sorted(phone_book)
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

# def solution(phone_book):
#     for p in phone_book:
#         for k in phone_book:
#             if p != k and p.startswith(k):
#                 return False
#     answer = True
#     return answer
