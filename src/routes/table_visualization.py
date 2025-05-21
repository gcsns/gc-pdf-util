from fastapi import APIRouter
from fastapi.responses import Response
from typing import List, Dict, Optional
from utils.table_visualization import ScheduleItem, create_table_visualization

router = APIRouter()

@router.post("/visualize-table")
def visualize_table(
    data: List[ScheduleItem],
    column_widths: Optional[Dict[str, int]] = None
):
    """
    Endpoint to visualize schedule data as a table image.
    
    Args:
        data (List[ScheduleItem]): List of schedule items to visualize
        column_widths (Optional[Dict[str, int]]): Dictionary mapping column names to their widths in pixels.
            If not provided, default widths will be used.
            Example: {"days": 100, "time": 150, "teacher": 200}
        
    Returns:
        Response: PNG image response containing the table visualization
    """
    img_bytes = create_table_visualization(data, column_widths)
    return Response(content=img_bytes, media_type="image/png") 