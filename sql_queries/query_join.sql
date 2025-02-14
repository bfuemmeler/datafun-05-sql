-- Join the tables to select all authors, and the release dates of their books
SELECT authors.author_id, books.year_published
FROM authors
LEFT JOIN books ON authors.author_id = books.author_id
ORDER BY books.year_published DESC;