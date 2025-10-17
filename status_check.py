

def check_battery(level):
    if level < 20:
        return "⚠️ Battery Critical: Land immediately!"
    elif level < 50:
        return f"🔋 Battery at {level}%. Return to base soon."
    else:
        return f"✅ Battery healthy at {level}%."

print(check_battery(75))

