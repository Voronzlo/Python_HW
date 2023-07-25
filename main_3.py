things = {'палатка': 500, 'спальный мешок': 100, 'консервы': 10, 'нож': 15,
          'термос': 50, 'аптечка': 50, 'бутылка': 30, 'бинокль': 50, 'спички': 10,
          'ружье': 500, 'уголь': 100, 'ракетка': 100, 'одежда': 300, 'топор': 200}

LIMIT = 1500

def backpack_capacity(capacity: int, things: dict) -> list[str]:
    packaging_option = []
    summary = []
    for key, value in things.items():
        if value <= capacity:
            capacity -= value
            packaging_option.append(key)
    return packaging_option
print(backpack_capacity(LIMIT, things))