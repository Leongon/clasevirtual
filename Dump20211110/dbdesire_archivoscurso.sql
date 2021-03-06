-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: dbdesire
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.14-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `archivoscurso`
--

DROP TABLE IF EXISTS `archivoscurso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `archivoscurso` (
  `idarchivoscurso` int(11) NOT NULL AUTO_INCREMENT,
  `urlpdf` varchar(45) NOT NULL,
  `fkmodulocurso` int(11) NOT NULL,
  PRIMARY KEY (`idarchivoscurso`),
  KEY `fk_archivoscurso_modulocurso1_idx` (`fkmodulocurso`),
  CONSTRAINT `fk_archivoscurso_modulocurso1` FOREIGN KEY (`fkmodulocurso`) REFERENCES `modulocurso` (`idmodulocurso`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `archivoscurso`
--

LOCK TABLES `archivoscurso` WRITE;
/*!40000 ALTER TABLE `archivoscurso` DISABLE KEYS */;
INSERT INTO `archivoscurso` VALUES (1,'Este es un pdf para el modulo mariposa 1',1),(2,'Este es un pdf para el modulo mariposa 2',1),(3,'Este es un pdf para el modulo mariposa 3',1),(4,'Este es un pdf para el modulo camisa 1',2),(5,'Este es un pdf para el modulo camisa 2',2),(6,'Este es un pdf para el modulo camisa 3',2),(11,'Este es un pdf para el modulo la cucaracha 1',3),(12,'Este es un pdf para el modulo la cucaracha 2',3),(13,'Este es un pdf para el modulo la cucaracha 3',3),(14,'Este es un pdf para el modulo la cucaracha 4',3);
/*!40000 ALTER TABLE `archivoscurso` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-10 19:03:04
