#!/usr/bin/python
#-*- coding: utf-8 -*-

import argparse
import subprocess
from flask import Flask, jsonify, request
from flask import render_template

app = Flask(__name__)

@app.route(
