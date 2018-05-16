# -*- coding: utf-8 -*-
"""
    {{NAMEPROJECT}}.{{MODNAME}}.forms
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    {{NAME}} {{MODNAME}} forms module

    :copyright: (c) {{YEAR}} by {{AUTHOR}}.
    :license: BSD, see LICENSE for more details.
"""

from flask_mongoengine.wtf import model_form
from flask_wtf import Form
from wtforms import SubmitField, StringField

# Get Model 
from {{NAMEPROJECT}}.{{MODNAME}}.models import {{MODNAME | capitalize}}

class {{MODNAME}}Form(Form):
    nome = StringField("Nome")
    submit = SubmitField("Adicionar")
