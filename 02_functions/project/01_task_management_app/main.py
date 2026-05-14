from managers.user_manager import register_user, get_users, get_user_by_username, users

from managers.task_managers import (
    create_task,
    get_all_task,
    get_task_by_user,
    get_task_by_category,
    get_task_by_status,
    delete_task,
    mark_task_complate,
    tasks,
)


def main():
    """Main Aplication entry point"""
    # Register users
    print("1. Register Account")
    print(register_user("Andrew", "Andrew@gmail.com", "adrw1234567", users))
    print(register_user("Bob", "Bob@gmail.com", "123456BOB", users))
    print(register_user("Charley", "Charley@gmail.com", "98765Charley", users))
    print(register_user("Dory", "Dory@gmail.com", "9876543dory", users))

    print("\n" + "=" * 50 + "\n")

    # Get user by username
    print("2. Get User by Username:\n")
    print(get_user_by_username("andrew", users))
    print(get_user_by_username("BOB", users))
    print(get_user_by_username("Kevin", users))  # Not registered

    print("\n" + "=" * 50 + "\n")

    # Get All users
    print("3. Get All Users who Registered: \n")
    print(get_users(users))
    print("\n" + "=" * 50 + "\n")

    # Task Creation
    print("Create Task: \n")
    print(
        create_task(
            "Daily",
            "The task is a my daily rutine to start my activity",
            "2026-05-13",
            "pending",
            "personal",
            "andrew",
            users,
            tasks,
        )
    )
    print(
        create_task(
            "Rutine",
            "The task is a my daily rutine to start my activity",
            "2026-05-13",
            "pending",
            "work",
            "bob",
            users,
            tasks,
        )
    )
    print(
        create_task(
            "Rutine",
            "The task is a my daily rutine to start my activity",
            "2026-05-13",
            "completed",
            "work",
            "charley",
            users,
            tasks,
        )
    )
    print(
        create_task(
            "Rutine",
            "The task is a my daily rutine to start my activity",
            "2026-05-13",
            "completed",
            "personal",
            "dory",
            users,
            tasks,
        )
    )
    print("\n" + "=" * 50 + "\n")
    # Get all task
    print(get_all_task(tasks))

    print("\n" + "=" * 50 + "\n")
    # Task by user
    print("Get task by user: \n")
    print(get_task_by_user("andrew", tasks))
    print(get_task_by_user("zara", tasks))  # User dont create task

    print("\n" + "=" * 50 + "\n")
    # Task by category
    print("Get task by category: \n")
    print(get_task_by_category("work", tasks))
    print(get_task_by_category("personal", tasks))
    print(get_task_by_category("sleep", tasks))  # Not valid category

    print("\n" + "=" * 50 + "\n")
    # Task by status
    print("Get task by status: \n")
    print(get_task_by_status("pending", tasks))
    print(get_task_by_status("Completed", tasks))

    print("\n" + "=" * 50 + "\n")
    # Delete Task
    print(delete_task(3, "charley", tasks))
    print(
        delete_task(2, "charley", tasks)
    )  # If doesn't the owner of task, so you can"t delete this task

    print("\n" + "=" * 50 + "\n")
    # Mark to completed
    print("Mark Completed to the Task:")
    print(mark_task_complate(1, tasks))
    print(
        mark_task_complate(4, tasks)
    )  # Cannot change status to 'Completed' in he Task, cuase the Task has been Completed


if __name__ == "__main__":
    main()
