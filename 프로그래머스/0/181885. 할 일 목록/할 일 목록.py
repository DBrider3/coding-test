def solution(todo_list, finished):
    return [key for key, value in dict(zip(todo_list, finished)).items() if not value]
    