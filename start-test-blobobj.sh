#!/usr/bin/bash
# запуск тестов для проверки Blob Oblects
# ключ -s указывает путь где находятся
python -m unittest discover -s blobobj/tests/ $1