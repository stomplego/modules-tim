# Deployment Package for my_own_namespace.yandex_cloud_elk

## Содержимое
- `my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz` - Архив коллекции
- `simple_use_role.yml` - Пример playbook для использования роли

## Установка и использование

### 1. Установите коллекцию
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz

### 2. Запустите playbook
ansible-playbook simple_use_role.yml

## Требования
- Ansible >= 2.9
- Python >= 3.8

## Описание
Playbook создаёт файл /tmp/quick_test.txt с содержимым, содержащим текущее время.
