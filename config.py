from environs import Env

env = Env()
env.read_env()
API_TOKEN = env.str('BOT_TOKEN')