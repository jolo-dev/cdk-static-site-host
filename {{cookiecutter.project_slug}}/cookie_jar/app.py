#!/usr/bin/env python3

from aws_cdk import core
from cookie_jar_stack import CookieJarStack
from chock_stack import ChocoStack

app = core.App()
CookieJarStack(app, "chocolate-chips")
ChocoStack(app, "cookie-jar")

app.synth()
