# clues.py
CLUE_REGISTRY = {}
SOLUTION_REGISTRY = {}

from IPython.display import HTML, display

def setup_clue(clue_id, clue):
    CLUE_REGISTRY[clue_id] = clue

def setup_solution(solution_id, solution):
    SOLUTION_REGISTRY[solution_id] = solution

def show_clue(clue_id):
    if clue_id not in CLUE_REGISTRY:
        display(HTML(f"<p style='color: red;'>Error: Clue ID '{clue_id}' not found.</p>"))
        return
    clue = CLUE_REGISTRY[clue_id]
    display(HTML(f"""
    <div>
        <button onclick="document.getElementById('clue-{clue_id}').style.display='block'; this.style.display='none';">
            Reveal Clue
        </button>
        <div id="clue-{clue_id}" style="display:none; margin-top:10px; padding:10px; border:1px solid #ccc;">
            <p>{clue}</p>
        </div>
    </div>
    """))

def show_solution(solution_id):
    if solution_id not in SOLUTION_REGISTRY:
        display(HTML(f"<p style='color: red;'>Error: Solution ID '{solution_id}' not found.</p>"))
        return
    solution = SOLUTION_REGISTRY[solution_id]
    display(HTML(f"""
    <div>
        <button onclick="document.getElementById('solution-{solution_id}').style.display='block'; this.style.display='none';">
            Reveal Solution
        </button>
        <div id="solution-{solution_id}" style="display:none; margin-top:10px; padding:10px; border:1px solid #ccc;">
            <pre>{solution}</pre>
        </div>
    </div>
    """))
