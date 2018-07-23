# Ansible Role: {{ cookiecutter.ansible_org_role_slug }}

{{ cookiecutter.ansible_role_short_description }}

## Requirements

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

## Role Variables

The listed ariables are defined as defaults (see `defaults/main.yml`) or fixed variables (see `vars/main.yml`)
with the predefined values.

{%- set role_name = cookiecutter.ansible_role_slug %}
{% if cookiecutter.ansible_role_custom_repo == 'y' -%}
### Variables for tasks/repository

    {{ role_name }}_repository_gpgcheck: "yes"

The custom repository GPG check enabled/disabled.

    {{ role_name }}_repository_enabled: "no"

The custom repository enabled/disabled.
{% endif -%}

### Variables for tasks/package

    {{ role_name }}_package_name: "{{ role_name }}"

The package name to install.

    {{ role_name }}_package_state: "present"

The package install state. Defaults to present for idempotency, so no upgrades by default.

### Variables for tasks/config

    {{ role_name }}_config_dir: "{{ '{{ path_sysconfdir }}' }}/{{ role_name }}"

The service configuration directory. Defaults to /etc/{{ role_name }} on most Linux systems.

    {{ role_name }}_config_file: "{{ '{{' }} {{ role_name }}_config_dir {{ ' }}' }}/{{ role_name }}.conf"

The service main configuration file.

    {{ role_name }}_config_validate: "no"

Do configuration validation after config file changes.
You need to customize the validation cmd `tasks/config.yml`

### Variables for tasks/firewall

    {{ role_name }}_firewall_enabled: "yes"

Add firewall rules for the service.

### Variables for tasks/service and handlers/main

    {{ role_name }}_service_name: "{{ role_name }}"

The service name used for enable/disable/start/stop.

    {{ role_name }}_service_enabled: "yes"

The service activation state (enable/disable).

    {{ role_name }}_service_state: "started"

The service run state (started/stopped).

## Dependencies

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role: {{ cookiecutter.ansible_org_role_slug }}
           x: 42

## License

{{ cookiecutter.open_source_license }}

## Author Information

For authors/contributors please check AUTHORS.md.

## References

This ansible role was generated using [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
and the [wiredobjects Cookiecutter Ansible role template](https://github.com/wiredobjects/cookiecutter-ansible-role), a customized version of ansible-galaxy standard template.

* [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
* [wiredobjects/cookiecutter-ansible-role](https://github.com/wiredobjects/cookiecutter-ansible-role)
* [Ansible Documentation](https://docs.ansible.com/)
* [Ansible Documentation - Best Practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
