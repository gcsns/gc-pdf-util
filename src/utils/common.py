import re
from field import Field
import copy
from utils.stringUtil import fixArabic
from utils.pdftoimage import from_pdf_to_image_bytes
from utils.fileUtil import FileUtil

def remove_non_alphanumeric_and_convert_to_lower(text: str)-> str:
    # Using regular expression to substitute non-alphanumeric characters with an empty string
    return re.sub(r'[^a-zA-Z0-9]', '', text).lower()

def has_repetitive_words(input_string: str)-> bool:
    # Split the input string into words
    words = input_string.lower().split()
    
    # Create a dictionary to store word counts
    word_count = {}
    
    # Iterate through each word
    for word in words:
        # Increment the count for this word in the dictionary
        word_count[word] = word_count.get(word, 0) + 1
        
    # Check if any word appears more than once
    for count in word_count.values():
        if count > 1:
            return True  # Found repetitive words
    
    return False  # No repetitive words found

def fix_arabic_text_in_output(llmJson: dict, fields: list[Field])->dict:
        validatedResult = copy.deepcopy(llmJson)
        for field in fields:
            valueDictOrListOfDict = validatedResult.get(field.name)
            if not valueDictOrListOfDict:
                continue

            if isinstance(valueDictOrListOfDict, list):
                for i in range(len(valueDictOrListOfDict)):
                    valueDict = valueDictOrListOfDict[i]
                    if not valueDict:
                        continue
                    
                    value = valueDict.get("value")
                    if value:
                        valueDictOrListOfDict[i]["value"] = fixArabic(value)
                    continue
            elif isinstance(valueDictOrListOfDict, dict):    
                value = valueDictOrListOfDict.get("value")
                if value:
                    validatedResult[field.name]["value"] = fixArabic(value)
            
        return validatedResult

def fix_arabic_text_in_nested_output(input):
    if isinstance(input, list):
        return [fix_arabic_text_in_nested_output(value) for value in input]
    elif isinstance(input, dict):
        return {key: fix_arabic_text_in_nested_output(value) for key,value in input.items()}
    elif isinstance(input, str):
        return fixArabic(input)
    return input

def transform_file_to_llm_images(fileContent: bytes, filename: str):
    imageContentForLlm = []
    isPdf = filename.lower().endswith(".pdf")

    if not isPdf:
        return [{
            "type": "image_url",
            "image_url": {
                "url": FileUtil.convert_to_base64_with_mime(fileContent, filename)
            }
        }]
    
    filenameWithoutPrefix = filename.replace(".pdf", "")
    images = from_pdf_to_image_bytes(fileContent)
    for ind, value in enumerate(images):
        imageContentForLlm.append({
            "type": "image_url",
            "image_url": {
                "url": FileUtil.convert_to_base64_with_mime(value, f"{filenameWithoutPrefix}_{ind}.jpeg")
            }
        })

    return imageContentForLlm
