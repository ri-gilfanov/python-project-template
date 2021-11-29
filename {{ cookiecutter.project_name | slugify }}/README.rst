{% for _ in cookiecutter.project_name %}={% endfor %}
{{cookiecutter.project_name}}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_description }}

{% if cookiecutter.natural_language == 'ru' -%}
{% set docs_subtitle = 'Документация' -%}
{% else -%}
{% set docs_subtitle = 'Documentation' -%}
{% endif -%}

{% for _ in docs_subtitle %}={% endfor %}
{{ docs_subtitle }}
{% for _ in docs_subtitle %}={% endfor %}
{{ cookiecutter.documentation_url }}
