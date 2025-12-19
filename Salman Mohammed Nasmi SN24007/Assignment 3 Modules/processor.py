#Salman Mohammed Nasmi
#SN24007

from rich.table import Table
from rich.console import Console

terminal = Console()  # Rich console instance for styled output

def build_tasks_table(task_list):
    """Create a styled Rich table showing all tasks."""
    tbl = Table(title="Task Overview")
    tbl.add_column("ID", style="bright_cyan")
    tbl.add_column("Priority", style="magenta")
    tbl.add_column("Description", style="white")
    tbl.add_column("State", style="bright_green")

    for task in task_list:
        # Shorten long descriptions so they fit nicely
        description = task["task"]
        if len(description) > 40:
            description = description[:40] + "..."

        tbl.add_row(
            str(task["id"]),
            str(task["priority"]),
            description,
            task["status"],
        )

    return tbl

def get_open_tasks(task_list):
    """Return a list of tasks that are not completed yet."""
    return [task for task in task_list if task["status"] == "Pending"]

def summarize_tasks(task_list):
    """Return total number of tasks and how many are still pending."""
    total_tasks = len(task_list)
    pending_tasks = len(get_open_tasks(task_list))
    return total_tasks, pending_tasks
