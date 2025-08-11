#!/usr/bin/env python3
"""
TaskModel - Modelo de datos para las tareas
Maneja la lógica de las tareas de la aplicación
"""

class TaskModel:
    """Clase para manejar las tareas de la aplicación"""
    
    def __init__(self):
        """Inicializar el modelo de tareas"""
        self.tasks = []
        self.next_id = 1
    
    def add_task(self, description):
        """Añadir una nueva tarea"""
        task = {
            'id': self.next_id,
            'description': description,
            'completed': False
        }
        self.tasks.append(task)
        self.next_id += 1
        print(f"Tarea añadida: {description}")
    
    def list_tasks(self):
        """Listar todas las tareas"""
        if not self.tasks:
            print("No hay tareas disponibles.")
            return
        
        for task in self.tasks:
            status = "✓" if task['completed'] else "○"
            print(f"{status} [{task['id']}] {task['description']}")
    
    def get_task_by_id(self, task_id):
        """Obtener una tarea por su ID"""
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None
