from importlib import import_module


def run_action(action_num, database):
    actions_map = {
        1: "new-order",
        2: "order-info",
        3: "all-orders",
        4: "update-order",
        5: "delete-order",
        6: "delete-all-orders",
        7: "exit"
    }

    if action_num not in actions_map:
        raise ValueError("Action is not valid")

    if actions_map[action_num] == "exit":
        return True

    module = import_module(f"order_actions.{actions_map[action_num]}")

    module.run_module(database)
