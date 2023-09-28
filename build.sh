#!/bin/bash
set -o errexit

# Determine the virtual environment activation script based on the operating system
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Windows
    activate_script="venv/Scripts/activate"
else
    # Unix-like systems
    activate_script="venv/bin/activate"
fi

# Create and activate the virtual environment
python -m venv venv
source "$activate_script"

# Install required packages
pip install Flask torch torchvision nltk
pip install gunicorn==19.7.1


# Copy 'punkt' dataset to the default NLTK data path
python -c "import nltk, shutil; shutil.copytree('nltk_data', nltk.data.find('corpora'))"


# /opt/render/project/src/venv/bin/python -m pip install --upgrade pip

# Install required Python packages from requirements.txt
pip install -r requirements.txt


