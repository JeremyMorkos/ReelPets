DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS pets CASCADE;
DROP TABLE IF EXISTS user_hearts CASCADE;

CREATE TABLE users (
id SERIAL PRIMARY KEY,
user_name VARCHAR (254) NOT NULL,
password_hash TEXT NOT NULL,
image_url TEXT
);

CREATE TABLE pets (
  id SERIAL PRIMARY KEY,
  name VARCHAR(254) NOT NULL,
  type VARCHAR(254),
  image_url TEXT NOT NULL,
  favourite_food VARCHAR(254),
  user_id INT,
  CONSTRAINT fk_pets_users
    FOREIGN KEY(user_id)
    REFERENCES users(id)
);

CREATE TABLE user_hearts(
  id SERIAL PRIMARY KEY,

  user_id INT,
    CONSTRAINT fk_user_hearts_users
    FOREIGN KEY(user_id)
    REFERENCES users(id) ON DELETE CASCADE,

  pet_id INT,
    CONSTRAINT fk_user_hearts_pets
    FOREIGN KEY(pet_id)
    REFERENCES pets(id) ON DELETE CASCADE
);  

TRUNCATE TABLE users CASCADE;
TRUNCATE TABLE pets CASCADE;

ALTER SEQUENCE users_id_seq RESTART WITH 1;
ALTER SEQUENCE pets_id_seq RESTART WITH 1;
ALTER SEQUENCE user_hearts_id_seq RESTART WITH 1;

-- #password = hello
INSERT INTO users (user_name, password_hash, image_url) VALUES ('SeemySnakes', 'pbkdf2:sha256:260000$7JGWCmRiZ4ddVXr3$cd8e5412f9ebcff6b600fc95a38590f246046c72aaf9a1e4c4b9b64730e027c9','cloudinary://167789155165896:WhKSTGMc0tLFWw9CsnXbfQ-IrQ0@dwjdcepnm
');
-- #password = welcome
INSERT INTO users (user_name, password_hash, image_url) VALUES ('Frog delight', 'pbkdf2:sha256:260000$kK1OxClFjeKJv5XC$a84f692d5c1bf89879d8ee07cf55b564867ceb1b14dca16d8bad533c420eb76e','cloudinary://167789155165896:WhKSTGMc0tLFWw9CsnXbfQ-IrQ0@dwjdcepnm
');
-- #password = goodbye
INSERT INTO users (user_name, password_hash, image_url) VALUES ('CreepyCrawler', 'pbkdf2:sha256:260000$zKwnRQp4lJJebKVe$aa6a673c0e529710557b0f9ae5eac4cd07532c3bd3b01a3a39b39b35fa19056b','cloudinary://167789155165896:WhKSTGMc0tLFWw9CsnXbfQ-IrQ0@dwjdcepnm
');

INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Slitherer', 'Coral snake', 'https://a-z-animals.com/media/2022/04/Texas-Coral-Snake1.jpg', 'Apples', 1);
INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Scaley', 'Cobra', 'https://a-z-animals.com/media/2022/05/monocled-cobra-snake-on-white-picture-id1278579199.jpg', 'Mice', 1);
INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Slimeball', 'Leaf-Nosed snake', 'https://a-z-animals.com/media/2021/12/paradise-flying-snake.jpg', 'Slugs', 1);
INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Fred', 'Ring-Necked snake', 'https://a-z-animals.com/media/2022/02/shutterstock_687723445.jpg', 'Beans', 1);
INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Sally', 'Anaconda', 'https://a-z-animals.com/media/2022/02/shutterstock_1965532993.jpg', 'Plums', 1);
INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Snape', 'Australian copperhead snake', 'https://a-z-animals.com/media/2021/11/What-Does-a-Copperhead-Snake-Look-Like-header.jpg', 'Pumpkin Pie', 1);
INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Voldy', 'Hognose snake', 'https://a-z-animals.com/media/2022/04/Hognose-Snake-header.jpg', 'Ice Cream', 1);

INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Leafy', 'Tree frog', 'https://a-z-animals.com/media/2019/11/Tree-frog-Red-eyed-1024x535.jpg' , 'Crickets', 2);
INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Bully', 'American bullfrog', 'https://a-z-animals.com/media/2019/11/Bullfrog-on-leaf-1024x535.jpg' , 'Mealworms', 2);
INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Speedy', 'Northern leopard frog', 'https://a-z-animals.com/media/2021/02/Leopard-Frog-on-rock-1024x535.jpg', 'Locusts', 2);
INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Grumpy Guts', 'Poison dart frog', 'https://a-z-animals.com/media/2021/07/Incredible-Rainforest-Animals_-Poison-Dart-Frogs.jpg', 'Grasshoppers', 2);
INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Shiny', 'Golden poison frog', 'https://a-z-animals.com/media/2018/09/Poison-Dart-Frog-yellow.jpg', 'Caterpillars', 2);
INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Bill', 'Red-crowned toadlet', 'https://media.australian.museum/media/dd/images/Some_image.width-1200.75a457c.jpg', 'Blackworms', 2);
INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Zach', 'Pacman frog', 'https://a-z-animals.com/media/2022/02/shutterstock_410912479.jpg', 'Mice', 2);


INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Red', 'Redback spider', 'https://a-z-animals.com/media/2021/09/Redback-SPider-header.jpg', 'Crickets', 3);
INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Argghhh', 'Forked pirate spider', 'https://spiderbytes.org/wp-content/uploads/2015/10/Mimetidae_Florida.jpg', 'Mice', 3);
INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Mr Shy', 'Brown recluse spider', 'https://a-z-animals.com/media/2021/12/Most-Dangerous-Spiders-Brown-Recluse-Spider.jpg', 'Slugs', 3);
INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Mr Big', 'Goliath birdeater', 'https://a-z-animals.com/media/2021/10/goliath-tarantula-1.jpg',  'Beans', 3);
INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Wolfy', 'Rabid wolf spider', 'https://a-z-animals.com/media/2022/03/shutterstock_578630674.jpg', 'Plums', 3);
INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Moody', 'Coastal peacock spider', 'https://a-z-animals.com/media/2021/10/Peacock-spider-header.jpg', 'Pumpkin Pie', 3);
INSERT INTO pets (name, type, image_url, favourite_food,  user_id) VALUES ('Fuzz Ball', 'Giant huntsman spider', 'https://a-z-animals.com/media/2021/07/Huntsman-Spider-in-the-Rainforest-1024x535.jpg', 'Ice Cream', 3);



