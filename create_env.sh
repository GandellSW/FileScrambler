# Create python3 virtual environment (called env)
python3 -m venv env

# Enter in the virtual environment (called env)
source env/bin/activate

# Install required libs in virtual environment (-U update if allready installed)
pip install -U -r requirements.txt
