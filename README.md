<img alt="Coding" src="https://github.com/Adeniyii/AirBnB_clone/blob/main/assets/hbnb_logo.png?raw=true">
AirBnB Clone - Console



Introduction

The AirBnB clone's console serves as a command interpreter, providing a means to manipulate data without a visual interface. With this console, you can manage your data model efficiently, performing actions such as creating, updating, and destroying objects.


Features

Data Model Creation: Define and create your data model seamlessly within the console.
Object Management: Manage objects via a command-line interface, allowing for easy manipulation.
File Persistence: Store and persist objects to a JSON file for data consistency and accessibility.


Storage Abstraction

The console integrates a robust storage system, offering an abstraction layer between your objects and their persistence mechanisms. This abstraction ensures that:

Flexibility: You can seamlessly switch between storage types without modifying your codebase.
Ease of Maintenance: Updates to the storage system won't require extensive changes to your code.
Validation Tool: The console serves as a validation tool for testing the storage engine's functionality.
With the console, you can focus on your application's logic and functionality without worrying about the intricacies of data storage and persistence.


# Files and Directories

## `models` Directory
- Contains all classes used for the entire project.
- In an object-oriented programming (OOP) project, a class represents an object or instance.

## `tests` Directory
- Houses all unit tests for the project.

## `console.py`
- Serves as the entry point of the command interpreter.

## `models/base_model.py`
- Defines the base class for all models.
- Includes common elements such as:
  - Attributes: `id`, `created_at`, and `updated_at`.
  - Methods: `save()` and `to_json()`.

## `models/engine` Directory
- Contains all storage classes, utilizing the same prototype.
- Currently, it includes:
  - `file_storage.py`: Handles file storage functionality.

These directories and files are essential components of the project structure, facilitating organization and functionality across the entire application.



Command Interpreter Description

Starting the Command Interpreter
To start the command interpreter, run the console.py file in your terminal or command prompt.
python3 console.py


Using the Command Interpreter
Once the command interpreter is running, you'll see a prompt (hbnb) awaiting your commands.
You can type commands directly into the prompt to interact with the system.
Available Commands:
create: Creates a new instance of a specified class.

Syntax: create <class_name>
Example: create BaseModel
show: Prints the string representation of an instance based on class name and ID.

Syntax: show <class_name> <instance_id>
Example: show BaseModel 1234-1234-1234
Additional Commands (Optional):
You can extend the command interpreter to include more functionality based on your project requirements.
These additional commands could include updating instances, deleting instances, listing all instances of a class, etc.


Examples

- Creating a new instance:
(hbnb) create BaseModel

- Showing an instance:
(hbnb) show BaseModel 1234-1234-1234

- Exiting the command interpreter:
(hbnb) quit
