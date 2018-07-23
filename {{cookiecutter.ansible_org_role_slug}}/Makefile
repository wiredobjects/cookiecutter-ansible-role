.PHONY: virtualenv galaxy test clean

PLATFORM                   := $(shell uname -s | tr '[:upper:]' '[:lower:]')
ARCHITECTURE               := $(shell uname -m | sed -e 's/x86_64/amd64/')
PROJECT_DIR                 = $(PWD)
VENV_ACTIVATE               = source virtualenv/bin/activate
ANSIBLE_ROLE_NAME           = {{ cookiecutter.ansible_org_role_slug }}
ANSIBLE_DIR_ROLES_INTERNAL  = tests/roles/internal
ANSIBLE_DIR_ROLES_EXTERNAL  = tests/roles/external
ANSIBLE_GALAXY_ENABLE      ?= no
ANSIBLE_GALAXY_REQUIREMENTS = tests/roles/requirements.yml
ANSIBLE_INVENTORY_FILE      = tests/inventory
ANSIBLE_ENV_ARGS            = ANSIBLE_CONFIG=tests/ansible.cfg
ANSIBLE_PLAYBOOK_CMD        = $(ANSIBLE_ENV_ARGS) ansible-playbook -i $(ANSIBLE_INVENTORY_FILE) -e "project_dir=$(PWD)"
DOCKER_COMPOSE              = docker-compose -p $(ANSIBLE_ROLE_NAME) -f tests/docker-compose.yml


virtualenv: virtualenv/.built
galaxy: $(ANSIBLE_DIR_ROLES_INTERNAL)/.built $(ANSIBLE_DIR_ROLES_EXTERNAL)/.built
test-docker-prepare: tests/docker-centos7.build

help:
	@echo 'Usage:'
	@echo '    make virtualenv      Prepare the virtualenv environment'
	@echo '    make galaxy          Download external roles from galaxy or custom sources'
	@echo '    make test            Ansible playbooks tests'
	@echo '    make clean           Remove virtualenv environment and external galaxy roles'
	@echo '    make all             Run: virtualenv galaxy test run'
	@echo

all: virtualenv galaxy test

virtualenv/.built: requirements.txt
	rm -rf virtualenv
	virtualenv virtualenv
	$(VENV_ACTIVATE) && pip install -r requirements.txt
	touch $@

$(ANSIBLE_DIR_ROLES_INTERNAL)/.built: virtualenv
	ln -sf $(PROJECT_DIR) tests/roles/internal/$(ANSIBLE_ROLE_NAME)
	touch $@

$(ANSIBLE_DIR_ROLES_EXTERNAL)/.built: virtualenv $(ANSIBLE_GALAXY_REQUIREMENTS)
	#$(VENV_ACTIVATE) && ansible-galaxy install -r $(ANSIBLE_GALAXY_REQUIREMENTS) -p $(ANSIBLE_DIR_ROLES_EXTERNAL)
	touch $@

test: galaxy
	$(VENV_ACTIVATE) && $(ANSIBLE_PLAYBOOK_CMD) --syntax-check tests/test.yml
	$(VENV_ACTIVATE) && ansible-lint tests/test.yml

tests/docker-centos7.build:
	$(DOCKER_COMPOSE) up -d centos7
	$(DOCKER_COMPOSE) exec centos7 /bin/sh tests/prepare.sh
	touch $@

test-docker-run: test-docker-prepare
	$(DOCKER_COMPOSE) exec centos7 $(ANSIBLE_PLAYBOOK_CMD) tests/test.yml

clean-docker:
	$(DOCKER_COMPOSE) down -v

clean:
	rm -rf virtualenv
	rm -rf $(ANSIBLE_DIR_ROLES_EXTERNAL)/*
	rm -rf $(ANSIBLE_DIR_ROLES_INTERNAL)/*
	rm -rf site.retry
