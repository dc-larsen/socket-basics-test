"""Deliberately vulnerable app for testing Socket Basics SAST scanning."""
import os
import sqlite3
import subprocess


def search_users(query):
    """SQL injection: user input concatenated into query."""
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = '" + query + "'")
    return cursor.fetchall()


def run_command(user_input):
    """Command injection: user input passed to shell."""
    subprocess.call(user_input, shell=True)


def eval_input(data):
    """Code injection: eval on user-controlled data."""
    return eval(data)


DB_PASSWORD = "super_secret_password_123"
API_KEY = "sk-live-abc123def456ghi789"
