import tkinter as tk
from tkinter import messagebox, simpledialog
from classes.task_manager import TaskManager


class TaskManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager GUI v1.0")
        self.manager = TaskManager()
        self.manager.load_from_file()

        self.task_listbox = tk.Listbox(root, width=100, height=15, font=("Segoe UI Variable Text", 15))
        self.task_listbox.pack(pady=10)

        # Vstupné polia
        self.entry_name = tk.Entry(root, width=40, font=("Segoe UI Variable Text", 15))
        self.entry_name.pack()
        self.entry_name.insert(0, "Názov úlohy")
        self.entry_name.bind("<FocusIn>", lambda event: self.clear_placeholder(self.entry_name, "Názov úlohy"))
        self.entry_name.bind("<FocusOut>", lambda event: self.restore_placeholder(self.entry_name, "Názov úlohy"))

        self.entry_description = tk.Entry(root, width=40, font=("Segoe UI Variable Text", 15))
        self.entry_description.pack()
        self.entry_description.insert(0, "Popis úlohy (nepovinný)")
        self.entry_description.bind("<FocusIn>", lambda event: self.clear_placeholder(self.entry_description,
                                                                                      "Popis úlohy (nepovinný)"))
        self.entry_description.bind("<FocusOut>", lambda event: self.restore_placeholder(self.entry_description,
                                                                                         "Popis úlohy (nepovinný)"))

        # Tlačidlá
        tk.Button(root, text="Pridať úlohu", command=self.add_task, font=("Segoe UI Variable Text", 15)).pack(pady=(30, 10))
        tk.Button(root, text="Označiť ako hotovú", command=self.mark_done, font=("Segoe UI Variable Text", 15)).pack(pady=(0, 10))
        tk.Button(root, text="Označiť ako nehotovú", command=self.mark_undone, font=("Segoe UI Variable Text", 15)).pack(pady=(0, 10))
        tk.Button(root, text="Odstrániť úlohu", command=self.delete_task, font=("Segoe UI Variable Text", 15)).pack(pady=(0, 10))

        # Odložené vykreslenie úloh pre rýchlejší štart
        self.root.after(100, self.refresh_task_list)

    def clear_placeholder(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)

    def restore_placeholder(self, entry, placeholder):
        if not entry.get().strip():
            entry.insert(0, placeholder)

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.manager.tasks):
            self.task_listbox.insert(tk.END, str(task))
        for index, task in enumerate(self.manager.tasks):
            farba = '#d6f5d6' if task.state else '#f5d6d6'
            self.task_listbox.itemconfig(index, {'bg': farba})

    def add_task(self):
        name = self.entry_name.get()
        description = self.entry_description.get()
        if not name.strip() or name == "Názov úlohy":
            messagebox.showwarning("Upozornenie", "Názov úlohy nemôže byť prázdny.")
            return
        if description == "Popis úlohy (nepovinný)":
            description = ""
        if len(description) > 50:
            messagebox.showwarning("Upozornenie", "Popis úlohy nesmie presiahnuť 50 znakov.")
            return
        self.manager.add_task(name, description)
        self.refresh_task_list()
        self.entry_name.delete(0, tk.END)
        self.entry_name.insert(0, "Názov úlohy")
        self.entry_description.delete(0, tk.END)
        self.entry_description.insert(0, "Popis úlohy (nepovinný)")

    def get_selected_task_id(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showinfo("Info", "Prosím vyber úlohu zo zoznamu.")
            return None
        index = selection[0]
        return self.manager.tasks[index].id

    def mark_done(self):
        task_id = self.get_selected_task_id()
        if task_id is not None:
            self.manager.mark_task_done(task_id)
            self.refresh_task_list()

    def mark_undone(self):
        task_id = self.get_selected_task_id()
        if task_id is not None:
            self.manager.mark_task_undone(task_id)
            self.refresh_task_list()

    def delete_task(self):
        task_id = self.get_selected_task_id()
        if task_id is not None:
            self.manager.delete_task(task_id)
            self.refresh_task_list()


if __name__ == "__main__":
    root = tk.Tk()
    def nastav_ikonu():
        try:
            icon = tk.PhotoImage(file="icon.png")
            root.iconphoto(True, icon)
        except Exception as e:
            print("⚠️ Ikona nebola načítaná:", e)
    root.after(500, nastav_ikonu)
    root.resizable(False, False)
    root.update_idletasks()
    width = 700
    height = 600
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    gui = TaskManagerGUI(root)
    root.mainloop()
