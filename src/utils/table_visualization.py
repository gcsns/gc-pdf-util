from typing import List, Dict, Optional
import pandas as pd
import plotly.graph_objects as go
from fastapi import HTTPException
from pydantic import BaseModel

class ScheduleItem(BaseModel):
    days: str
    time: str
    teacher: str
    seatsLeft: int
    classStarted: bool
    subject: str
    course_id: str

def create_table_visualization(
    data: List[ScheduleItem],
    column_widths: Optional[Dict[str, int]] = None
) -> bytes:
    """
    Creates a table visualization from the schedule data and returns it as PNG bytes.
    
    Args:
        data (List[ScheduleItem]): List of schedule items to visualize
        column_widths (Optional[Dict[str, int]]): Dictionary mapping column names to their widths in pixels.
            If not provided, default widths will be used.
            Example: {"days": 100, "time": 150, "teacher": 200}
        
    Returns:
        bytes: PNG image bytes of the table visualization
        
    Raises:
        HTTPException: If there's an error during visualization
    """
    try:
        # Convert to pandas DataFrame
        df = pd.DataFrame([item.dict() for item in data])
        
        # Default column widths if not provided
        default_widths = {
            "days": 100,
            "time": 150,
            "teacher": 150,
            "seatsLeft": 100,
            "classStarted": 100,
            "subject": 300,
            "course_id": 200
        }
        
        # Use provided widths or defaults
        widths = column_widths if column_widths is not None else default_widths
        
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
            ),
            columnwidth=[widths.get(col, 100) for col in df.columns]  # Use provided width or default to 100
        )])
        
        # Update layout for better appearance
        fig.update_layout(
            title="Schedule Table",
            height=400,
            width=1000,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        # Convert the figure to bytes
        img_bytes = fig.to_image(format="png")
        
        return img_bytes
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 