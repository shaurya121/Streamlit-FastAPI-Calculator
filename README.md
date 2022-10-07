
# Streamlit FastAPI Calculator App

Here, we will-
1) Create a basic Python Calculator module.
2) Serve the function from the module using FastAPI.
3) Creating a very basic UI using Streamlit.
4) Integrating Streamlit & FastAPI.


## Screenshots
Idea:
![App Screenshot](https://raw.githubusercontent.com/shaurya121/Streamlit-FastAPI-Calculator/main/Idea.png)
UI:
![App Screenshot](https://raw.githubusercontent.com/shaurya121/Streamlit-FastAPI-Calculator/main/Screenshots/Streamlit_frontend.png)
FastAPI Server:
![App Screenshot](https://raw.githubusercontent.com/shaurya121/Streamlit-FastAPI-Calculator/main/Screenshots/FastAPI_server.png)
Streamlit Server:
![App Screenshot](https://raw.githubusercontent.com/shaurya121/Streamlit-FastAPI-Calculator/main/Screenshots/streamlit_server.png)

## Installation

Install required modules using:

```python
pip install fastapi
pip install uvicorn
```
## Usage/Examples
Create a calculator module:
```python
def calculate(operation, x, y):
	if operation=='+ Addition':
		return x+y
	elif operation=='- Subtraction':
		return abs(x-y)
```


Now we’ll create a basic request body. We’ll create a class User_input using pydantic’s BaseModel for type validation and sending the arguments to the calculator function, which we will simply import from the calculator module we created above.
```python
class User_input(BaseModel):
	operation: str
	x: float
	y: float
app= FastAPI()
@app.post("/calculate")
def operate(input: User_input):
	result=calculate(input.operation, input.x, input.y)
	return result
```

Create the web app using Streamlit-
```python
st.title: Display text in title formatting.
st.write: Write arguments to the app.
st.selectbox: Display a select widget.
st.slider: Display a slider widget.
st.button: Display a button widget.
```


Assemble Frontend with Backend-
```python
# For running streamlit app
streamlit run stream_lit.py
# For running backend with FastAPI
uvicorn fast_api:app --reload
```


## Acknowledgements

 - [Medium.com](https://medium.com/codex/streamlit-fastapi-%EF%B8%8F-the-ingredients-you-need-for-your-next-data-science-recipe-ffbeb5f76a92)
 
 

