#!/bin/bash
# Скрипт для автоматической установки коллекции и запуска playbook

echo "=== Установка коллекции my_own_namespace.yandex_cloud_elk ==="
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz --force

echo -e "\n=== Запуск playbook ==="
ansible-playbook simple_use_role.yml

echo -e "\n=== Проверка созданного файла ==="
cat /tmp/quick_test.txt
