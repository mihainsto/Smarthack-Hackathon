-- --------------------------------------------------------
-- Host:                         13.74.164.206
-- Server version:               5.7.27-0ubuntu0.18.04.1 - (Ubuntu)
-- Server OS:                    Linux
-- HeidiSQL Version:             10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping structure for table codeleones.ads
CREATE TABLE IF NOT EXISTS `ads` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `user_id` int(10) unsigned DEFAULT NULL,
  `description` text,
  `category` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `post_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `active` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

-- Dumping data for table codeleones.ads: ~6 rows (approximately)
/*!40000 ALTER TABLE `ads` DISABLE KEYS */;
INSERT INTO `ads` (`id`, `title`, `user_id`, `description`, `category`, `location`, `post_time`, `active`) VALUES
	(1, 'Donez canapea extensibila', 1, 'Donez canapea extensibila de doua persoane, mai multe detalii la telefon.', '2', 'Buftea', '2019-11-03 07:51:30', 0),
	(2, 'Ajutor la matematica', 1, 'Ofer ajutor la matematica elevilor in ani terminali de liceu.', '1', 'Buftea', '2019-11-03 07:52:26', 1),
	(3, 'Cina gratuita', 1, 'In dorinta de a nu risipi mancare oferim o cina gratuita in intervalul 21:00-22:00.', '0', 'Cluj-Napoca', '2019-11-03 07:54:12', 1),
	(4, 'Jucarii', 2, 'Donez jucarii pentru copii cu varsta intre 3 si 5 ani.', '2', 'Buftea', '2019-11-03 07:56:44', 1),
	(5, 'Donez pui pisica', 2, 'Donez pui de pisica cu varsta de doua luni deparazitati si vaccinati.', '2', 'Otopeni', '2019-11-03 07:59:20', 1),
	(9, 'ofer combina frigorifica', 1, 'ofer combina frigorifica', '2', 'Buftea', '2019-11-03 12:01:06', 1);
/*!40000 ALTER TABLE `ads` ENABLE KEYS */;

-- Dumping structure for table codeleones.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone_number` varchar(100) DEFAULT NULL,
  `register_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- Dumping data for table codeleones.users: ~2 rows (approximately)
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`id`, `username`, `password`, `email`, `phone_number`, `register_date`) VALUES
	(1, 'stefan', '123123', 'cristeastefan1999@gmail.com', '0751936455', '2019-11-03 07:19:11'),
	(2, 'ionpopescu', '123123', 'ion.popescu@gmail.com', '0712345678', '2019-11-03 07:55:24');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

-- Dumping structure for table codeleones.user_preferences
CREATE TABLE IF NOT EXISTS `user_preferences` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL DEFAULT '0',
  `category` int(11) NOT NULL DEFAULT '0',
  `keyword` text NOT NULL,
  PRIMARY KEY (`id`,`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- Dumping data for table codeleones.user_preferences: ~1 rows (approximately)
/*!40000 ALTER TABLE `user_preferences` DISABLE KEYS */;
INSERT INTO `user_preferences` (`id`, `user_id`, `category`, `keyword`) VALUES
	(4, 1, 2, 'frigider');
/*!40000 ALTER TABLE `user_preferences` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
