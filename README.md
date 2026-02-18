# fastapi-latest
==================== commands ==================
D:\campusx_fastapi
python -m venv myenv
.\venv\Scripts\activate
pip install fastapi uvicorn
pip install fastapi uvicorn pydantic --only-binary :all:
winget install --id Git.Git -e --source winget # git installation
pip install pydantic
pip install 'pydantic[email]' # required for email validator

uvicorn filename:app--reload
uvicorn main:app --reload
uvicorn app:app --reload

http://127.0.0.1:8000/docs

=================== errors =========================
error1:
    ImportError: cannot import name 'TypeAdapter' from 'pydantic' (D:\campusx_fastapi\myenv\Lib\site-packages\pydantic\__init__.py)
sol: pip install --upgrade pydantic 
--------

---------------------------------------------------------------------------------------------------
                                                            Model
---------------------------------------------------------------------------------------------------                                                           
1. Download model.pkl 
2. pip install "scikit-learn==1.6.1"
3. pip install pandas
 
