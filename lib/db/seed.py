from lib.models.author import Author
from lib.models.magazine import Magazine

a1 = Author.create("Alice")
a2 = Author.create("Bob")

m1 = Magazine.create("Tech Times", "Technology")
m2 = Magazine.create("Nature World", "Science")

a1.add_article(m1, "AI in 2025")
a1.add_article(m2, "The Ocean's Secret")
a2.add_article(m1, "Quantum Computing")
