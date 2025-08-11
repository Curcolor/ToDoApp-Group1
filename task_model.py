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
            'is_completed': False  # Usando is_completed como atributo principal
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
            status = "✓" if task['is_completed'] else "○"  # Usando is_completed
            print(f"{status} [{task['id']}] {task['description']}")
    
    def get_task_by_id(self, task_id):
        """Obtener una tarea por su ID"""
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None
    
    def mark_as_complete(self, task_id):
        """Marcar una tarea como completada"""
        task = self.get_task_by_id(task_id)
        if task:
            task['is_completed'] = True
            print(f"Tarea {task_id} marcada como completada: {task['description']}")
            return True
        else:
            print(f"No se encontró la tarea con ID {task_id}")
            return False
    
    def set_done(self, task_id):
        """Marcar una tarea como terminada (método alternativo de Jairo)"""
        return self.mark_as_complete(task_id)  # Redirige al método principal
    
    def delete_task(self, task_id):
        """Eliminar una tarea por su ID"""
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            print(f"Tarea {task_id} eliminada: {task['description']}")
            return True
        else:
            print(f"No se encontró la tarea con ID {task_id}")
            return False
    
    def remove_task(self, task_id):
        """Remover una tarea por su ID (método alternativo de Jairo)"""
        return self.delete_task(task_id)  # Redirige al método principal
