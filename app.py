#!/usr/bin/env python3

from aws_cdk import core

from sweet_cookies.sweet_cookies_stack import SweetCookiesStack


app = core.App()
SweetCookiesStack(app, "sweet-cookies")

app.synth()
