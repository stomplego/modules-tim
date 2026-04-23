#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module
short_description: Create a text file on remote host
version_added: "1.0.0"
description:
    - This module creates a text file on the remote host with specified content.
    - If the file already exists, it will be overwritten.
options:
    path:
        description:
            - The absolute path to the file to create on the remote host.
        required: true
        type: str
    content:
        description:
            - The content to write to the file.
        required: true
        type: str
author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
- name: Create a file with content
  my_namespace.my_own_collection.my_own_module:
    path: /tmp/example.txt
    content: "Hello, Ansible!"
'''

RETURN = r'''
path:
    description: The path to the file that was created.
    type: str
    returned: success
    sample: "/tmp/example.txt"
content:
    description: The content that was written to the file.
    type: str
    returned: success
    sample: "Hello, Ansible!"
changed:
    description: Whether the file was created or changed.
    type: bool
    returned: always
    sample: true
'''

from ansible.module_utils.basic import AnsibleModule
import os

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        content=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']
    result['path'] = path
    result['content'] = content

    # Check if file exists and read its content
    file_exists = os.path.exists(path)
    existing_content = None
    
    if file_exists:
        try:
            with open(path, 'r') as f:
                existing_content = f.read()
        except Exception as e:
            module.fail_json(msg="Failed to read existing file: %s" % str(e), **result)

    # Determine if change is needed
    if file_exists and existing_content == content:
        result['changed'] = False
        module.exit_json(**result)
    else:
        result['changed'] = True

    # In check mode, don't make changes
    if module.check_mode:
        module.exit_json(**result)

    # Create directory if it doesn't exist
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        try:
            os.makedirs(directory, mode=0o755)
        except Exception as e:
            module.fail_json(msg="Failed to create directory %s: %s" % (directory, str(e)), **result)

    # Write content to file
    try:
        with open(path, 'w') as f:
            f.write(content)
    except Exception as e:
        module.fail_json(msg="Failed to write to file %s: %s" % (path, str(e)), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
