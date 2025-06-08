import uuid

class Task:
    def __init__(self, task_id, name, description=""):
        self.id = task_id
        self.name = name
        self.description = description
        self.state = False

    def mark_as_done(self):
        self.state = True

    def __str__(self):
        state_str = "✅ HOTOVÁ" if self.state else "❌ NEHOTOVÁ"
        return f"[{state_str}] {self.name} (ID: {self.id}) - {self.description}"

    def mark_as_undone(self):
        self.state = False