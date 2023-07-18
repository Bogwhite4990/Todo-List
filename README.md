# Python Todo List Web Application

This is a simple Python Todo List web application built with Flask. It allows users to add, delete, and view their todo items with the added feature of mapping tasks to emojis. The application uses the Flask framework and the `emoji` library to enhance the todo items with emojis.

## Installation

To run this Python Todo List web application, follow the steps below:

1. Make sure you have Python installed on your system. You can download Python from the official website: [Python.org](https://www.python.org/downloads/)
2. Clone the repository or download the source code files to your local machine.
3. Open a command line or terminal and navigate to the project directory.
4. Install the required dependencies by running the following command: pip install flask emoji
5. Once the dependencies are installed, execute the following command to start the application: python app.py

6. The application will start running locally on your machine. Open your web browser and visit `http://localhost:5000` to access the Todo List web application.

## Usage

- **Home Page:** The home page displays the list of todo items. Each item is displayed with an associated emoji, based on the task.

- **Add Task:** To add a new task to the todo list, enter the task in the input field provided on the home page and click the "Add" button.

- **Delete Task:** To delete a task from the todo list, click the "Delete" button next to the task on the home page.

## Customizing Emojis

The application allows you to map tasks to emojis. To add or modify the emoji mappings, follow these steps:

1. Open the `app.py` file in a text editor.
2. Locate the `emoji_mapping` dictionary in the code. It contains a set of predefined mappings of tasks to emojis.
3. To add a new mapping, insert a new key-value pair in the dictionary. The key should be the task (in lowercase), and the value should be the corresponding emoji code. You can find emoji codes from websites like [Emoji Cheat Sheet](https://www.webfx.com/tools/emoji-cheat-sheet/).

Example:
```python
emoji_mapping = {
    'run': ':man_running:',
    'eat': ':hamburger:',
    'sleep': ':sleeping_face:',
    'new_task': ':rocket:',  # Add a new task with its corresponding emoji
}

```

Save the app.py file after making the changes.
Restart the application by stopping the current execution and running python app.py again. The updated emoji mappings will take effect.

# Conclusion
This Python Todo List web application provides a simple and interactive way to manage your tasks. By mapping tasks to emojis, it adds a fun element to your todo list. Feel free to customize the application according to your needs and preferences.

