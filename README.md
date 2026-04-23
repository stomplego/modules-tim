# Yandex Cloud ELK Collection

**my_own_namespace.yandex_cloud_elk**

Коллекция для управления Yandex Cloud ELK стеком с пользовательскими модулями Ansible.

## Требования

- Ansible >= 2.9
- Python >= 3.8

## Установка

```bash
# Установка из архива
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz

# Установка из Git репозитория
ansible-galaxy collection install git+https://github.com/yourusername/my_own_collection.git
Модули
my_own_module
Создаёт текстовый файл на удалённом хосте с указанным содержимым.
Параметры
Параметр	Тип	Обязательный	По умолчанию	Описание
path	str	yes	-	Абсолютный путь для создания файла
content	str	yes	-	Содержимое для записи в файл
Возвращаемые значения
Значение	Тип	Описание
changed	bool	Был ли файл создан или изменён
path	str	Путь к созданному файлу
content	str	Записанное содержимое
uid	int	ID пользователя-владельца
gid	int	ID группы-владельца
owner	str	Имя владельца
group	str	Имя группы
mode	str	Права доступа
size	int	Размер файла в байтах
Примеры
- name: Создать простой файл
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: "/tmp/example.txt"
    content: "Hello, World!"

- name: Создать многострочный файл
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: "/opt/app/config.yml"
    content: |
      app_name: myapp
      version: 1.0.0
      environment: production
Роли
my_file_role

Роль для создания файлов с использованием my_own_module.


Параметры роли

Параметр	Тип	По умолчанию	Описание
my_file_path	str	/tmp/default_file.txt	Путь для создания файла
my_file_content	str	Многострочный текст	Содержимое файла
Пример использования роли

- hosts: localhost
  roles:
    - role: my_own_namespace.yandex_cloud_elk.my_file_role
      vars:
        my_file_path: "/tmp/custom.txt"
        my_file_content: "Custom content"
Playbook пример

---
- name: Deploy configuration files
  hosts: all
  tasks:
    - name: Create app config
      ansible.builtin.include_role:
        name: my_own_namespace.yandex_cloud_elk.my_file_role
      vars:
        my_file_path: "/etc/myapp/config.ini"
        my_file_content: |
          [DEFAULT]
          debug = false
          [database]
          host = localhost
Лицензия
GPL-3.0-or-later


Авторы
stomplego@gmail.com
