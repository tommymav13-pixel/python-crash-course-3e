def make_sandwich(*items):
    """Prints a summary of a sandwich"""
    print("\nMaking a summary of a sandwich:")
    for item in items:
        print(f"- {item}")


make_sandwich('tuna')
make_sandwich('chicken', 'cheese', 'tomato')
make_sandwich('pastrami', 'mustard', 'pickles', 'cheese', 'onion')