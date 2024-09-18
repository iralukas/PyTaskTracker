import datetime
import sys
import PyQt5
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from TaskManager import Task


class TaskWidgetView(QFrame):
    def __init__(self, task: Task):
        super().__init__()

        self.task = task
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Add labels for task attributes
        layout.addWidget(QLabel(f"Task Name: {self.task.name}"))
        layout.addWidget(QLabel(f"Description: {self.task.description}"))
        layout.addWidget(QLabel(f"Deadline Time: {self.task.deadline_time.isoformat()}"))
        layout.addWidget(QLabel(f"Status: {self.task.status.name}"))

        self.setLayout(layout)
        self.setFixedSize(300, 100)  # Width: 300px, Height: 200px
        # self.setFrameShape(QFrame.StyledPanel)
        self.setObjectName('Custom_Widget')
        self.setStyleSheet("""
           #Custom_Widget {
             border-radius: 10px;
             opacity: 100;
             border: 1px solid #000000;                   
                }""")


class TaskWidget(QFrame):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Add labels for task attributes
        layout.addWidget(QLabel(f"Task Name: {self.task.name}"))
        layout.addWidget(QLabel(f"Description: {self.task.description}"))
        layout.addWidget(QLabel(f"Deadline Time: {self.task.deadline_time.isoformat()}"))
        layout.addWidget(QLabel(f"Status: {self.task.status.name}"))

        self.setLayout(layout)
        self.setFixedSize(300, 100)  # Width: 300px, Height: 200px
        self.setFrameShape(QFrame.StyledPanel)

    def parse_task(self):
        values = None
        task = Task(values)
        return task


class WindowApp:
    def __init__(self):
        self.tasks = []

        self.draw()

    def draw(self):
        app = QApplication(sys.argv)
        window = QWidget()
        window.setWindowTitle("TaskTracker")
        # window.move(500,200)
        tabs = QTabWidget()
        tab1 = QWidget()
        layoutTab1 = QVBoxLayout()

        self.add_task(Task("Задача", "Некоторая задача", True, datetime.datetime.now()))
        self.add_task(Task("Задача", "Некоторая задача", True, datetime.datetime.now()))

        for task in self.tasks:
            layoutTab1.addWidget(task)
        tab1.setLayout(layoutTab1)

        tab2 = QWidget()
        layoutTab2 = QVBoxLayout()
        tab2Label = QLabel("Welcome on second")
        layoutTab2.addWidget(tab2Label)
        tab2.setLayout(layoutTab2)
        tabs.addTab(tab1, "My tasks")
        tabs.addTab(tab2, "Add task")
        verticalBox = QVBoxLayout()
        verticalBox.addWidget(tabs)

        window.show()
        window.setLayout(verticalBox)
        sys.exit(app.exec())

    def add_task(self, task: Task):
        qtTask = TaskWidgetView(task)
        self.tasks.append(qtTask)


if __name__ == "__main__":
    WindowApp()
