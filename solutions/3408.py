# https://leetcode.com/problems/design-task-manager/

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = tasks
        self.task_map = {}
        self.sort_map = SortedDict()
        for userId, taskId, priority in tasks:
            self.task_map[taskId] = (userId, priority)
            self.sort_map[(priority, taskId)] = userId

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (userId, priority)
        self.sort_map[(priority, taskId)] = userId

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, old_priority = self.task_map[taskId]
        del self.sort_map[(old_priority, taskId)]

        self.task_map[taskId] = (self.task_map[taskId][0], newPriority)        
        self.sort_map[(newPriority, taskId)] = userId

    def rmv(self, taskId: int) -> None:
        userId, priority = self.task_map[taskId]
        del self.task_map[taskId]
        del self.sort_map[(priority, taskId)]

    def execTop(self) -> int:
        if not self.sort_map:
            return -1

        key, userId = self.sort_map.popitem(-1)
        taskId = key[1]
        del self.task_map[taskId]

        return userId


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
