import os
import json

sugar = "{{ cookiecutter.sugar }}"
tailwind = "{{ cookiecutter.tailwind }}"
rest = "{{ cookiecutter.rest_client }}"

if sugar == "React":
    os.system("npx create-react-app sugar --template typescript --use-npm")

elif sugar == "Vue":
    os.system("npx @vue/cli create sugar --default")

os.chdir("sugar")

if tailwind == "y":
    os.system("npm install tailwind")

if rest == "axios":
    os.system("npm install axios")

os.system("npm audit fix")
# Remove Git
os.system("rm -rf ./.git ./.gitignore")

with open("package.json") as f:
    package_json = json.load(f)

package_json["name"] = "{{ cookiecutter.project_slug }}"
package_json["author"] = "{{ cookiecutter.author }}"
package_json["description"] = "{{ cookiecutter.description }}"

with open('package.json', "w") as package_file:
    json.dump(package_json, package_file, indent=4)
