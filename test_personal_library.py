#virtual envirornment
import json
import os
import tempfile
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch

from main.py import (
    load_library,
    save_library,
    add_book,
    remove_book,
    list_books,
    search_book,
    show_author_stats
)


def test_missing_file_starts_empty():
    folder = tempfile.TemporaryDirectory()
    filename = os.path.join(folder.name, "library.json")

    library = load_library(filename)

    assert library == {}
    folder.cleanup()


def test_wrong_json_shape_starts_empty():
    folder = tempfile.TemporaryDirectory()
    filename = os.path.join(folder.name, "library.json")

    with open(filename, "w") as file:
        json.dump(["Dune", "The Hobbit"], file)

    library = load_library(filename)

    assert library == {}
    folder.cleanup()


def test_save_and_load_library():
    folder = tempfile.TemporaryDirectory()
    filename = os.path.join(folder.name, "library.json")
    library = {
        "Dune": {
            "author": "Frank Herbert",
            "year": 1965
        }
    }

    save_library(library, filename)
    new_library = load_library(filename)

    assert new_library == library
    folder.cleanup()


def test_add_book():
    library = {}

    with patch("builtins.input", side_effect=["Dune", "Frank Herbert", "1965"]):
        add_book(library)

    assert library["Dune"]["author"] == "Frank Herbert"
    assert library["Dune"]["year"] == 1965


def test_duplicate_title_updates_book():
    library = {
        "Dune": {
            "author": "Frank Herbert",
            "year": 1965
        }
    }

    with patch("builtins.input", side_effect=["Dune", "Frank Herbert", "1966"]):
        add_book(library)

    assert len(library) == 1
    assert library["Dune"]["year"] == 1966


def test_remove_book():
    library = {
        "Dune": {
            "author": "Frank Herbert",
            "year": 1965
        }
    }

    with patch("builtins.input", return_value="Dune"):
        remove_book(library)

    assert "Dune" not in library


def test_list_books():
    library = {
        "Dune": {
            "author": "Frank Herbert",
            "year": 1965
        }
    }
    output = StringIO()

    with redirect_stdout(output):
        list_books(library)

    assert "1. Dune by Frank Herbert (1965)" in output.getvalue()


def test_search_book():
    library = {
        "The Hobbit": {
            "author": "J. R. R. Tolkien",
            "year": 1937
        },
        "Dune": {
            "author": "Frank Herbert",
            "year": 1965
        }
    }
    output = StringIO()

    with patch("builtins.input", return_value="hob"), redirect_stdout(output):
        search_book(library)

    assert "The Hobbit by J. R. R. Tolkien (1937)" in output.getvalue()


def test_search_with_no_matches():
    library = {
        "Dune": {
            "author": "Frank Herbert",
            "year": 1965
        }
    }
    output = StringIO()

    with patch("builtins.input", return_value="xyz"), redirect_stdout(output):
        search_book(library)

    assert "is not in your library" in output.getvalue()


def test_author_statistics():
    library = {
        "Dune": {
            "author": "Frank Herbert",
            "year": 1965
        },
        "Dune Messiah": {
            "author": "Frank Herbert",
            "year": 1969
        },
        "The Hobbit": {
            "author": "J. R. R. Tolkien",
            "year": 1937
        }
    }
    output = StringIO()

    with redirect_stdout(output):
        show_author_stats(library)

    assert "Frank Herbert: 2 book(s)" in output.getvalue()
    assert "J. R. R. Tolkien: 1 book(s)" in output.getvalue()


def run_tests():
    "Run each test and save the results in a log file"
    tests = [
        test_missing_file_starts_empty,
        test_wrong_json_shape_starts_empty,
        test_save_and_load_library,
        test_add_book,
        test_duplicate_title_updates_book,
        test_remove_book,
        test_list_books,
        test_search_book,
        test_search_with_no_matches,
        test_author_statistics
    ]

    log = open("test_run.log", "w")
    passed = 0

    for test in tests:
        try:
            output = StringIO()
            with redirect_stdout(output):
                test()

            print(test.__name__ + ": PASSED")
            log.write(test.__name__ + ": PASSED\n")
            log.write(output.getvalue())
            passed += 1
        except Exception as error:
            print(test.__name__ + ": FAILED")
            print(error)
            log.write(test.__name__ + ": FAILED\n")
            log.write(str(error) + "\n")

    log.write("\n" + str(passed) + " of " + str(len(tests)) + " tests passed.\n")
    log.close()
    print(str(passed) + " of " + str(len(tests)) + " tests passed.")


if __name__ == "__main__":
    run_tests()
