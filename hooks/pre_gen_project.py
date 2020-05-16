project_slug = "{{ cookiecutter.project_slug }}"

assert (
    project_slug == project_slug.lower()
), f"{project_slug} project slug should be all lowercase"