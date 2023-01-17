"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import chardet
import subprocess  # подпроцесс

ARGS = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]
for ping_res in ARGS:
    ping_proc = subprocess.Popen(ping_res, stdout=subprocess.PIPE)
    print(ping_proc.stdout)

    for line in ping_proc.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding'])
        print(line)
