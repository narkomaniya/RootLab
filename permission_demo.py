import json
from pathlib import Path

FILE = Path("rootlab_permissions.json")


def load_permissions():
    if FILE.exists():
        try:
            return json.loads(FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("Файл разрешений повреждён, начинаю с пустого списка.")
    return {}


def save_permissions(permissions):
    FILE.write_text(
        json.dumps(permissions, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )


permissions = load_permissions()

while True:
    print("\nRootLab — тест логики разрешений")
    print("1 — разрешить приложению")
    print("2 — запретить приложению")
    print("3 — показать список")
    print("4 — отозвать разрешение")
    print("0 — выйти")

    choice = input("> ").strip()

    if choice in ("1", "2"):
        app = input("Введи имя приложения: ").strip()

        if not app:
            print("Имя не должно быть пустым.")
            continue

        permissions[app] = "разрешено" if choice == "1" else "запрещено"
        save_permissions(permissions)
        print(f"Для «{app}»: {permissions[app]}.")

    elif choice == "3":
        if not permissions:
            print("Список пока пуст.")
        else:
            for app, status in permissions.items():
                print(f"{app}: {status}")

    elif choice == "4":
        app = input("Имя приложения для удаления: ").strip()

        if permissions.pop(app, None) is not None:
            save_permissions(permissions)
            print("Запись удалена.")
        else:
            print("Такой записи нет.")

    elif choice == "0":
        break

    else:
        print("Выбери пункт 0, 1, 2, 3 или 4.")
