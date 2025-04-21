critical = 1.5

def player(name: str, dmg: int, hp: int):
    return {
        "name": name,
        "dmg": dmg,
        "hp": hp
    }

def item(name: str, ef: int, amount: int):
    return {
        "name": name,
        "ef": ef,
        "amount": amount,
        "use_item": lambda: item.update({"amount": item ["amount"] - 1}) if item["amount"] > 0 else None
    }
    return item

def critical_hit(attack):
    return attack * critical 