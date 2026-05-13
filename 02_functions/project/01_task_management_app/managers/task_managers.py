from validators import (
    validate_title,
    validate_status,
    validate_category,
    validate_due_date,
    validate_description,
)
from validators import validate_owner_exists

tasks = []  # Global Task List Variabels


def create_task(
    title, description, due_date, status, category, owner, users_list, task_list
):
    task_id = len(task_list) + 1
    valid_title = validate_title(title)
    valid_description = validate_description(description)
    valid_due_date = validate_due_date(due_date)
    valid_status = validate_status(status)
    valid_category = validate_category(category)
    valid_username = validate_owner_exists(owner, users_list)

    if (
        valid_title
        and valid_description
        and valid_due_date
        and valid_status
        and valid_category
        and valid_username
    ):
        new_task = {
            "task_id": task_id,
            "title": title,
            "description": description,
            "due_date": due_date,
            "status": status,
            "category": category,
            "owner": owner,
        }
        # Add New Task in LIst
        task_list.append(new_task)
        create_task_mssg = {
            "name": f"Task by {owner}",
            "mssg": "Task created successfuly!",
        }
        # Return True & Successed Mssg
        return True, create_task_mssg
    else:
        eror_validators = {
            "valid_title": (not valid_title, "This section can't be empty"),
            "valid_description": (not valid_description, "Must be <= 100 Character!"),
            "valid_due_date": (
                not valid_due_date,
                "Please enter in format: YYYY-MM-DD",
            ),
            "valid_status": (not valid_status, "Must be : 'Pending' And 'Completed'"),
            "valid_category": (
                not valid_category,
                "Must be : 'work', 'personal '', 'other'",
            ),
            "valid_owner": (not valid_username, "Username isn't Registered!"),
        }
        for _, (is_error, error_msg) in eror_validators.items():
            if is_error:
                return False, error_msg
