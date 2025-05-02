1. Firstly, run command(in root directory of the project):  
docker-compose up --build

2. In order to test flask server open another command prompt window and run command: 
Invoke-RestMethod -Uri http://localhost:5000/predict -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"features": [5.1, 3.5, 14, 9.0]}' 
or for powershell:
Invoke-RestMethod -Uri http://localhost:5000/predict -Method POST -Body '{"features": [5.1, 3.5, 1.4, 9.0]}' -ContentType "application/json"

3. To test batch model deployment just check folder /batch_deployment locally, every minute file output.csv will be updated wih predictions corresponding to input values(file input.csv)


In order to run tests, firstly run rest_api/app.py file, then open in root directory of the project command prompt and run: 
pytest tests/
