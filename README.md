Download ollama for windows
verify version thru cmd
//ollama pull llama3.2
//ollama run llama3.2   ..test it and say /bye
//http://localhost:11434 : should show ollama is running this shows local api service is active.
 Come to VS code:
 create a new folder
 //python -m venv venv
//venv\Scripts\activate
//pip install fastapi uvicorn requests
create main.py file and copy the code mentioned above.
in terminal:
//uvicorn main:app --reload
Test the inference and the agent thru swagger UI.


