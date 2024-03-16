import webbrowser
from datetime import datetime
from collections import defaultdict

# Sample data
tasks_completed = [
    {'date': '2024-03-16', 'task': 'Complete assignment 1', 'points': 100},
    {'date': '2024-03-16', 'task': 'Get groceries', 'points': 0},
    {'date': '2024-03-16', 'task': 'Submit coding project', 'points': 100},
    {'date': '2024-03-16', 'task': 'Write code', 'points': 0},
    {'date': '2024-03-16', 'task': 'Attend practice', 'points': 0},
]

# Get the current date
current_date = datetime.now().strftime('%Y-%m-%d')

# Initialize a defaultdict to store points per task
points_per_task = defaultdict(int)

# Calculate points for tasks completed today
total_points_today = 0
for task in tasks_completed:
    if task['date'] == current_date and task['points'] != 0:
        points_per_task[task['task']] += task['points']
        total_points_today += task['points']

# Get the tasks that haven't been completed today
tasks_not_finished = set(task['task'] for task in tasks_completed if task['date'] == current_date and task['points'] == 0)
# Create an HTML string
html_output = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Task Points for {current_date}</title>
    <style>
        h1 {{
            text-align: center;
            color: pink;
        }}
    </style>
</head>
<body>
    <h1>CalicoFocus</h1>
    <h2>Task List</h2>
    <h3>Items completed on {current_date}</h3>
    <ul>
"""

for task, points in points_per_task.items():
    html_output += f"        <li>{task}: {points} points</li>\n"

html_output += """
    </ul>
"""

if tasks_not_finished:
    html_output += """
    <h3>Not Finished</h3>
    <ul>
    """
    for task in tasks_not_finished:
        html_output += f"        <li>{task}</li>\n"
    html_output += "    </ul>\n"

html_output += f"""
    <p>Total points: {total_points_today}</p>
</body>
</html>
"""

# Save the HTML string to a file
html_file_path = '/Users/inthilachanthirat/task_points.html'
with open(html_file_path, 'w') as file:
    file.write(html_output)

# Open the HTML file in a web browser
webbrowser.open('file://' + html_file_path)
