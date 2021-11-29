{% if cookiecutter.natural_language == 'ru' -%}
    {% set main_title = cookiecutter.project_name + '. Документация' -%}
    {% set contents_subtitle = 'Содержание' -%}
{% else -%}
    {% set main_title = cookiecutter.project_name + "'. Documentation" -%}
    {% set contents_subtitle = 'Contents' -%}
{% endif -%}

{%- for _ in main_title %}={% endfor %}
{{ main_title }}
{% for _ in main_title %}={% endfor %}
{{ cookiecutter.project_description }}

.. toctree::
  :maxdepth: 1
  :caption: {{ contents_subtitle }}


