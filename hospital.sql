-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 24, 2021 at 09:50 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hms_software`
--

-- --------------------------------------------------------

--
-- Table structure for table `hospital`
--

CREATE TABLE `hospital` (
  `id` int(255) NOT NULL,
  `name_of_table` varchar(255) NOT NULL,
  `ref` varchar(255) NOT NULL,
  `dose` varchar(255) NOT NULL,
  `no_of_tablets` varchar(255) NOT NULL,
  `lot` varchar(255) NOT NULL,
  `issuedate` varchar(255) NOT NULL,
  `exp_date` varchar(255) NOT NULL,
  `daily_dose` varchar(255) NOT NULL,
  `storage` varchar(255) NOT NULL,
  `nhs_number` varchar(255) NOT NULL,
  `p_name` varchar(255) NOT NULL,
  `dob` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hospital`
--

INSERT INTO `hospital` (`id`, `name_of_table`, `ref`, `dose`, `no_of_tablets`, `lot`, `issuedate`, `exp_date`, `daily_dose`, `storage`, `nhs_number`, `p_name`, `dob`, `address`) VALUES
(1, 'Nice', '100', 'sourov pal', '', '', '', '01-01-2022', '', '', '', '', '24/10/2021', 'a'),
(2, 'Nice', '100', '', '', '', '', '', '', '', '', '', '24/10/2021', 'a'),
(3, 'Nice', '100', '', '', '', '', '', '', '', '', '', '24/10/2021', 'a'),
(4, 'Nice', '100', '', '', '', '', '', '', '', '', '', '24/10/2021', ''),
(5, 'Nice', '100', '', '', '', '', '', '', '', '', '', '24/10/2021', ''),
(7, 'Nice', '100', '', 'aaaaa', '', '', '', '', '', '', '', '24/10/2021', ''),
(8, 'Nice', '200', '', 'aaaaa', '', '', '', '', '', '', '', '24/10/2021', ''),
(9, 'Nice', '400', '', 'aaaaa', '', '', '', '', '', '', '', '24/10/2021', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `hospital`
--
ALTER TABLE `hospital`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `hospital`
--
ALTER TABLE `hospital`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
