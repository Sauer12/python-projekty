import json
from classes.task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.last_id = 0

    def add_task(self, name, description=""):
        self.last_id += 1
        task = Task(self.last_id, name, description)
        self.tasks.append(task)
        print("✅ Úloha bola pridaná.")
        self.save_to_file()

    def list_tasks(self):
        if not self.tasks:
            print("⚠️ Zoznam úloh je prázdny.")
        for task in self.tasks:
            print(task)

    def mark_task_done(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_as_done()
                print("☑️ Úloha bola označená ako hotová.")
                self.save_to_file()
                return
        print("❌ Úloha s týmto ID neexistuje.")

    def mark_task_undone(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_as_undone()
                print("🔁 Úloha bola označená ako nehotová.")
                self.save_to_file()
                return
        print("❌ Úloha s týmto ID neexistuje.")


    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print("🗑️ Úloha bola odstránená.")
                self.save_to_file()
                return
        print("❌ Úloha s týmto ID neexistuje.")


    def save_to_file(self, filename="tasks.json"):
        with open(filename, "w") as file:
            data = [task.__dict__ for task in self.tasks]
            json.dump(data, file, indent=4)
        print("💾 Úlohy boli uložené do súboru.")

    def load_from_file(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                content = file.read()
                if not content.strip():
                    print("⚠️ Súbor je prázdny. Neboli načítané žiadne úlohy.")
                    return

                data = json.loads(content)
                self.tasks = []
                max_id = 0
                for item in data:
                    item_id = int(item["id"])
                    task = Task(item_id, item["name"], item["description"])
                    if item_id > max_id:
                        max_id = item_id
                    task.state = item["state"]
                    self.tasks.append(task)

                self.last_id = max_id
                print("📂 Úlohy boli načítané zo súboru.")
        except FileNotFoundError:
            print("⚠️  Súbor nenájdený. Zatiaľ neexistuje žiadny zoznam úloh.")
        except json.decoder.JSONDecodeError:
            print("❌ Súbor je poškodený alebo neobsahuje platný JSON.")