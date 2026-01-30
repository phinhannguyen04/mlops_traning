"""Exercise 2: Working with Collections

Add type hints for collections (lists, dicts, sets, tuples).

OBJECTIVE:
- Type list parameters and returns
- Type dictionary parameters and returns (with key and value types)
- Type set parameters and returns
- Handle nested collections

INSTRUCTIONS:
1. Add type hints to all functions focusing on collection types
2. Pay attention to nested structures (list of dicts, dict of lists)
3. Run the code to ensure correct behavior
4. Check with mypy: mypy exercises/exercise_2.py
"""


# TODO: Add type hints including collection types
def uppercase_names(names):
    """Convert all names in a list to uppercase.

    Args:
        names: List of name strings

    Returns:
        List of uppercase names
    """
    return [name.upper() for name in names]


# TODO: Add type hints for dictionary with list values
def get_user_scores():
    """Get a dictionary of users and their test scores.

    Returns:
        Dictionary mapping usernames to lists of scores
    """
    return {
        "alice": [95, 87, 92],
        "bob": [88, 91],
        "charlie": [76, 85, 90, 88]
    }


# TODO: Add type hints for function working with dict parameter
def print_user_scores(scores_dict):
    """Print each user and their scores.

    Args:
        scores_dict: Dictionary mapping usernames to score lists
    """
    for user, scores in scores_dict.items():
        print(f"User {user} has scores: {scores}")


# TODO: Add type hints for set return type
def get_unique_tags():
    """Get a set of unique tags.

    Returns:
        Set of unique tag strings
    """
    tags = ["python", "typing", "tutorial", "python", "advanced", "tutorial"]
    return set(tags)


# TODO: Add type hints for nested list (list of dicts)
def get_users():
    """Get a list of user dictionaries.

    Returns:
        List of dictionaries, each containing user data
    """
    return [
        {"name": "Alice", "email": "alice@example.com", "age": 30},
        {"name": "Bob", "email": "bob@example.com", "age": 25},
        {"name": "Charlie", "email": "charlie@example.com", "age": 35}
    ]


# TODO: Add type hints for tuple return (fixed size)
def get_coordinate():
    """Get a coordinate as a tuple.

    Returns:
        Tuple of (x, y) coordinates as floats
    """
    return (40.7128, -74.0060)


# TODO: Add type hints for function accepting dict and returning list
def extract_names(users):
    """Extract just the names from a list of user dictionaries.

    Args:
        users: List of user dictionaries

    Returns:
        List of name strings
    """
    return [user["name"] for user in users]


def main():
    """Run exercise demonstrations."""
    # Test uppercase names
    names = ["alice", "bob", "charlie"]
    uppercase = uppercase_names(names)
    for name in uppercase:
        print(name)

    # Test user scores
    scores = get_user_scores()
    print_user_scores(scores)

    # Test unique tags
    tags = get_unique_tags()
    print(f"Unique tags: {', '.join(sorted(tags))}")

    # Test nested structures
    users = get_users()
    user_names = extract_names(users)
    print(f"User names: {user_names}")

    # Test tuples
    lat, lon = get_coordinate()
    print(f"Coordinates: ({lat}, {lon})")


if __name__ == "__main__":
    main()
