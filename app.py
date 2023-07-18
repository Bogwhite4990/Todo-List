from flask import Flask, render_template, request, redirect, url_for
import emoji

app = Flask(__name__)

# Store the todo list items
todos = []

# Mapping of tasks to emojis
emoji_mapping = {
    'run': ':man_running:',
    'eat': ':hamburger:',
    'sleep': ':sleeping_face:',
    # Add emoji here from here https://www.webfx.com/tools/emoji-cheat-sheet/
}


def add_emoji(task):
    # Check if the task is in the mapping
    if task.lower() in emoji_mapping:
        # Get the emoji for the task
        emoji_icon = emoji_mapping[task.lower()]
        # Add the emoji to the task
        task_with_emoji = f"{task} {emoji.emojize(emoji_icon)}"
        return task_with_emoji
    else:
        return task


@app.route('/')
def home():
    todos_with_emoji = [add_emoji(todo) for todo in todos]
    return render_template('index.html', todos=todos_with_emoji)


@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        todos.append(todo)
    return redirect(url_for('home'))


@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(todos):
        del todos[index]
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
