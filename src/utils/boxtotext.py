from ocrresultwithboxes import OcrResultWithBoxes
from utils.stringUtil import fixArabic

def get_text_from_ocr_result_boxes(result_with_boxes: OcrResultWithBoxes, inlcude_score: bool = True):
    text_data = ''
    for box in result_with_boxes:
        if inlcude_score:
            text_data += f'{fixArabic(box[1])} {box[2]}\n'
        else:
            text_data += f'{fixArabic(box[1])}\n'
    return text_data
