def classify_issue(title: str, description: str) -> str:
    """
    Simple triage helper.
    """

    text = f"{title} {description}".lower()

    if any(word in text for word in [
        "outage",
        "production down",
        "data loss",
        "security breach",
    ]):
        return "Critical"

    if any(word in text for word in [
        "500",
        "authentication",
        "database",
        "timeout",
    ]):
        return "High"

    if any(word in text for word in [
        "slow",
        "performance",
        "ui bug",
    ]):
        return "Medium"

    return "Low"