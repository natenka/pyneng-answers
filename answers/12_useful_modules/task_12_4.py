# -*- coding: utf-8 -*-
"""
Задание 12.4

Создать функцию find_n_ip.

Параметры функции:
* ip_from_range1 - IP-адрес из диапазона адресов range1
* range1 - диапазон IP-адресов вида "10.1.1.1-10.1.2.2"
* range2 - диапазон IP-адресов вида "10.2.2.100-10.2.3.101"

Функция должна определить каким адресом по счету является адрес ip_from_range1
в диапазоне range1. И найти такой же адрес по счету в диапазоне range2.

Функция должна возвращать найденный IP-адрес в виде строки "10.5.1.3"

Например, если передать функции find_n_ip такие аргументы:
new_ip = find_n_ip("10.1.1.17", "10.1.1.1-10.1.1.30", "50.1.1.1-50.1.1.20")

new_ip должен быть равен "50.1.1.17"

Если передать такие аргументы:
new_ip = find_n_ip("10.1.1.127", "10.1.1.100-10.1.2.200", "50.1.1.110-50.1.2.210")

new_ip должен быть равен "50.1.1.137"
"""


from ipaddress import ip_address


def find_n_ip(ip_from_range1, range1, range2):
    range_list = "-".join([range1, range2]).split("-")
    start1, end1, start2, end2 = [ip_address(i) for i in range_list]

    ip = ip_address(ip_from_range1)

    current_ip = start1
    index = 0
    while True:
        if current_ip == ip:
            break
        elif current_ip > end1:
            raise ValueError(f"IP {ip} не в диапазоне {range1}")
        index += 1
        current_ip += 1

    match_ip = start2
    for _ in range(index):
        match_ip += 1
    if match_ip > end2:
        raise ValueError(f"Найденный IP {match_ip} не в диапазоне {range2}")
    return str(match_ip)


def find_n_ip(ip_from_range1, range1, range2):
    range_list = "-".join([range1, range2]).split("-")
    start1, end1, start2, end2 = [int(ip_address(i)) for i in range_list]
    ip = int(ip_address(ip_from_range1))
    if ip > end1:
        raise ValueError(f"IP {ip} не в диапазоне {range1}")

    index = ip - start1
    match_ip = start2 + index
    if match_ip > end2:
        raise ValueError(f"Найденный IP {match_ip} не в диапазоне {range2}")
    return str(ip_address(match_ip))


if __name__ == "__main__":
    print(find_n_ip("10.1.1.127", "10.1.1.100-10.1.2.200", "50.1.1.110-50.1.2.210"))
