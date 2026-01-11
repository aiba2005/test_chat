import sys
from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parent
sys.path.append(str(ROOT_DIR.parent))
from fastapi import FastAPI
import uvicorn
from starlette.middleware.sessions import SessionMiddleware
from mysite.api import auth
from mysite.config import SECRET_KEY
from mysite.api import auth, group_people, chat_group, user, chat_wb, message_chat

app = FastAPI()

app.include_router(auth.auth_router)
app.include_router(user.user_router)
app.include_router(chat_group.group_router)
app.include_router(group_people.people_router)
app.include_router(chat_wb.chat_router)
app.include_router(message_chat.message_router)

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)