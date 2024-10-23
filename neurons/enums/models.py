LLMS : list[str] = [
    "modules.llms.llama",
    # "modules.llms.flan_t5_large"
]

TTS : list[str] = [
    "modules.tts.seamless"
]

MODELS: dict = {
}

PROMPTS: dict = {
    "GENERATE_INPUT_DATA": """You are an expert story teller.
You can write short stories that capture the imagination, 
end readers on an adventure and complete an alegorical thought all within 100~200 words. 
Please write a short story about {topic} in {source_language}. 
Keep the story short but be sure to use an alegory and complete the idea.""",
    "GENERATE_OUTPUT_DATA": """
Provided text is written in {source_language}.
Please translate into {target_language}
Don't put any tags, description or decorators.
Write only translated text in raw text format.
""",
    "EVALUATE_RESULT": """Evaluate the following translation:\n\n\
Original Text: {original}\n\
Translation: {translation}\n\n\
Rate the quality of this translation on a scale from 0 to 10, floating point is possible\
where 0 means it's very poor and 10 means it's flawless. Please provide only the number."""}