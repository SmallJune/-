CREATE TABLE `og_article_type` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `article_type` varchar(32)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
CREATE TABLE `og_article` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `article_type_id` integer NOT NULL,
    `sub_type` varchar(32),
    `title` varchar(64) NOT NULL,
    `content` longtext NOT NULL
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
ALTER TABLE `og_article` ADD CONSTRAINT `article_type_id_refs_id_d819d1ca` FOREIGN KEY (`article_type_id`) REFERENCES `og_article_type` (`id`);

CREATE TABLE `og_article_attachment` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `attachment_type` varchar(2) NOT NULL,
    `image` varchar(100),
    `article_id` integer NOT NULL,
    `place` integer NOT NULL
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
ALTER TABLE `og_article_attachment` ADD CONSTRAINT `article_id_refs_id_b41095a4` FOREIGN KEY (`article_id`) REFERENCES `og_article` (`id`);

CREATE INDEX `og_article_5a73e2b2` ON `og_article` (`article_type_id`);
CREATE INDEX `og_article_attachment_e669cc35` ON `og_article_attachment` (`article_id`);


CREATE TABLE `og_company` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `company` varchar(64) NOT NULL,
    `address` varchar(64)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
CREATE TABLE `og_jobs` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `jobs_type` integer NOT NULL,
    `jobs` varchar(64) NOT NULL,
    `number` integer NOT NULL,
    `gender` varchar(1) NOT NULL,
    `education` varchar(32) NOT NULL,
    `workplace` varchar(32) NOT NULL,
    `major` varchar(32) NOT NULL,
    `description` longtext NOT NULL,
    `demand` longtext NOT NULL,
    `company_id` integer NOT NULL
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
ALTER TABLE `og_jobs` ADD CONSTRAINT `company_id_refs_id_e0e2c6de` FOREIGN KEY (`company_id`) REFERENCES `og_company` (`id`);
CREATE INDEX `og_jobs_0316dde1` ON `og_jobs` (`company_id`);
--  2015-1-15  --
ALTER TABLE `og_article`
ADD COLUMN `article_templates` varchar(20) NOT NULL AFTER `sub_type`;

--  2015-1-15  --
CREATE TABLE `og_download_file` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `file_type` integer NOT NULL,
    `file_name` varchar(200) NOT NULL,
    `url` varchar(200) NOT NULL
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


Alter table og_article CHANGE content content longtext;