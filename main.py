from dotenv import load_dotenv
load_dotenv()

from sylliba.api.translation_api import APIServer

server = APIServer()
server.start()