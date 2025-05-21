from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import pandas as pd
import plotly.graph_objects as go
import io
from fastapi.responses import Response

router = APIRouter()

class ScheduleItem(BaseModel):
    days: str
    time: str
    teacher: str
    seatsLeft: int
    classStarted: bool
    subject: str
    course_id: str

@router.post("/visualize-table")
def visualize_table(data: List[ScheduleItem]):
    try:
        # Convert to pandas DataFrame
        df = pd.DataFrame([item.dict() for item in data])
        
        # Create a table using plotly
        fig = go.Figure(data=[go.Table(
            header=dict(
                values=list(df.columns),
                fill_color='paleturquoise',
                align='left'
            ),
            cells=dict(
                values=[df[col] for col in df.columns],
                fill_color='lavender',
                align='left'
            )
        )])
        
        # Update layout for better appearance
        fig.update_layout(
            title="Schedule Table",
            height=400,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        # Convert the figure to bytes
        img_bytes = fig.to_image(format="png")
        
        # Return the image
        return Response(content=img_bytes, media_type="image/png")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 