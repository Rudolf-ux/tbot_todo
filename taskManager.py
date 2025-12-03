class TaskManager:
    def __init__(self):
        self.path = "cash.csv"
        self.tasks = []
        self.load_data()

    def save_data(self):

        try:
            with open(self.path, "w", encoding="utf-8") as file:
                for task in self.tasks:
                    file.write(f"{task['name']}:{task['description']}\n")
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")

    def load_data(self):

        try:
            with open(self.path, "r", encoding="utf-8") as file:
                lines = file.readlines()

            for line in lines:
                line = line.strip()
                if not line:
                    continue


                if ':' in line:
                    parts = line.split(':', 1)
                    if len(parts) == 2:
                        name = parts[0].strip()
                        description = parts[1].strip()
                        # Добавляем напрямую в список
                        self.tasks.append({
                            'name': name,
                            'description': description
                        })


        except FileNotFoundError:

            print("Файл не найден, будет создан новый")
            self.tasks = []
        except Exception as e:
            print(f"Ошибка при загрузке: {e}")
            self.tasks = []

    def create_task(self, name, description):

        self.tasks.append({
            'name': name,
            'description': description
        })
        self.save_data()

    def get_str_tasks(self):

        if not self.tasks:
            return "Нет задач"

        result = ""
        for i, task in enumerate(self.tasks, 1):
            result += f"{i}. {task['name']}: {task['description']}\n"
        return result