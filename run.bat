@echo off

IF NOT EXIST .env (
    python -m venv .env
    cd .env\Scripts
    call activate
    cd ../..
    pip install -r requirements.txt
) ELSE (
    cd .env\Scripts
    call activate
    cd ../..
)
python.exe main.py
