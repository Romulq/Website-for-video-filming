PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;


CREATE TABLE IF NOT EXISTS "film_site_aboutme" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "selfy" varchar(100) NULL, 
    "description" text NOT NULL, 
    "firstName" varchar(255) NOT NULL, 
    "lastName" varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS "film_site_videotype" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "name" varchar(255) NOT NULL, 
    "price" integer unsigned NOT NULL CHECK ("price" >= 0), 
    "slug" varchar(32) NOT NULL
);

CREATE TABLE IF NOT EXISTS "film_site_myworks" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "name" varchar(255) NOT NULL, 
    "videoType_id" bigint NOT NULL REFERENCES "film_site_videotype" ("id") DEFERRABLE INITIALLY DEFERRED, 
    "videoFile" varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS "film_site_order" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "firstName" varchar(255) NOT NULL, 
    "lastName" varchar(255) NOT NULL, 
    "eventDate" date NOT NULL, 
    "timeWork" integer unsigned NOT NULL CHECK ("timeWork" >= 0), 
    "suggestions" text NOT NULL, 
    "phone" varchar(12) NOT NULL, 
    "email" varchar(127) NOT NULL, 
    "created_at" datetime NOT NULL, 
    "typeVideo_id" bigint NOT NULL REFERENCES "film_site_videotype" ("id") DEFERRABLE INITIALLY DEFERRED, 
    "price" decimal NOT NULL
);

CREATE INDEX "film_site_videotype_slug_bdc45e87" ON "film_site_videotype" ("slug");
CREATE INDEX "film_site_myworks_videoType_id_9120681b" ON "film_site_myworks" ("videoType_id");
CREATE INDEX "film_site_order_typeVideo_id_a80d7338" ON "film_site_order" ("typeVideo_id");

COMMIT;
