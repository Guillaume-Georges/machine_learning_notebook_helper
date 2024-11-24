# progress.py
import ipywidgets as widgets
from IPython.display import HTML, display

PROGRESS_TRACKER = {}

def score_your_task(task_id, task_description):
    score_dropdown = widgets.Dropdown(
        options=[("Select your score", None),
                 ("1 - Without the clue (Full Score)", 1.0),
                 ("0.75 - With the clue (Partial Credit)", 0.75),
                 ("0.5 - With the solution (Minimal Credit)", 0.5)],
        description="Score:",
        style={'description_width': 'initial'}
    )
    save_button = widgets.Button(description="Submit Score")
    output = widgets.Output()

    def save_score(_):
        if score_dropdown.value is None:
            with output:
                output.clear_output()
                print(f"Please select a score for '{task_id}' before submitting.")
        else:
            PROGRESS_TRACKER[task_id] = score_dropdown.value
            with output:
                output.clear_output()
                print(f"Score for '{task_id}' saved as: {score_dropdown.value}")

    save_button.on_click(save_score)
    display(HTML(f"<h4>{task_description}</h4>"))
    display(score_dropdown, save_button, output)

def display_total_score():
    total_score = sum(PROGRESS_TRACKER.values())
    max_score = len(PROGRESS_TRACKER)
    display(HTML(f"<p><b>Total Score:</b> {total_score}/{max_score}</p>"))
