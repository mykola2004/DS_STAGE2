To launch the project, use following commands in terminal opened from project's main repository:
- docker-compose up -d  
- docker exec -it mlflow-client bash

In opened bash, run:  
- python ./src/run_experiments.py

now, you can check completed experiments, visiting: http://localhost:5000

Finding best model and saving its artifacts(in src/release), code can be done with command:  
- python ./src/find_best_model.py
