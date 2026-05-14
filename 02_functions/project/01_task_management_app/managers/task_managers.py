from validators import (
    validate_title,
    validate_status,
    validate_category,
    validate_due_date,
    validate_description,
)
from validators import validate_owner_exists
from managers.clear_task_display import clean_display_task, display_multiple_task

tasks = []  # Global Task List Variabels


# Create Task
def create_task(
    title, description, due_date, status, category, owner, users_list, task_list
):
    valid_username = validate_owner_exists(owner, users_list)
    task_id = len(task_list) + 1
    valid_title = validate_title(title)
    valid_description = validate_description(description)
    valid_due_date = validate_due_date(due_date)

    clean_status = status.lower().strip()
    valid_status = validate_status(clean_status)

    clean_category = category.lower().strip()
    valid_category = validate_category(clean_category)

    if (
        valid_username
        and valid_title
        and valid_description
        and valid_due_date
        and valid_status
        and valid_category
    ):
        new_task = {
            "task_id": task_id,
            "title": title,
            "description": description,
            "due_date": due_date,
            "status": clean_status,
            "category": clean_category,
            "owner": owner,
        }
        # Add New Task in LIst
        task_list.append(new_task)
        create_task_mssg = {
            "name": f"Task by {owner}",
            "mssg": "Task created successfuly!",
        }
        # Return True & Successed Mssg
        return f"Status: {True}", create_task_mssg
    else:
        eror_validators = {
            "valid_title": (
                not valid_title,
                "This section can't be empty in the Title",
            ),
            "valid_description": (
                not valid_description,
                "Descrption Must be <= 100 Character!",
            ),
            "valid_due_date": (
                not valid_due_date,
                "Please enter Due Date in this format: YYYY-MM-DD",
            ),
            "valid_status": (
                not valid_status,
                "Must be Enter Status by: 'Pending' And 'Completed'",
            ),
            "valid_category": (
                not valid_category,
                "Must be Enter this Category  : 'work', 'personal '', 'other'",
            ),
            "valid_owner": (not valid_username, "Username isn't Registered!"),
        }
        for _, (is_error, error_msg) in eror_validators.items():
            if is_error:
                return False, error_msg


# Get All Task
def get_all_task(task_list):
    print("Get All Task: ")
    display_multiple_task(task_list)


# Get Task by Owner
def get_task_by_user(owner, task_list):
    print(f"\n Get Task by Owner: {owner}")
    clean_owner = owner.lower().strip()
    result = []
    for tsk in task_list:
        if tsk["owner"] == clean_owner:
            result.append(tsk)
    if result:
        display_multiple_task(result)
    else:
        print(f"Not tasks found for owner {clean_owner}")


# Get Task by category
def get_task_by_category(category, task_list):
    print(f"\n Get Task by Category: {category}")
    clean_category = category.lower().strip()
    result = []
    for tsk in task_list:
        if tsk["category"] == clean_category:
            result.append(tsk)
    if result:
        display_multiple_task(result)
    else:
        print(f"Not tasks found for Category {clean_category}")


# Get Task by staatus
def get_task_by_status(status, task_list):
    print(f"\n Get Task by Status: {status}")
    clean_status = status.lower().strip()
    result = []
    for tsk in task_list:
        if tsk["status"] == clean_status:
            result.append(tsk)
    if result:
        display_multiple_task(result)
    else:
        print(f"Not tasks found for Status {clean_status}")


# Delete Task
def delete_task(task_id, owner, task_list):
    result = []
    for tsk in task_list:
        if tsk["task_id"] == task_id:
            result.append(tsk)
            if tsk["owner"] == owner and result:
                print("Delete this task:")
                display_multiple_task(result)
                task_list.remove(tsk)
                return True, f"Task {task_id} succesfuly removed"
            else:
                return False, f"Owner: {owner} can't be deleted this task"
    return False, "Task not found"


# Mark task to completed
def mark_task_complate(task_id, task_list):
    result = []
    for tsk in task_list:
        if tsk["task_id"] == task_id:
            result.append(tsk)
            if tsk["status"] == "completed":
                display_multiple_task(result)
                return False, f"Task has been Complated"
            else:
                tsk["status"] = "completed"
                display_multiple_task(result)
                return True, f"Task {task_id} successfuly updated to 'Completed'"
    return False, "Task not found"
