### here we'll create an api for customer 

import os
import numpy as np
import pandas as pd
from mlproject.pipeline.prediction import PredictionPipeline
from fastapi import FastAPI
from pydantic import BaseModel
from src.mlproject.constant import schema_file_path
from src.mlproject.utils.common import read_yaml_file
from typing import Dict

app=FastAPI()

columns_name=read_yaml_file(schema_file_path)
column_data_type=columns_name.columns
col_val=({key:"" for key,val in column_data_type.items()})

class ColumnsInput(BaseModel):
    columns_name: Dict[str, str] 
    
    class Config:
        orm_mode = True
        json_schema_extra = {
            "example": {
                "columns_name": col_val
            }
        }


@app.get('/trainpipelinestart')
def training():
    os.system("python main.py")
    return "training pipeline started"


@app.post("/predict")
def predict_value(columns:ColumnsInput):
    request=columns.columns_name
    alcohol=float(request['alcohol'])
    chlorides=float(request['chlorides'])
    citric_acid=float(request['citric acid'])
    fixed_acidity=float(request['fixed acidity'])
    free_sulfur_dioxide=float(request['free sulfur dioxide'])
    ph_val=float(request['pH'])
    quality=float(request['quality'])
    residual_sugar=float(request['residual sugar'])
    sulphates=float(request['sulphates'])
    total_sulfur_dioxide=float(request['total sulfur dioxide'])
    volatile_acidity=float(request['volatile acidity'])
    
    val=[[alcohol,chlorides,citric_acid,fixed_acidity,free_sulfur_dioxide,ph_val,quality,residual_sugar,sulphates,
                total_sulfur_dioxide,volatile_acidity]]
    
    data=np.array(val).reshape(1,11)
    obj=PredictionPipeline()
    predict=obj.predict(data)
    
    return {"prediction value":str(predict)}