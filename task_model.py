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
            'is_done': False  # Usando is_done en lugar de completed
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
            status = "✓" if task['is_done'] else "○"  # Usando is_done
            print(f"{status} [{task['id']}] {task['description']}")
    
    def get_task_by_id(self, task_id):
        """Obtener una tarea por su ID"""
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None
    
    def set_done(self, task_id):
        """Marcar una tarea como terminada (método de Jairo)"""
        task = self.get_task_by_id(task_id)
        if task:
            task['is_done'] = True
            print(f"Tarea {task_id} marcada como terminada: {task['description']}")
            return True
        else:
            print(f"No se encontró la tarea con ID {task_id}")
            return False
    
    def remove_task(self, task_id):
        """Remover una tarea por su ID (método de Jairo)"""
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            print(f"Tarea {task_id} removida: {task['description']}")
            return True
        else:
            print(f"No se encontró la tarea con ID {task_id}")
            return False
