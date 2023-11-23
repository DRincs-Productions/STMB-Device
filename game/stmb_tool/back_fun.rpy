default smartphone_back_list = []

init python:
    def go_to_back(list_backs: list[str]) -> None:
        if len(list_backs) > 0:
            list_backs.pop()

    def add_back(list_backs: list[str], value: str) -> None:
        list_backs.append(value)

    def go_to_home(list_backs: list[str]) -> None:
        list_backs.clear()

    def last_back(list_backs: list[str]) -> str:
        if len(list_backs) > 0:
            return list_backs[-1]
        else:
            return "main_menu"

    def is_back_list_empty(list_backs: list[str]) -> bool:
        return len(list_backs) > 0
