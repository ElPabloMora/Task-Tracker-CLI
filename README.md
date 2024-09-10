It is a command line interface where we can add, update and delete tasks. We can also mark a completion status for said task. This solution is based on the page [roadmap.sh](https://roadmap.sh/projects/task-tracker)

# How to use :
```python
#To add a new task
py task-tracker.py add "task"

#To delete task based on id
py task-tracker.py delete 2

#To update task based on id
py task-tracker.py update 2
m
#To mark task done/progress
py task-tracker.py mark-done 4
py task-tracker.py mark_ii_progress 4

#To show tasks
py task-tracker.py list all
py task-tracker.py list done
py task-tracker.py list in-progress
```
> [!IMPORTANT]
> Make sure you write the commands correctly so that they do not give errors
