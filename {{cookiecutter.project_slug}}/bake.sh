#!/bin/bash
cd "dough"
{% if cookiecutter.dough == "React" %}
npx react-scripts build && mv build dist
{% endif %}
{% if cookiecutter.dough == "Vue" %}
npx vue-cli-service build
{% endif %}
cd ".."

{% if cookiecutter.chocolate_chips == "Flask" %}
mv chocolate_chips/flask_choco.py chocolate_chips/flask/flask_choco.py
{% endif %}

cd "cookie_jar"
# npx cdk synth chocolate-chips
# npx cdk synth cookie-jar
npx cdk deploy chocolate-chips
npx cdk deploy cookie-jar