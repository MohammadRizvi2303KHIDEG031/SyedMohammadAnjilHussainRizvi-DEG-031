import fire
import mlflow
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score




def setup_knn_pipeline(k):
    knn = KNeighborsClassifier(n_neighbors=k)
    pipe = make_pipeline(StandardScaler(), knn)
    return pipe




def track_with_mlflow(model, X_test, Y_test, mlflow, model_metadata):
    mlflow.log_params(model_metadata)
    mlflow.log_metric("accuracy", model.score(X_test, Y_test))
    mlflow.sklearn.log_model(model, "knn", registered_model_name="sklearn_knn")


def main(max_k: int):
    
    data = load_wine()
    wine_x = data.data
    wine_x = wine_x[:-2]
    wine_y = data.target
    wine_y = wine_y[:-2]
    x_train, x_test, y_train, y_test = train_test_split(wine_x, wine_y, test_size=0.2, random_state=0)
    scaler = StandardScaler()

    k_list = range(1, max_k)

    for k in k_list:
        with mlflow.start_run():
            knn_pipe = setup_knn_pipeline(k)
            knn_pipe.fit(x_train, y_train)
            model_metadata = {"k": k}
            track_with_mlflow(knn_pipe, x_test, y_test, mlflow, model_metadata)


if __name__ == "__main__":
    fire.Fire(main)
