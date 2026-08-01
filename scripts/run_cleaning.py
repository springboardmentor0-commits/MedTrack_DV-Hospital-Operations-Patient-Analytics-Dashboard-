import json
import os
import pandas as pd
import numpy as np

def run_notebook_cells(nb_path):
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    global_scope = {}
    print(f"Executing cells from {nb_path}...")
    for idx, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            source_code = "".join(cell['source'])
            print(f"Executing Code Cell {cell.get('execution_count', idx)}...")
            exec(source_code, global_scope)
            
    print("All notebook cells executed successfully.")

if __name__ == '__main__':
    run_notebook_cells('hospital_cleaning.ipynb')
