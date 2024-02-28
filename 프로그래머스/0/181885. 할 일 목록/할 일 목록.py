def solution(todo_list, finished):
    a = dict(zip(todo_list, finished))
    return [key for key, value in a.items() if not value]
    