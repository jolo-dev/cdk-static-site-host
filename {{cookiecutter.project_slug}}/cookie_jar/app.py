#!/usr/bin/env python3

from aws_cdk import core

from cookie_jar.cookie_jar_stack import CookieJarStack


app = core.App()
CookieJarStack(app, "cookie-jar")

app.synth()
