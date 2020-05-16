#!/bin/bash
cd "sugar"
{% if cookiecutter.sugar == "React" %}
npx react-scripts build && mv build dist
{% endif %}
{% if cookiecutter.sugar == "Vue" %}
npx vue-cli-service build
{% endif %}
cd ".."

cd "cookie_jar"
source .env/bin/activate
pip install -r requirements.txt
npx cdk synth
npx cdk bootstrap
npx cdk deploy