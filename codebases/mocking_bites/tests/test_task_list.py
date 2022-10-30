from lib.task_list import TaskList

def test_task_list_initially_empty():
  task_list = TaskList()
  assert task_list.all() == []

def test_tasks_initially_not_all_complete():
  task_list = TaskList()
  assert task_list.all_complete() == False

# Unit test `.all` and `.all_complete` behaviour
