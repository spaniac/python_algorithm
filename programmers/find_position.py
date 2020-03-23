def solution(v):
    x_list = tuple(map(lambda x: x[0], v))
    y_list = tuple(map(lambda y: y[1], v))

    x = max(x_list) if x_list.count(max(x_list)) < x_list.count(min(x_list)) else x_list.count(min(x_list))
    y = max(y_list) if y_list.count(max(y_list)) < y_list.count(min(y_list)) else y_list.count(min(y_list))

    answer = [x, y]

    print('Hello Python')

    return answer
