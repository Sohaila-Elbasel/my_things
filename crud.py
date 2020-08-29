from models import *
from app import db

def add_categories():
    objects = [
        Category(name = 'classics'),
        Category(name = 'comic'),
        Category(name = 'mystery'),
        Category(name = 'fantasy'),
        Category(name = 'historical'),
        Category(name = 'horror'),
        Category(name = 'fiction'),
        Category(name = 'romance'),
        Category(name = 'sci-fi'),
    ]

    for object in objects:
        category = object
        db.session.add(category)
        db.session.commit()

    print(Category.query.all())

def add_book():
    # book = Book(category_id = 2, name='To Kill a Mockingbird', price=9.99, rate=4.8, weight = 9.0, author = 'Harper Lee', summary = "Harper Lee's Pulitzer prize-winning masterwork of honor and injustice in the deep south—and the heroism of one man in the face of blind and violent hatred One of the best-loved stories of all time, To Kill a Mockingbird has been translated into more than forty languages, sold more than forty million copies worldwide, served as the basis for an enormously popular motion picture, and was voted one of the best novels of the twentieth century by librarians across the country. A gripping, heart-wrenching, and wholly remarkable tale of coming-of-age in a South poisoned by virulent prejudice, it views a world of great beauty and savage inequities through the eyes of a young girl, as her father—a crusading local lawyer—risks everything to defend a black man unjustly accused of a terrible crime.", about_author = "Harper Lee was born in 1926 in Monroeville, Alabama. She is the author of the acclaimed To Kill a Mockingbird and Go Set a Watchman, which became a phenomenal #1 New York Times bestseller when it was published in July 2015. Ms. Lee received the Pulitzer Prize, the Presidential Medal of Freedom, and numerous other literary awards and honors. She died on February 19, 2016.", height = 7.9, width = 5.3, depth = 0.9, pages = '336', publisher = 'Harper Perennial', language = 'English', condition = 'new', photo_url = 'https://upload.wikimedia.org/wikipedia/commons/4/4f/To_Kill_a_Mockingbird_%28first_edition_cover%29.jpg')

    book = Book(category_id = 1, name='Life of Pi', price=9.99, rate=4.4, weight = 9.6, author = 'Yann Martel ', summary = "The son of a zookeeper, Pi Patel has an encyclopedic knowledge of animal behavior and a fervent love of stories. When Pi is sixteen, his family emigrates from India to North America aboard a Japanese cargo ship, along with their zoo animals bound for new homes.The ship sinks. Pi finds himself alone in a lifeboat, his only companions a hyena, an orangutan, a wounded zebra, and Richard Parker, a 450-pound Bengal tiger. Soon the tiger has dispatched all but Pi, whose fear, knowledge, and cunning allow him to coexist with Richard Parker for 227 days while lost at sea. When they finally reach the coast of Mexico, Richard Parker flees to the jungle, never to be seen again. The Japanese authorities who interrogate Pi refuse to believe his story and press him to tell them \"the truth.\" After hours of coercion, Pi tells a second story, a story much less fantastical, much more conventional--but is it more true?", about_author = "Yann Martel, the son of diplomats, was born in Spain in 1963. He grew up in Costa Rica, France, Mexico, Alaska, and Canada and as an adult has spent time in Iran, Turkey, and India. After studying philosophy in college, he worked at various odd jobs until he began earning his living as a writer at the age of twenty-seven. He lives in Montreal.", height = 8.0, width = 5.0, depth = 0.91, pages = '326', publisher = ' Mariner Books', language = 'English', condition = 'new', photo_url = 'https://images-na.ssl-images-amazon.com/images/I/51rxEvLljUL._SX322_BO1,204,203,200_.jpg')

    db.session.add(book)
    db.session.commit()
    print('ok')



print(Book.query.all())
