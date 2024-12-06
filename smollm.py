#!/usr/bin/env python3

import subprocess
import sys
import platform

def check_command_exists(command):
    """Check if a command-line tool is available on the system."""
    try:
        subprocess.run([command, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

def install_ollama_mac():
    """
    Attempt to install Ollama if it's not found on macOS using Homebrew.
    """
    if check_command_exists("brew"):
        print("Attempting to install Ollama using Homebrew...")
        try:
            subprocess.run(["brew", "install", "ollama/tap/ollama"], check=True)
            return True
        except subprocess.CalledProcessError:
            print("Failed to install Ollama via Homebrew. Please install Ollama manually.")
            return False
    else:
        print("Homebrew not found. Please install Ollama manually from https://docs.ollama.ai.")
        return False

def install_ollama_ubuntu():
    """
    Attempt to install Ollama on Ubuntu using the provided instructions.
    """
    print("Attempting to install Ollama on Ubuntu...")
    try:
        # Try the direct install script
        subprocess.run(["curl", "-fsSL", "https://ollama.com/install.sh"], check=True, stdout=subprocess.PIPE)
        # Pipe the shell script into sh
        subprocess.run(["sh"], input=subprocess.run(["curl", "-fsSL", "https://ollama.com/install.sh"], 
                                                   capture_output=True, text=True).stdout.encode("utf-8"), check=True)
        return True
    except subprocess.CalledProcessError:
        print("Automatic installation via the install script failed, attempting manual install...")
        # Manual install steps
        try:
            subprocess.run(["curl", "-L", "https://ollama.com/download/ollama-linux-amd64.tgz", "-o", "ollama-linux-amd64.tgz"], check=True)
            subprocess.run(["sudo", "tar", "-C", "/usr", "-xzf", "ollama-linux-amd64.tgz"], check=True)
            # Start Ollama in the background
            subprocess.Popen(["ollama", "serve"])
            return True
        except subprocess.CalledProcessError:
            print("Failed to manually install Ollama. Please refer to https://ollama.ai for further instructions.")
            return False

def install_ollama():
    """
    Install Ollama depending on the platform.
    """
    system = platform.system().lower()
    if system == "darwin":
        return install_ollama_mac()
    elif system == "linux":
        # Attempt a simple check for Ubuntu by checking /etc/os-release
        try:
            with open('/etc/os-release') as f:
                contents = f.read().lower()
                if 'ubuntu' in contents:
                    return install_ollama_ubuntu()
                else:
                    print("This Linux distribution is not explicitly supported. Please install Ollama manually.")
                    return False
        except FileNotFoundError:
            print("Cannot determine Linux distribution. Please install Ollama manually.")
            return False
    else:
        print("This script only supports macOS or Ubuntu at the moment. Please install Ollama manually.")
        return False

def download_model(model_name="smollm:135m"):
    """
    Download (pull) the specified SmolLM model using Ollama.
    """
    print(f"Downloading the {model_name} model...")
    try:
        subprocess.run(["ollama", "pull", model_name], check=True)
        print("Model downloaded successfully.")
    except subprocess.CalledProcessError:
        print("Failed to download the model. Please ensure that Ollama is properly set up.")
        sys.exit(1)

def run_model(model_name="smollm:135m", prompt=""):
    """
    Run the specified SmolLM model with the given prompt using Ollama.
    """
    print(f"Running the {model_name} model...")
    try:
        # `ollama run` will run the model with the given prompt
        result = subprocess.run(["ollama", "run", model_name], input=prompt.encode("utf-8"), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        output = result.stdout.decode("utf-8").strip()
        print("\nModel output:")
        print(output)
    except subprocess.CalledProcessError as e:
        print("Failed to run the model:")
        print(e.stderr.decode("utf-8"))

if __name__ == "__main__":
    # Check if Ollama is installed, if not try to install it
    if not check_command_exists("ollama"):
        print("Ollama not found on this system.")
        if not install_ollama():
            sys.exit(1)

    # Download the SmolLM model
    download_model("smollm:135m")

    # Ask the user for a prompt
    user_prompt = input("Please enter your prompt: ")

    # Run the model with the user's prompt
    run_model("smollm:135m", user_prompt)
