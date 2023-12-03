-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 03, 2023 at 04:49 PM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_recognizer`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
CREATE TABLE IF NOT EXISTS `student` (
  `Dep` varchar(45) NOT NULL,
  `course` varchar(45) NOT NULL,
  `Year` varchar(45) NOT NULL,
  `Semester` varchar(45) NOT NULL,
  `Student_id` varchar(45) NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Division` varchar(45) NOT NULL,
  `Roll` varchar(45) NOT NULL,
  `Gender` varchar(45) NOT NULL,
  `Dob` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Phone` varchar(45) NOT NULL,
  `Address` varchar(45) NOT NULL,
  `Teacher` varchar(45) NOT NULL,
  `PhotoSample` varchar(45) NOT NULL,
  PRIMARY KEY (`Student_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`Dep`, `course`, `Year`, `Semester`, `Student_id`, `Name`, `Division`, `Roll`, `Gender`, `Dob`, `Email`, `Phone`, `Address`, `Teacher`, `PhotoSample`) VALUES
('Fakulteti i Shkencave Kompjuterike', 'FSHK-SD', '2021-22', 'Semester-5', '210306034', 'Rrezart', 'A', '212121', 'Male', '232', 'sasasqas', '121212', 'assas', 'qassas', 'Yes'),
('Fakulteti i Shkencave Kompjuterike', 'FSHK-SD', '2021-22', 'Semester-5', '210306076', 'Xhafer', 'A', '01', 'Male', '22', 'xhafer@gmail.com', '21212', 'Prizren', 'Test', 'Yes');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
