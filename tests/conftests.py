import json
from flask import Flask, request, jsonify
import pytest
from flask import create_app

@pytest.fixture()
def app():
  app = create_app


@pytest.fixture()
def client():
  return app.test_client()