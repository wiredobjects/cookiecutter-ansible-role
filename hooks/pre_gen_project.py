import re
import sys

def sys_exit(msg):
    print(msg)
    sys.exit(1)

REGEX_ANSIBLE_ROLE_SLUG = r'^[_a-zA-Z][-_a-zA-Z0-9]+$'
REGEX_EMAIL = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'

author_name = '{{ cookiecutter.author_name }}'
email = '{{ cookiecutter.email }}'
ansible_role_slug = '{{ cookiecutter.ansible_role_slug }}'

if author_name == '':
    sys_exit('[ERROR] No value for author name provided: %s - Please provide at least an alias name' % author_name)

if not re.match(REGEX_EMAIL, email):
    sys_exit('[ERROR] No valid email provided: %s' % email)

if not re.match(REGEX_ANSIBLE_ROLE_SLUG, ansible_role_slug):
    sys_exit('[ERROR] Ansible role slug (%s) is not a valid.' % project_slug)

