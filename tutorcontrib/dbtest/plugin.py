from pathlib import Path
from tutor import hooks

DBTEST_SERVICE = r"""
dbtest:
  image: mysql:8.0
  command: ["sh", "-lc", "sleep infinity"]
  environment:
    DB_HOST: "{{ MYSQL_HOST }}"
    DB_PORT: "{{ MYSQL_PORT }}"
    DB_USER: "{{ OPENEDX_MYSQL_USERNAME }}"
    DB_PASS: "{{ OPENEDX_MYSQL_PASSWORD }}"
    DB_NAME: "{{ OPENEDX_MYSQL_DATABASE }}"
  depends_on:
    - mysql
  networks:
    - default
"""

# if you ship template files:
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(Path(__file__).parent / "templates")

# ✅ add the dbtest service to both dev & local compose files
hooks.Filters.ENV_PATCHES.add_item(("dev-docker-compose-services", DBTEST_SERVICE))
hooks.Filters.ENV_PATCHES.add_item(("local-docker-compose-services", DBTEST_SERVICE))

# (optional) prove plugin loads by annotating caddy config
hooks.Filters.ENV_PATCHES.add_item(("caddyfile-global", "# dbtest plugin loaded\n"))
