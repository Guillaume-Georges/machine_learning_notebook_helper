from IPython.display import display, HTML

# Registers
CLUE_REGISTRY = {}
SOLUTION_REGISTRY = {}

# Embed clues and solutions directly
CLUES_AND_SOLUTIONS = {
    "clues": {
        "ClueImportDataset": "Use: !wget -q {your_link}",
        "ClueDisplayDataset": "Use `pd.read_csv('the_name_of_file.csv')` to load the dataset. Then, use the `.head()` method to display the first few rows.",
        "ClueIdentifyMissingValues": "Use `len(your_dataset)` to find the number of rows. Then, use the `.isnull().sum()` method to count the missing values for each column.",
        "ClueRemoveMissingValues": "Apply `.dropna()` to your dataset to remove rows with missing values. Then use the same method with the code above to check if it worked."
    },
    "solutions": {
        "SolutionImportDataset": "!wget -q https://raw.githubusercontent.com/Guillaume-Georges/diabetes-dataset-machine-learning-course/refs/heads/main/diabetes_dataset_missing_values.csv",
        "SolutionDisplayDataset": "import pandas as pd; dataset = pd.read_csv('diabetes_dataset_missing_values.csv'); dataset.head()",
        "SolutionIdentifyMissingValues": """total_rows = len(dataset)
missing_counts = dataset.isnull().sum()
print(f"Total number of rows in the dataset: {total_rows}")
print("Missing values per column:")
print(missing_counts)""",
        "SolutionRemoveMissingValues": """cleaned_dataset = dataset.dropna();
print(cleaned_dataset.isnull().sum())""",
        "SolutionShowDataTypes": "print(cleaned_dataset.dtypes)",
        "SolutionCountUniqueValues": "print(your_dataset_name[[\"gender\", \"location\", \"smoking_history\"]].nunique())",
        "SolutionLabelEncoding": """data_encoded = cleaned_dataset.copy()
data_encoded = pd.get_dummies(data_encoded, columns=['gender', 'smoking_history'])
label_encoder = LabelEncoder()
data_encoded['location'] = label_encoder.fit_transform(data_encoded['location'])
data_encoded['race:Hispanic'] = data_encoded['race:Hispanic'].round().astype(int)
data_encoded.head()"""
    }
}

# Initialize the CLUE_REGISTRY and SOLUTION_REGISTRY with the embedded data
CLUE_REGISTRY.update(CLUES_AND_SOLUTIONS["clues"])
SOLUTION_REGISTRY.update(CLUES_AND_SOLUTIONS["solutions"])

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
