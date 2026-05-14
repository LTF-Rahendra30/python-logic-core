# Clean Display Task
def clean_display_task(task):
    print(f"""
    "Task ID": {task['task_id']}
    "Title": {task['title']}
    "Description": {task['description']}
    "Due Date": {task['due_date']}
    "Status": {task['status']}
    "Category": {task['category']}
    "Owner": {task['owner']} \n""")


def display_multiple_task(task_list):
    if not task_list:
        print("No task found")
        return
    for task in task_list:
        clean_display_task(task)
