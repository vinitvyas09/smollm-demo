# Ollama SmolLM Setup Script

## Overview

This repository provides a Python script that helps you:

1. Install **Ollama** if it's not already present on your system.
2. Download and run the **SmolLM** 135M model locally.

The `SmolLM` model is a minimal demonstration model (135M parameters) provided for showcase and testing purposes. It is intentionally small and not suitable for production-level tasks. Expect limited capabilities and usefulness.

## Features

- **Automatic Installation (Ubuntu/macOS)**:  
  If Ollama is not found on your system, the script will attempt to install it.  
  - On **Ubuntu**, it tries both the provided `curl` installation script as well as a manual installation method.
  - On **macOS**, it attempts to install using Homebrew.
  
- **Model Downloading**:  
  The script will pull the `smollm:135m` model using Ollama's `ollama pull` command.

- **Interactive Prompt Input**:  
  The script asks you for a prompt and then runs the model to produce a response.

## Requirements

- **Python 3**
- **curl** (required if Ollama is not already installed and you’re on Ubuntu)
- **tar** and `sudo` permissions (for manual installation on Ubuntu)
- Internet connection to download the model and Ollama.

## Instructions

- Ensure you have Python 3 installed.
- Make the script executable:
```bash
chmod +x smollm.py
```
- Run the script:
```bash
./smollm.py
```
If Ollama is not installed, the script will guide you through the installation process.
After the model is downloaded, the script will prompt you to enter input text. Type your prompt and press Enter to see the model’s output.

## Notes on the Model
The SmolLM 135M model is very small, intended purely as a demonstration of how to set up and run models with Ollama.
Do not expect high-quality responses or any complex reasoning from it.
This model is primarily for testing the installation and setup process, as well as for showcasing how one might integrate Ollama with Python. It is not intended for production use or practical applications.
