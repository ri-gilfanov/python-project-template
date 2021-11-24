{% if cookiecutter.natural_language == 'ru' -%}
{% set html_title = cookiecutter.project_name + ". xxx" -%}
{{ html_title }}
{% for _ in html_title %}={% endfor %}
{{ cookiecutter.project_description }}

.. toctree::
  :maxdepth: 1
  :caption: Содержание


{% else -%}
{% set html_title = cookiecutter.project_name + "'s documentation" -%}
{{ html_title }}
{% for _ in html_title %}={% endfor %}
{{ cookiecutter.project_description }}

.. toctree::
  :maxdepth: 1
  :caption: Contents


{% endif -%}
