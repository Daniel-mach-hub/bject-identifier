from lib.models.author import Author

def test_author_creation():
    author = Author.create("Test Author")
    assert author.name == "Test Author"
