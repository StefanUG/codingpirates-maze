import subprocess
import os

def run_script(script_path):
    env = os.environ.copy()
    # Add your custom environment variable
    env["TESTMODE"] = "True"

    result = subprocess.run(['python', script_path], env=env, stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').strip()
    
    print(f"{output} {script_path}")

def visit_dir(dir):
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        if os.path.isdir(path):
            visit_dir(path)
        elif file.endswith(".py") and file != "test_all.py":
            run_script(path)


if __name__ == "__main__":
    visit_dir(os.path.dirname(os.path.abspath(__file__)))
    print("DONE")
