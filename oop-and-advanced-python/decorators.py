# ==========================================
# Decorator Example
# ==========================================

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"\nExecuting '{func.__name__}'...")
        result = func(*args, **kwargs)
        print(f"Finished '{func.__name__}'.")
        return result

    return wrapper