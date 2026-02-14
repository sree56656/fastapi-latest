# fastapi-latest
==================== commands ==================
D:\campusx_fastapi
python -m venv myenv
.\myenv\Scripts\activate
pip install fastapi uvicorn
pip install fastapi uvicorn pydantic --only-binary :all:
winget install --id Git.Git -e --source winget # git installation
pip install pydantic
pip install 'pydantic[email]' # required for email validator

uvicorn filename:app--reload
uvicorn main:app --reload

http://127.0.0.1:8000/docs

=================== errors =========================
error1:
    ImportError: cannot import name 'TypeAdapter' from 'pydantic' (D:\campusx_fastapi\myenv\Lib\site-packages\pydantic\__init__.py)
sol: pip install --upgrade pydantic 
--------
error2:
    
