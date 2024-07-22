from modules.translation.translation import Translation
from modules.translation.data_models import TranslationRequest

translation = Translation()

request = TranslationRequest(
    text="Hello",
    task_string="text2speech",
    source_lang="English",
    target_lang="French"
)

response = translation.translate(request)