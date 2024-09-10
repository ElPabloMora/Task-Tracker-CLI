import json
import os
from datetime import datetime
import argparse

#create global variable
FILENAME = 'json_task.json'

def read_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME,'r') as file:
            return json.load(file)
    return []

def write_tasks(registros_existentes):
    if os.path.exists(FILENAME):
        with open(FILENAME,'w') as file:
            json.dump(registros_existentes, file, indent=4)
            
def add_task(desc):
    registros_existentes =  read_tasks()
    #find the last id in the records
    last_id = max(ts['id'] for ts in registros_existentes) if registros_existentes else 0
    #create a new task with dictionary format
    new_task = {
            "id":last_id + 1,
            "description":desc,
            "status":'progress',
            "createdAt":datetime.now().isoformat(),
            "updatedAt":"None"
    }

    registros_existentes.append(new_task)   

    write_tasks(registros_existentes)
        
def update_task(task_id,new_desc):
    
    registros_existentes = read_tasks()
    
    for ts in registros_existentes:
        if ts['id'] == task_id:
            ts['description'] = new_desc
            ts['updatedAt'] = datetime.now().isoformat()
            #hacemos la escritura en el archivo
            write_tasks(registros_existentes)
            return
    print("Tarea no encontrada.")
        
def delete_task(task_id):
    
    registros_existentes = read_tasks()
    
    registros_existentes = [ts for ts in registros_existentes if ts["id"] != task_id]
    
    write_tasks(registros_existentes)

def mark_in_progress(task_id):
    
    registros_existentes = read_tasks()
    
    for ts in registros_existentes:
        if ts['id'] == task_id:
            ts['status'] = 'progress'
            write_tasks(registros_existentes)
            return
    print('Tarea no encontrada')
    
def mark_done(task_id):
    
    registros_existentes = read_tasks()
    
    for ts in registros_existentes:
        if ts['id'] == task_id:
            ts['status'] = 'done'
            write_tasks(registros_existentes)
            return
    print('Tarea no encontrada')

def list_tasks(filter_status):
    
    registros_existentes = read_tasks()
    
    if not registros_existentes:
        print("No tasks")
        return
    
    filter_tasks = registros_existentes
   
    if filter_status:
        filter_tasks = [ts for ts in registros_existentes if ts['status'] == filter_status]
    
    if not filter_tasks:
        print("Tasks no found")
        return 
      
    for task in filter_tasks:
        print(f"{task['id']},{task['description']},{task['status']},{task['createdAt']},{task['updatedAt']},")

def main():
    parser = argparse.ArgumentParser(description='Task Tracker')
    subparsers = parser.add_subparsers(dest='command')
    
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Description')
    
    list_parser = subparsers.add_parser('list', help='List of tasks')
    list_parser.add_argument('status', choices=['all', 'done', 'in-progress'],  default='all', help='Filter tasks')
    
    delete_parser = subparsers.add_parser('delete', help='Delete in List')
    delete_parser.add_argument('id', type=int, help='Identification')
    
    update_parser = subparsers.add_parser('update', help='Update tasks')
    update_parser.add_argument('id', type=int, help='Identification')
    update_parser.add_argument('new_description', type=str, help='New description')
    
    mark_done_parser = subparsers.add_parser('mark-done', help='mark the task completed')
    mark_done_parser.add_argument('id', type=int, help='Identification')
    
    mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help='mark the task in process')
    mark_in_progress_parser.add_argument('id', type=int, help='Identification')
    
    args = parser.parse_args()
    
    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'list':
        if args.status == 'all':
            list_tasks()
        else:
            list_tasks(args.status)
    elif args.command== 'mark-done':
        mark_done(args.id)
    elif args.command== 'mark-in-progress':
        mark_in_progress(args.id)
    elif args.command== 'update':
        update_task(args.id,args.new_description)
    elif args.command == 'delete':
        delete_task(args.id)
        
if __name__ == '__main__':
    main()