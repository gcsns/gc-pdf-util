import os

AUTH_SERVER_BASE_URL=os.environ.get("AUTH_SERVER_BASE_URL")

AUTH_SERVER_ENDPOINTS={
    "JWKS_JSON": '/api/oauth2/jwks.json',
}

AUTH_SERVER_ISSUER = os.environ.get("AUTH_SERVER_ISSUER")

AUTH_SERVER_AUDIENCE = os.environ.get("AUTH_SERVER_AUDIENCE", AUTH_SERVER_ISSUER)

DEFAULT_OCR = os.environ.get("DEFAULT_OCR", "azure")

ENABLED_OCRS = os.environ.get("ENABLED_OCRS", "rapidOcr,azure,azureCvRead,azureDi,suryaOcr").split(',')

ENABLED_TEXT_LLM_MODELS = os.environ.get("ENABLED_TEXT_LLM_MODELS", "gpt-3.5-turbo,azure:gpt-3-5").split(',')

ENABLED_VISION_LLM_MODELS = os.environ.get("ENABLED_VISION_LLM_MODELS", "gpt-4o,gpt-4o-2024-08-06,gpt-4o-mini,gpt-4"
                                    +",gemini-pro"
                                    +",claude-3-haiku-20240307,claude-3-opus-20240229,claude-3-sonnet-20240229,claude-3-5-haiku-20241022,claude-3-5-sonnet-20240620,claude-3-5-sonnet-20241022"
                                    +",bedrock:anthropic.claude-3-haiku-20240307-v1:0,bedrock:anthropic.claude-3-5-haiku-20241022-v1:0"
                                    +",bedrock:anthropic.claude-3-5-sonnet-20240620-v1:0,bedrock:us.anthropic.claude-3-5-sonnet-20241022-v2:0"
                                    +",azure:gpt-4,azure:gpt-4o,azure:gpt-4o-mini").split(',')

STRUCTURED_OUTPUT_MODELS = os.environ.get("STRUCTURED_OUTPUT_MODELS", "gpt-4o,gpt-4o-2024-08-06,gpt-4o-mini,gpt-4o-mini-2024-07-18"
                                    +",azure:gpt-4o").split(',')

ENABLED_LLM_MODELS = ENABLED_TEXT_LLM_MODELS + ENABLED_VISION_LLM_MODELS

DEFAULT_LLM_MODEL = os.environ.get("DEFAULT_LLM_MODEL", "azure:gpt-3-5")

CONFIDENCE_SCORE_THRESHOLD = float(os.environ.get("CONFIDENCE_SCORE_THRESHOLD", "0"))

DEFAULT_EMBEDDING_SCORE_THRESHOLD = float(os.environ.get("DEFAULT_EMBEDDING_SCORE_THRESHOLD", "0.5"))

GOOGLE_AI_STUDIO_API_KEY = os.environ.get("GOOGLE_AI_STUDIO_API_KEY")

HANDWRITING_DETECTION_QUERY_TEMPLATE = os.environ.get("HANDWRITING_DETECTION_QUERY_TEMPLATE")

PADDLE_RETRY_COUNTS = int(os.environ.get("PADDLE_RETRY_COUNTS", "4"))

PADDLE_RETRY_INTERVAL = int(os.environ.get("PADDLE_RETRY_INTERVAL", "2"))

LINE_MERGE_CRITERIA_MEDIAN_PERCENTAGE = float(os.environ.get("LINE_MERGE_CRITERIA_MEDIAN_PERCENTAGE", "100"))

LINE_MERGE_CRITERIA_MAX_DELTAS = int(os.environ.get("LINE_MERGE_CRITERIA_MAX_DELTAS", "3"))

LINE_MERGE_CRITERIA_ALLOWED_WIDTH_ALIGNMENT_GAP_PERCENTAGE = float(os.environ.get("LINE_MERGE_CRITERIA_ALLOWED_WIDTH_ALIGNMENT_GAP_PERCENTAGE", "2"))

ENABLED_EMBEDDING_MODELS = os.environ.get("ENABLED_EMBEDDING_MODELS", "openai:text-embedding-ada-002,openai:text-embedding-3-small,openai:text-embedding-3-large"
                                          +",hf,hf:nomic-ai/nomic-embed-text-v1,hf:nomic-ai/nomic-embed-text-v1.5"
                                          +",hf:intfloat/multilingual-e5-large-instruct"
                                          +",hf-bge,hf-bge:Salesforce/SFR-Embedding-Mistral,hf-bge:mixedbread-ai/mxbai-embed-large-v1,hf-bge:WhereIsAI/UAE-Large-V1,hf-bge:BAAI/bge-m3"
                                          +",azure:text-embedding-ada-002"
                                          +",nomic:nomic-embed-text-v1,nomic:nomic-embed-text-v1.5"
                                          +",voyage:voyage-law-2"
                                          +",bedrock:cohere.embed-multilingual-v3"
                                          ).split(',')

# Number of pages after which embedding will be used in pdf-query
EMBEDDING_PAGE_THRESHOLD = int(os.environ.get("EMBEDDING_PAGE_THRESHOLD", "4"))

EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL", "azure:text-embedding-ada-002")

SPLITTER_CHUNK_SIZE = int(os.environ.get("SPLITTER_CHUNK_SIZE", "6000"))

SPLITTER_CHUNK_OVERLAP = int(os.environ.get("SPLITTER_CHUNK_OVERLAP", "1000"))

USE_OCR_SCORE_IN_PDF_QUERY = os.environ.get("USE_OCR_SCORE_IN_PDF_QUERY", "False").lower() == "true"

IBAN_VALIDATION_BASE_URL = os.environ.get("IBAN_VALIDATION_BASE_URL", "https://openiban.com/validate/")

AZURE_VISION_ENDPOINT = os.environ.get("AZURE_VISION_ENDPOINT")

AZURE_VISION_KEY = os.environ.get("AZURE_VISION_KEY")

AZURE_CV_READ_ENDPOINT = os.environ.get("AZURE_CV_READ_ENDPOINT")

AZURE_CV_READ_KEY = os.environ.get("AZURE_CV_READ_KEY")

AZURE_DI_ENDPOINT = os.environ.get("AZURE_DI_ENDPOINT")

AZURE_DI_KEY = os.environ.get("AZURE_DI_KEY")

TEMPORARY_IMAGE_FOLDER = os.environ.get("BLUR_TEMPORARY_IMAGE_FOLDER", "images")

TENSORFLOW_LITE_MODEL = os.environ.get("BLUR_TENSORFLOW_LITE_MODEL", "blur_detection.tflite")

IMAGE_SIZE_X = int(os.environ.get("BLUR_IMAGE_SIZE_X", "600"))

IMAGE_SIZE_Y = int(os.environ.get("BLUR_SPLITTER_CHUNK_SIZE_MULTI", "600"))

AZURE_TRANSLATOR_KEY = os.environ.get("AZURE_TRANSLATOR_KEY", "2702551a98e74a81bd1aa0d492c24b12")

AZURE_TRANSLATOR_LOCATION = os.environ.get("AZURE_TRANSLATOR_LOCATION", "uaenorth")

AZURE_TRANSLATOR_ENDPOINT = os.environ.get("AZURE_TRANSLATOR_ENDPOINT", "https://api.cognitive.microsofttranslator.com")

BEDROCK_TIMEOUT = int(os.environ.get("BEDROCK_TIMEOUT", "150"))

# ELA RPA Configs

ELA_RPA_SCALE = int(os.environ.get("ELA_RPA_SCALE", 30))
ELA_RPA_QUALITY = int(os.environ.get("ELA_RPA_QUALITY", 80))
ELA_RPA_THRESHOLD = int(os.environ.get("ELA_RPA_THRESHOLD", 7))

SIGNATURE_MATCHING_CONSTANT_1=int(os.environ.get("SIGNATURE_MATCHING_CONSTANT_1", 84))
SIGNATURE_MATCHING_CONSTANT_2=int(os.environ.get("SIGNATURE_MATCHING_CONSTANT_2", 250))
SIGNATURE_MATCHING_CONSTANT_3=int(os.environ.get("SIGNATURE_MATCHING_CONSTANT_3", 100))
SIGNATURE_MATCHING_CONSTANT_4=int(os.environ.get("SIGNATURE_MATCHING_CONSTANT_4", 18))
SIGNATURE_MATCHING_THRESHOLD = float(os.environ.get("SIGNATURE_MATCHING_THRESHOLD", 0.7))