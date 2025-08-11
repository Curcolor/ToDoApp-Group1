#!/usr/bin/env python3
"""
ToDoApp - Aplicación de gestión de tareas
Proyecto colaborativo del Grupo 1
"""

from task_model import TaskModel

def main():
    """Función principal de la aplicación"""
    print("=== ToDoApp - Gestión de Tareas ===")
    
    # Crear algunas tareas de ejemplo
    task_manager = TaskModel()
    
    # Añadir tareas iniciales
    task_manager.add_task("Completar proyecto de Git")
    task_manager.add_task("Estudiar para el examen")
    task_manager.add_task("Revisar documentación")
    
    # Mostrar tareas
    print("\nTareas actuales:")
    task_manager.list_tasks()
    
    # Ejemplo usando los métodos de Jairo
    print("\n--- Marcando tarea 1 como terminada ---")
    task_manager.set_done(1)
    
    print("\nTareas después de marcar como terminada:")
    task_manager.list_tasks()
    
    print("\n--- Removiendo tarea 2 ---")
    task_manager.remove_task(2)
    
    print("\nTareas después de remover:")
    task_manager.list_tasks()

if __name__ == "__main__":
    main()
