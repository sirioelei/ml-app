## Info
This app trains a model on iris dataset from sklearn.

## Requirements
Required dependencies are listed in file `requirements.txt`

## How to use it
### Model training
Start `python app.py` - it will train model and save it into `iris_model.pkl`
### Usage
start `python main.py` in terminal and then create http request `localhost:5000/predict` with request body

```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```
It can be tested using curl
``` bash
curl -X POST -H "Content-Type: application/json" -d '{"features":[5.1, 3.5, 1.4, 0.2]}' http://localhost:5000/predict
```
### docker-compose
To run as a docker container run - it will build docker image
```bash
docker-compose up --build
```
