import xml.etree.ElementTree as ET
data = '''<library>
    <book id="1">
        <title>Don Quijote de la Mancha</title>
        <author>Miguel de Cervantes</author>
        <year>1605</year>
        <genre>Novela</genre>
        <available>true</available>
    </book>
    <book id="2">
        <title>Cien años de soledad</title>
        <author>Gabriel García Márquez</author>
        <year>1967</year>
        <genre>Realismo mágico</genre>
        <available>false</available>
    </book>
    <book id="3">
        <title>La Casa de los Espíritus</title>
        <author>Isabel Allende</author>
        <year>1982</year>
        <genre>Novela</genre>
        <available>true</available>
    </book>
</library>'''
tree = ET.fromstring(data)
books = tree.findall('book')
print(f"Quantity of books in inventory: {len(books)}")
for item in books:
    book_id = item.get('id')
    print("------------------------------------")
    print("")
    print(f"The book ID is: {book_id}")
    title = item.find('title').text
    print(f"Title: {title}")
    author = item.find('author').text
    print(f"Author: {author}")
    
    


