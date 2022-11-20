from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("PRODUCTION_API_TOKEN")  # Bot token
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili



DATABASE_HOST=env.str("DATABASE_HOST")
DATABASE_NAME=env.str("DATABASE_NAME")
DATABASE_USER=env.str("DATABASE_USER")
DATABASE_PORT=env.str("DATABASE_PORT")
DATABASE_PASSWORD=env.str("DATABASE_PASSWORD")
DATABASE_URI=env.str("DATABASE_URI")

#PRODUCTION_API_TOKEN
#DEVELOPMENT_BOT_TOKEN





