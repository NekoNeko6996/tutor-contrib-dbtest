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

# Chèn service vào compose cho DEV và LOCAL
hooks.Filters.ENV_PATCHES.add_item(
    ("local-docker-compose-dev-services", DBTEST_SERVICE)
)
hooks.Filters.ENV_PATCHES.add_item(
    ("local-docker-compose-services", DBTEST_SERVICE)
)
