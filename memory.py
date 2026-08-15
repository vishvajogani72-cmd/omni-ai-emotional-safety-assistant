import json
import os

MEMORY_FILE = os.path.join(
    os.path.dirname(__file__),
    "memory.json"
)



def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return {}

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
         return {}


def save_memory(data):

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


def remember(key, value):

    data = load_memory()
    data[key] = value

    save_memory(data)

    return f"I'll remember that, Owner."


def recall(key):

    data = load_memory()

    # ----------------------------------
    # Normal memory
    # ----------------------------------

    if key in data:

        return data[key]

    # ----------------------------------
    # Favorite memory
    # ----------------------------------

    favorites = data.get(
        "favorites",
        {}
    )
    favorite_key = key.replace(
        "favorite_",
        "",
        1
    )

    # Case-insensitive search
    for name, item in favorites.items():

        if name.lower() == favorite_key.lower():

            return item

    return None
