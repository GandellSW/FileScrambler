Rem Create python3 virtual environment (called env)
python -m venv env

Rem Enter in the virtual environment (called env)
.\env\Scripts\activate

Rem Install required libs in virtual environment (-U update if allready installed)
pip install -U -r requirements.txt
