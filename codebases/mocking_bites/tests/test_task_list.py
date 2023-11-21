from lib.task_list import TaskList
from unittest.mock import Mock


def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour

def test_all_complete_mock_1():
    task_list = TaskList()
    fake_task = Mock()
    fake_task.is_complete.return_value = True
    task_list.add(fake_task)
    assert task_list.all_complete() == True
    

def test_all_complete_mock_several_2():
    task_list = TaskList()
    task1 = Mock()
    task2 = Mock()
    task3 = Mock()
    task1.is_complete.return_value = False
    task2.is_complete.return_value = False
    task3.is_complete.return_value = False
    task_list.add(task1)
    task_list.add(task2)
    task_list.add(task3)
    assert task_list.all_complete() == False


def test_all_complete_mock_all_complete_3():
    task_list = TaskList()
    task1 = Mock()
    task2 = Mock()
    task3 = Mock()
    task1.is_complete.return_value = False
    task2.is_complete.return_value = False
    task3.is_complete.return_value = False
    task_list.add(task1)
    task_list.add(task2)
    task_list.add(task3)
    task1.is_complete.return_value = True
    task2.is_complete.return_value = True
    task3.is_complete.return_value = True
    assert task_list.all_complete() == True

