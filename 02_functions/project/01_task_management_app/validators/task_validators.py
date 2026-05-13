# Formating title
def validate_title(title):
    title = title.lower()
    return title != "" in title


# Validate Status
def validate_status(status):
    status = status.lower()
    return status == "pending" or "completed" in status


# Validate Category
def validate_category(category):
    category = category.lower()
    return category in ["work", "personal", "other"]


# Validate Due Date
def validate_due_date(due_date):
    part = due_date.split("-")

    # Check 3 Parts (Year,Month,Day)
    if len(part) != 3:
        return False
    year = part[0]
    month = part[1]
    day = part[2]

    # Check Formatting (Year,Month,Day)
    if (
        len(year) == 4
        and year.isdigit()
        and len(month) == 2
        and month.isdigit()
        and len(day) == 2
        and day.isdigit()
    ):
        return True
    else:
        return False


# Validate Description
def validate_description(description):
    return len(description) <= 100
