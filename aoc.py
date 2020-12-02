import requests
import datetime
import pyperclip
from os import path, environ, mkdir
from dotenv import load_dotenv

load_dotenv()


def download_input(day=datetime.datetime.today().day):
    session = environ['AOC_SESSION']
    text = requests.get(f"https://adventofcode.com/2020/day/{day}/input",
                        cookies={"session": session}).text

    folder = "caches/"
    if not path.exists(folder):
        mkdir(folder)

    cache_path = f"caches/input-{day}.txt"
    with open(cache_path, "w+") as file:
        file.write(text)

    return text


def load_input(day=datetime.datetime.today().day):
    if not path.exists("caches/"):
        return download_input(day)

    cache_path = f"caches/input-{day}.txt"
    if path.exists(cache_path):
        return open(cache_path).read()

    return download_input(day)


def parse_input(day=datetime.datetime.today().day):
    return [s.strip() for s in load_input(day).splitlines()]


def copy_answer(answer):
    pyperclip.copy(str(answer))
