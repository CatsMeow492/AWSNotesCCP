import os
import subprocess

def run_command(command, timeout=60):
    try:
        print(f"Running command: {command}")  # Debug print
        result = subprocess.run(command, shell=True, text=True, timeout=timeout)
        print(f"Command finished: {command}")  # Debug print
        return result
    except subprocess.TimeoutExpired:
        print(f"Error: Command '{command}' timed out after {timeout} seconds.")
        return None
    except KeyboardInterrupt:
        print("Process interrupted by user.")
        return None

def safe_remove(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found, skipping removal.")
    except PermissionError:
        print(f"Error: No permission to remove {file_path}.")

# Remove files
safe_remove("study_guide.md")
safe_remove("output.mp3")

# Run main.py
print("Changing directory to questionShuffler")
os.chdir("questionShuffler")
print("Directory changed to questionShuffler")  # Debug print
run_command("python3 main.py")

# Run studyGuideGenerator.py
print("Changing directory to ..")
os.chdir("..")
try:
    answer = input("Would you like to run studyGuideGenerator? (Y/N): ").strip().lower()
    if answer == 'y':
        run_command("python3 studyGuideGenerator.py")
    else:
        print("Skipping studyGuideGenerator.")
except KeyboardInterrupt:
    print("\nProcess interrupted by user. Exiting gracefully.")
    os.chdir("..")  # Ensure the directory is changed back if needed
    exit(0)

# Remove failed_questions.txt
print("Changing directory to questionShuffler")
os.chdir("questionShuffler")
print("Directory changed to questionShuffler")  # Debug print
safe_remove("failed_questions.txt")
print("Changing directory to ..")
os.chdir("..")

# Run readToMe.py
answer = input("Would you like to run readToMe? (Y/N): ").strip().lower()
if answer == 'y':
    run_command("python3 readToMe.py")
else:
    print("Skipping readToMe.")

# Play output.mp3
run_command("mpg123 output.mp3")

if __name__ == "__main__":
    try:
        run_command("python3 main.py")
    except KeyboardInterrupt:
        print("Main process interrupted by user.")
