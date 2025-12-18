import os
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    for i in range(11):
        inner_path = os.path.join(path, f"folder_{i}")
        if not os.path.exists(inner_path):
            os.makedirs(inner_path)