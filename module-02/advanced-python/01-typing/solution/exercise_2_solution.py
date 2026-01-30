"""Exercise 2 Solution: Working with Collections

This solution demonstrates proper type hints for collections including
lists, dicts, sets, tuples, and nested structures.
"""


def uppercase_names(names: list[str]) -> list[str]:
    """Convert all names in a list to uppercase.

    Args:
        names: List of name strings

    Returns:
        List of uppercase names
    """
    return [name.upper() for name in names]


def get_user_scores() -> dict[str, list[int]]:
    """Get a dictionary of users and their test scores.

    Returns:
        Dictionary mapping usernames to lists of scores
    """
    return {
        "alice": [95, 87, 92],
        "bob": [88, 91],
        "charlie": [76, 85, 90, 88]
    }


def print_user_scores(scores_dict: dict[str, list[int]]) -> None:
    """Print each user and their scores.

    Args:
        scores_dict: Dictionary mapping usernames to score lists
    """
    for user, scores in scores_dict.items():
        print(f"User {user} has scores: {scores}")


def get_unique_tags() -> set[str]:
    """Get a set of unique tags.

    Returns:
        Set of unique tag strings
    """
    tags = ["python", "typing", "tutorial", "python", "advanced", "tutorial"]
    return set(tags)


def get_users() -> list[dict[str, str | int]]:
    """Get a list of user dictionaries.

    Returns:
        List of dictionaries, each containing user data
    """
    return [
        {"name": "Alice", "email": "alice@example.com", "age": 30},
        {"name": "Bob", "email": "bob@example.com", "age": 25},
        {"name": "Charlie", "email": "charlie@example.com", "age": 35}
    ]


def get_coordinate() -> tuple[float, float]:
    """Get a coordinate as a tuple.

    Returns:
        Tuple of (x, y) coordinates as floats
    """
    return (40.7128, -74.0060)


def extract_names(users: list[dict[str, str | int]]) -> list[str]:
    """Extract just the names from a list of user dictionaries.

    Args:
        users: List of user dictionaries

    Returns:
        List of name strings
    """
    return [str(user["name"]) for user in users]


def main() -> None:
    """Run exercise demonstrations."""
    # Test uppercase names
    names: list[str] = ["alice", "bob", "charlie"]
    uppercase: list[str] = uppercase_names(names)
    for name in uppercase:
        print(name)

    # Test user scores
    scores: dict[str, list[int]] = get_user_scores()
    print_user_scores(scores)

    # Test unique tags
    tags: set[str] = get_unique_tags()
    print(f"Unique tags: {', '.join(sorted(tags))}")

    # Test nested structures
    users: list[dict[str, str | int]] = get_users()
    user_names: list[str] = extract_names(users)
    print(f"User names: {user_names}")

    # Test tuples
    lat: float
    lon: float
    lat, lon = get_coordinate()
    print(f"Coordinates: ({lat}, {lon})")


if __name__ == "__main__":
    main()
