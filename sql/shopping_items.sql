-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: shopping
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `items` (
  `name` varchar(255) DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `item_no` int DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES ('Yonex Gr 300',500,1,'Sports'),('Sandisk OTG 32Gb',649,2,'Electronics'),('Sandisk Pendrive 32Gb',499,3,'Electronics'),('Sandisk Pendrive 64Gb',749,4,'Electronics'),('Sandisk Pendrive 128Gb',1249,5,'Electronics'),('Apple iphone 12 Pro Max',100649,6,'Smartphone'),('Apple iphone 11 Pro',90649,7,'Smartphone'),('Apple iphone 11',70649,8,'Smartphone'),('Pixel',32999,9,'Smartphone'),('Pixel Xl',36999,10,'Smartphone'),('Pixel 2',39999,11,'Smartphone'),('Pixel 3',44999,12,'Smartphone'),('Pixel 4',52999,13,'Smartphone'),('Pixel 5',57999,14,'Smartphone'),('Pixel 4a',31999,15,'Smartphone'),('Pixel 4a 5G',42999,16,'Smartphone'),('Monopoly',599,17,'Boardgame'),('Monopoly ELectronic Bank Edition',1599,18,'Boardgame'),('Nivia Storm Football',399,19,'Sports'),('Cosco Tennis Ball x6',199,20,'Sports'),('Cosco Tennis Bat',499,21,'Sports'),('Nike EPL Football',2399,68,'Sports'),('Addidas Worldcup Football',1799,22,'Sports'),('Stag International Carrom Board',5399,23,'Boardgame'),('Hero Gear Cycle',19399,24,'Sports'),('Mask 100x',299,25,'Medical'),('Mask 200x',599,26,'Medical'),('Mask N95 10x',199,27,'Medical'),('Covid Vacine',2299,28,'Medical'),('Vico Pain Balm',199,29,'Medical'),('3-Burner Gas Stove',2299,30,'Kitchen'),('2-Burner Gas Stove',1699,31,'Kitchen'),('1-Burner Gas Stove',999,32,'Kitchen'),('Pigeon Induction 1200Watt',3299,33,'Kitchen'),('Cello Lunch Box',299,67,'Kitchen'),('Tupperware Lunch Box',499,34,'Kitchen'),('Tupperware WaterBottle',199,35,'Kitchen'),('LG Mircowave',12999,36,'Kitchen'),('Samsung 55 inch TV',47299,37,'Television'),('Samsung 55 inch UHD TV',87299,38,'Television'),('Samsung 65 inch UHD TV',127299,39,'Television'),('Samsung 65 inch 8k TV',147299,40,'Television'),('LG 55 inch TV',47299,41,'Television'),('LG 55 4k inch TV',66299,42,'Television'),('Cello Pressure Cooker 5L',1299,43,'Kitchen'),('Cello Tape',19,44,'Stationary'),('Fevicol 200ml',20,45,'Stationary'),('Fevistick',10,46,'Stationary'),('Natraj Pencil 10x',20,47,'Stationary'),('Cello Pen',5,48,'Stationary'),('Parker Gold',119,49,'Stationary'),('Dairy 2020',59,50,'Stationary'),('Pastel Crayons',79,51,'Stationary'),('Pastel Combo Pack 100Crayons',1119,52,'Stationary'),('Pastel PaintBrush x3',29,53,'Stationary'),('Google Home Next gen',6919,54,'Assitant'),('Cello Electronic Tape',19,55,'Stationary'),('Google Home Mini Next gen',2999,56,'Assitant'),('Google Home',4999,57,'Assitant'),('Google Home mini',2999,58,'Assitant'),('Echo Dot 1st gen',2519,59,'Assitant'),('Echo Dot 2nd gen',2919,60,'Assitant'),('Echo Dot 3rd gen',3519,61,'Assitant'),('Echo Dot 4th gen',4519,62,'Assitant'),('Echo Dot Mini 1st gen',1519,63,'Assitant'),('Echo Dot Mini 2nt gen',1719,64,'Assitant'),('Echo Dot Mini 3rd gen',2019,65,'Assitant'),('Echo Dot Mini 4th gen',2319,66,'Assitant');
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-26  3:48:40
