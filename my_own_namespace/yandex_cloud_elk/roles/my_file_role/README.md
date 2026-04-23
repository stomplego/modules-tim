# my_file_role

This role creates a text file using the custom `my_own_module` module.

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `my_file_path` | `/tmp/default_file.txt` | Path where the file will be created |
| `my_file_content` | Multi-line string | Content to write to the file |

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: my_file_role
      vars:
        my_file_path: "/tmp/custom_file.txt"
        my_file_content: "Custom content here"
License
GPL-3.0-or-later
