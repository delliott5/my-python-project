

def check_battery(level):
    if level < 20:
        return "⚠️ Battery Critical: Land immediately!"
    elif level < 50:
        return "🔋 Battery low: Return to base soon."
    else:
        return "✅ Battery OK."

print(check_battery(45))
