import os
import sys

print("DJANGO_SETTINGS_MODULE (before) =", os.environ.get("DJANGO_SETTINGS_MODULE"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mikan_project.settings")
print("DJANGO_SETTINGS_MODULE (after)  =", os.environ.get("DJANGO_SETTINGS_MODULE"))


# 1) Djangoプロジェクトへのパスを通す
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)

# 2) settings.py を指定
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mikan_project.settings")

# 3) Djangoを起動
import django
django.setup()

# 4) ASGIハンドラを取得
from django.core.handlers.asgi import ASGIHandler

app = ASGIHandler()
