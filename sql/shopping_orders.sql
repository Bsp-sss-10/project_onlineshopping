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
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_no` int DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `item` varchar(255) DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `pay_method` varchar(255) DEFAULT NULL,
  `qty` int DEFAULT NULL,
  `total` int DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (34466,'2020-12-25','Yonex Gr 300',500,'ishaan.singh15@yahoo.in','UPI',3,1500,NULL),(51599,'2020-12-25','Yonex Gr 300',500,'ishaan.singh15@yahoo.in','Cash on Delivery',5555,2777500,NULL),(29375,'2020-12-25','Yonex Gr 300',500,'shivan@gmail.com','Cash on Delivery',4,2000,NULL),(72872,'2020-12-25','Yonex Gr 300',500,'shivan@gmail.com','Debit Card / Credit Card',55,27500,NULL),(55632,'2020-12-25','Yonex Gr 300',500,'ishaan@singh15@yahoo.in','Debit Card / Credit Card',77,38500,NULL),(32385,'2020-12-25','Yonex Gr 300',500,'kumudsingh05@gmail.com','Cash on Delivery',1,500,NULL),(22849,'2020-12-26','Pixel 3',44999,'shivan@gmail.com','Cash on Delivery',1,44999,NULL),(34947,'2020-12-26','Google Home',4999,'shivan@gmail.com','UPI',5,24995,NULL),(23559,'2020-12-26','Cello Pen',5,'shivan@gmail.com','Cash on Delivery',55,275,NULL),(10499,'2020-12-26','Dairy 2020',59,'shivan999999@gmail','Cash on Delivery',111,6549,NULL),(77848,'2021-1-6','Yonex Gr 300',500,'shivan@gmail.com','Cash on Delivery',4,2000,NULL),(85119,'2021-1-6','Sandisk Pendrive 64Gb',749,'1@2','Cash on Delivery',3,2247,NULL),(85119,'2021-1-6','Sandisk Pendrive 32Gb',499,'1@2','Cash on Delivery',5,3245,NULL),(85119,'2021-1-6','Sandisk OTG 32Gb',649,'1@2','Cash on Delivery',4,2596,NULL),(91807,'2021-1-6','Yonex Gr 300',500,'1@2','Cash on Delivery',3,1500,NULL),(91807,'2021-1-6','Sandisk Pendrive 64Gb',749,'1@2','Cash on Delivery',55,41195,NULL),(53721,'2021-1-7','Yonex Gr 300',500,'shivan@gmail.com','Debit Card / Credit Card',0,0,NULL),(78442,'2021-1-8','Pixel 4a 5G',42999,'shivan@gmail.com','UPI',2,85998,NULL),(19414,'2021-1-8','Cello Pen',5,'ravnishsingh68@gmail.com','Debit Card / Credit Card',5,25,NULL),(51643,'2021-1-8','Nivia Storm Football',399,'shivanii@1','Cash on Delivery',44,17556,NULL),(57444,'2021-1-8','Samsung 65 inch 8k TV',147299,'ravnishsingh68@gmail.com','UPI',-55,-68695,NULL),(57444,'2021-1-8','Google Home',4999,'ravnishsingh68@gmail.com','UPI',2,9998,NULL),(57444,'2021-1-8','Cello Tape',19,'ravnishsingh68@gmail.com','UPI',5,95,NULL),(57444,'2021-1-8','Stag International Carrom Board',5399,'ravnishsingh68@gmail.com','UPI',1,5399,NULL),(57444,'2021-1-8','Pixel 4',52999,'ravnishsingh68@gmail.com','UPI',2,105998,NULL),(57444,'2021-1-8','Covid Vacine',2299,'ravnishsingh68@gmail.com','UPI',5,11495,NULL),(57444,'2021-1-8','Mask N95 10x',199,'ravnishsingh68@gmail.com','UPI',1,199,NULL),(57444,'2021-1-8','Sandisk Pendrive 128Gb',1249,'ravnishsingh68@gmail.com','UPI',5,6245,NULL),(28882,'2021-1-31','Pixel 4',52999,'shivan@gmail.com','Cash on Delivery',2,105998,'A-23, Chpl chouhan Dream homes,  smriti nagar,bhilai,Chhattisgarh(490020)');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-31 12:45:06
