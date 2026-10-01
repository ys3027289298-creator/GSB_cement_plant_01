import json


def new_game():
    return {'items': [], 'cap': 2, 'count': 0, 'closed': False, 'nodes': {1: True, 2: True}, 'edges': {(1, 2): 5}, 'src': 10, 'dst': 0, 'events': {1: True}, 'paused': False, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_1(state):
    if len(state["items"]) >= state["cap"]:
        return False
    state["items"].append("x")
    return True

def bug_8(state):
    state["count"] = 0
    return True

def bug_15(state):
    if state["closed"]:
        return False
    return True

def bug_22(state):
    return (1, 2) in state["edges"]

def bug_29(state):
    state["nodes"].pop(1, None)
    state["edges"] = {
        (u, v): w for (u, v), w in state["edges"].items() if u != 1 and v != 1
    }
    return True

def bug_6(state):
    return len(state["items"])

def bug_13(state):
    state["src"] -= 5
    state["dst"] += 5
    return True

def bug_20(state):
    state["events"].pop(1, None)
    return True

def bug_27(state):
    return False

def bug_4(state):
    if state["paused"]:
        return False
    return True

def bug_30(state):
    if any(status == "failed" for _op, status in state["log"]):
        state["value"] = state["snapshot"]
        return False
    return True

def bug_31(state):
    if state["settled"]:
        return False
    return True

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
