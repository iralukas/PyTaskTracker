import enum
from dataclasses import dataclass
from datetime import datetime
import sched
import time


class TaskStatus(enum.IntEnum):
    not_started = enum.auto()
    in_progress = enum.auto()
    done = enum.auto()
    archived = enum.auto()


@dataclass
class Task:
    name: str = "New task"
    description: str = "The task that needs to be done"
    is_limited_time: bool = False
    deadline_time: datetime = -1
    status: TaskStatus = TaskStatus.not_started  # fixme maybe int


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.fill_tasks()

    def fill_tasks(self):
        self.add_task(name="Task 1")

    def add_task(self, name, description='', deadline=None):
        '''
        Add another task to manager
        :param name:
        :type name:
        :param description:
        :type description:
        :param deadline:
        :type deadline:
        :return:
        :rtype:
        '''
        if deadline:
            self.tasks.append(Task(name, description, True, deadline))
        else:
            self.tasks.append(Task(name, description))
        self.notify("Задача успешно добавлена")

    def get_all_tasks(self):
        return self.tasks

    def notify(self, msg):
        '''
        Notify user that something has happened
        :param msg:
        :type msg:
        :return:
        :rtype:
        '''
        print(msg)
