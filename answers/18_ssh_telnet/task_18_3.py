# -*- coding: utf-8 -*-
"""
Задание 18.3

Создать функцию send_commands (для подключения по SSH используется netmiko).

Параметры функции:
* device - словарь с параметрами подключения к одному устройству
* show - одна команда show (строка)
* config - список с командами, которые надо выполнить в конфигурационном режиме

Аргументы show и config должны передаваться только как ключевые. При передачи
этих аргументов как позиционных, должно генерироваться исключение TypeError.

In [4]: send_commands(r1, 'sh clock')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-75adcfb4a005> in <module>
----> 1 send_commands(r1, 'sh clock')

TypeError: send_commands() takes 1 positional argument but 2 were given


В зависимости от того, какой аргумент был передан, функция вызывает разные функции
внутри. При вызове функции send_commands, всегда должен передаваться
только один из аргументов show, config. Если передаются оба аргумента, должно
генерироваться исключение ValueError.

Далее комбинация из аргумента и соответствующей функции:
* show - функция send_show_command из задания 18.1
* config - функция send_config_commands из задания 18.2

Функция возвращает строку с результатами выполнения команд или команды.

Проверить работу функции:
* со списком команд commands
* командой command

Пример работы функции:

In [14]: send_commands(r1, show='sh clock')
Out[14]: '*17:06:12.278 UTC Wed Mar 13 2019'

In [15]: commands = ['username user5 password pass5', 'username user6 password pass6']

In [16]: send_commands(r1, config=commands)
Out[16]: 'config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#username user5 password pass5
R1(config)#username user6 password pass6
R1(config)#end
R1#'

"""
import yaml
from task_18_1 import send_show_command
from task_18_2 import send_config_commands


commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
command = "sh ip int br"


def send_commands(device, *, config=None, show=None):
    if show and config:
        raise ValueError("Можно передавать только один из аргументов show/config")
    elif show:
        return send_show_command(device, show)
    elif config:
        return send_config_commands(device, config)


if __name__ == "__main__":
    commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    r1 = devices[0]
    print(send_commands(r1, config=commands))
    print(send_commands(r1, show=command))
