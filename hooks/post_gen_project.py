import os

icing = "{{ cookiecutter.icing }}"

if icing == "React":
    os.system("npx create-react-app icing --template typescript")
elif icing == "Vue":
    os.system("npx @vue/cli create icing")

os.system("npm audit fix")
# Remove Git
os.system("rm ./icing.git ./icing.gitignore")
