from bt import TaskStatus, Task
import pytest

@pytest.fixture(autouse=True)
def setup():
    pass

def test_task_success():
    class SuccessTask(Task):
        def __init__(self):
            super().__init__()

        def perform_action(self):
            return TaskStatus.SUCCESS

    task = SuccessTask()
    task.step()
    assert task.status == TaskStatus.SUCCESS
