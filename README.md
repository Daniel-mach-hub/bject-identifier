# Object Relations Code Challenge

# Object Relations Code Challenge

A simple ORM-style implementation using Python and SQLite to manage the relationships between Authors, Articles, and Magazines.

## 📘 Overview

This project models the following relationships:

- An `Author` can write many `Articles`
- A `Magazine` can publish many `Articles`
- An `Article` belongs to both an `Author` and a `Magazine`
- This forms a many-to-many relationship between Authors and Magazines through Articles

## 🏗️ Project Structure

```
code-challenge/
├── lib/
│   ├── models/
│   │   ├── author.py
│   │   ├── article.py
│   │   └── magazine.py
│   ├── db/
│   │   ├── connection.py
│   │   ├── schema.sql
│   │   └── seed.py
├── scripts/
│   └── setup_db.py
├── tests/
│   ├── __init__.py
│   └── test_author.py
├── .gitignore
└── README.md
```

## ⚙️ Setup Instructions

### Using `venv`

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install pytest
```

### Initialize Database

```bash
python scripts/setup_db.py
```

This creates the SQLite database and runs the schema file.

### Seed Data (Optional)

```bash
python lib/db/seed.py
```

Populates the database with sample authors, magazines, and articles.

## 🧪 Running Tests

```bash
pytest
```

## 🧩 Key Classes and Methods

### Author

- `Author.create(name)`
- `Author.find_by_id(id)`
- `author.articles()`
- `author.magazines()`
- `author.add_article(magazine, title)`
- `author.topic_areas()`

### Magazine

- `Magazine.create(name, category)`
- `magazine.articles()`
- `magazine.contributors()`
- `magazine.article_titles()`
- `magazine.contributing_authors()`

### Article

- `Article.create(title, author_id, magazine_id)`
- `Article.find_by_id(id)`

## 🧵 Example Usage

```python
from lib.models.author import Author
from lib.models.magazine import Magazine

author = Author.create("Jane Doe")
magazine = Magazine.create("Tech Weekly", "Technology")
author.add_article(magazine, "The Future of AI")
```

## 🗂 .gitignore

```
.env
env/
__pycache__/
*.pyc
*.db
```

## ✅ Commit Guidelines

- Small, logical commits
- Descriptive messages, e.g.:
  - `Feature: Implement Author relationships`
  - `Fix: Correct magazine contributor query`

## 🔥 Bonus Features (Optional)

- `Magazine.top_publisher()`
- Author with most articles
- Add command-line interface (CLI)

