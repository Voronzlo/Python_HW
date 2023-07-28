def create_dict(**kwargs):
    return {str(key): value for key, value in kwargs.items()}

# Пример использования
result = create_dict(name='John', age=25, city='New York')
print(result)