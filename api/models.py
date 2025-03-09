from djongo import models

class Task(models.Model):
    task_id = models.IntegerField(primary_key=True)  # 明確指定主鍵
    task_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    task_type = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_completed = models.BooleanField()

    def __str__(self):
        return self.task_name

class Interaction(models.Model):
    interaction_id = models.IntegerField()
    object_type = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.object_type} - {self.action}"

class Path(models.Model):
    start_position_x = models.IntegerField()
    start_position_y = models.IntegerField()
    end_position_x = models.IntegerField()
    end_position_y = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"From ({self.start_position_x}, {self.start_position_y}) to ({self.end_position_x}, {self.end_position_y})"

class NPC(models.Model):
    npc_id = models.IntegerField(primary_key=True)  # 明確指定主鍵
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    current_task = models.IntegerField()
    status = models.CharField(max_length=50)
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    last_active = models.DateTimeField()
    tasks = models.JSONField(blank=True, default=list)  # 使用 JSONField 替代嵌套模型
    path = models.JSONField(blank=True, default=list)  # 使用 JSONField 替代嵌套模型
    interactions = models.JSONField(blank=True, default=list)  # 使用 JSONField 替代嵌套模型
    level = models.IntegerField()
    experience = models.IntegerField()
    last_level_up = models.DateTimeField()

    def __str__(self):
        return self.name
