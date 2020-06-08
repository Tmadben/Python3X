/* DATABASE CREATION */

DROP DATABASE IF EXISTS parcauto_db;

CREATE DATABASE parcauto_db;

USE parcauto_db;




--
-- Table structure for table `tbl_tarifs`
--

DROP TABLE IF EXISTS `tbl_tarifs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_tarifs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom_tarif` varchar(45) NOT NULL,
  `prix_unitaire` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_tarifs`
--
-- ORDER BY:  `id`

LOCK TABLES `tbl_tarifs` WRITE;
/*!40000 ALTER TABLE `tbl_tarifs` DISABLE KEYS */;
INSERT INTO `tbl_tarifs` (`id`, `nom_tarif`, `prix_unitaire`) VALUES (1,'Tourisme',500),(2,'Camionnette',1000),(3,'Moto',200),(4,'Camion',2000);
/*!40000 ALTER TABLE `tbl_tarifs` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `tbl_enregistrements`
--

DROP TABLE IF EXISTS `tbl_enregistrements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_enregistrements` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num_ticket` varchar(45) NOT NULL,
  `time_arri` datetime NOT NULL,
  `time_depa` datetime DEFAULT NULL,
  `duree` int(11) DEFAULT '0',
  `montant` int(11) DEFAULT '0',
  `nom_tarif` varchar(50) NOT NULL,
  `prix_tarif` int(11) NOT NULL,
  `num_vehicule` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_enregistrements`
--
-- ORDER BY:  `id`

LOCK TABLES `tbl_enregistrements` WRITE;
/*!40000 ALTER TABLE `tbl_enregistrements` DISABLE KEYS */;
INSERT INTO `tbl_enregistrements` (`id`, `num_ticket`, `time_arri`, `time_depa`, `duree`, `montant`, `nom_tarif`, `prix_tarif`, `num_vehicule`) VALUES (4,'2020-05-TDKT-00000001','2020-05-31 16:03:20',NULL,0,0,'Moto',200,'KTM001'),(5,'2020-05-TDKT-00000002','2020-05-31 16:04:41',NULL,0,0,'Camion',2000,'YTH006');
/*!40000 ALTER TABLE `tbl_enregistrements` ENABLE KEYS */;
UNLOCK TABLES;

