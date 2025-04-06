import shutil
from mlflow.tracking import MlflowClient

client = MlflowClient()
experiment = client.get_experiment_by_name("Breast Cancer Classification")

best_run = None
best_acc = -1

for run in client.search_runs(experiment.experiment_id):
    acc = run.data.metrics.get("accuracy", 0)
    if acc > best_acc:
        best_acc = acc
        best_run = run

run_id = best_run.info.run_id
experiment_id = experiment.experiment_id

artifact_src = f"/mlflow/mlruns/{experiment_id}/{run_id}/artifacts"
artifact_dst = "/app/release"

print(f"Best model : {best_run.data.params.get('model')}")
print(f"Hyperparameters : {best_run.data.params}")
print(f"Accuracy : {best_acc:.4f}")

shutil.copytree(artifact_src, artifact_dst, dirs_exist_ok=True)

print("Best model artiafcts are copied")