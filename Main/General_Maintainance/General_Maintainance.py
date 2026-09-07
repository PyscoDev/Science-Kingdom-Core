import sys
import os
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))
modules_dir = os.path.join(current_dir,'..','Custom_Modules')
sys.path.append(modules_dir)
terminal_dir = os.path.join(current_dir,'..','..','Terminal_Scripts','Linux','Debian')
sys.path.append(terminal_dir)

from Env_Loader import Gatekeeper

def run_bash_with_password(script_path, password):
    try:
        result = subprocess.run(["bash", script_path],input=password,text=True,capture_output=True,check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"

if __name__== "__main__":

    Root_Holder=Gatekeeper()
    Root_Password= Root_Holder.unlock("fake_sudo")

    print("\n\nInitiating the System Maintainance ...............\n\n")
    print("\n\nInitiating the System Upgrade ...............\n\n")
    target_script = os.path.join(terminal_dir, "system_upgrader.sh")
    result = run_bash_with_password(target_script, Root_Password)
    print(result)
    print("\n\nInitiating Temporary File Cleaning ...............\n\n")
    target_script = os.path.join(terminal_dir, "cache_cleaner.sh")
    result = run_bash_with_password(target_script, Root_Password)
    print(result)
    print("\n\nSystem Maintainance Complete...............\n\n")