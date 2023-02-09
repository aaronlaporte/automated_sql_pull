@ECHO OFF 
TITLE Execute python script on anaconda environment
ECHO Please Wait...
:: Section 1: Activate the environment.
ECHO ============================
ECHO Conda Activate
ECHO ============================
@CALL "C:\Users\me\Anaconda3\condabin\activate.bat"
:: Section 2: Execute python script.
ECHO ============================
ECHO asps.py  ::THIS DOESNT MATTER, JUST A LABEL
ECHO ============================
python "FILEPATH TO PYTHON FILE YOU WANT TO ACTIVATE"

ECHO ============================
ECHO End
ECHO ============================

PAUSE