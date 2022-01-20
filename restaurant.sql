-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 20, 2022 at 05:58 PM
-- Server version: 8.0.27
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `restaurant`
--
CREATE DATABASE IF NOT EXISTS `restaurant` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `restaurant`;

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE `menu` (
  `id` int NOT NULL,
  `name` varchar(30) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `price` int DEFAULT NULL,
  `category` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`id`, `name`, `price`, `category`) VALUES
(1, 'Nasi Putih', 5000, 'Nasi'),
(2, 'Nasi Uduk', 6500, 'Nasi'),
(3, 'Nasi Putih 1/2', 4000, 'Nasi'),
(4, 'Ayam Bekakak 1 ekor', 85000, 'Lauk'),
(5, 'Ayam Bekakak 1/4 ekor', 22000, 'Lauk'),
(6, 'Tahu Goreng', 2000, 'Lauk'),
(7, 'Tempe Goreng', 2000, 'Lauk'),
(8, 'Krupuk Blek', 2000, 'Cemilan'),
(9, 'Rempeyek', 5000, 'Cemilan'),
(10, 'Sate Ati Ampela', 5000, 'Lauk'),
(11, 'Lalapan', 2000, 'Sayuran'),
(12, 'Pete Goreng', 10000, 'Sayuran'),
(13, 'Teh Tawar', 2000, 'Minuman'),
(14, 'Teh Manis', 5000, 'Minuman'),
(15, 'Air Mineral', 5000, 'Minuman');

-- --------------------------------------------------------

--
-- Table structure for table `menucategories`
--

CREATE TABLE `menucategories` (
  `category` varchar(15) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `menucategories`
--

INSERT INTO `menucategories` (`category`) VALUES
('Cemilan'),
('Lauk'),
('Minuman'),
('Nasi'),
('Sayuran');

-- --------------------------------------------------------

--
-- Table structure for table `staffs`
--

CREATE TABLE `staffs` (
  `id` int NOT NULL,
  `firstName` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `lastName` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `position` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `gender` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `age` int DEFAULT NULL
) ;

--
-- Dumping data for table `staffs`
--

INSERT INTO `staffs` (`id`, `firstName`, `lastName`, `email`, `position`, `gender`, `age`) VALUES
(1, 'Sani', 'Sholihin', 'sanish@gmail.com', 'Chef', 'Male', 31),
(2, 'Agung', 'Hidayat', 'hidangan@gmail.com', 'Waiter', 'Male', 21),
(3, 'Diah', '', 'diadiadia@gmail.com', 'Cashier', 'Female', 49),
(4, 'Galih', 'Kamulyan', 'kakiku@gmail.com', 'Cashier', 'Male', 22);

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

CREATE TABLE `status` (
  `status` varchar(25) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `status`
--

INSERT INTO `status` (`status`) VALUES
('Cancelled'),
('Finished'),
('Order Delivered'),
('Order Received'),
('Waiting for Order');

-- --------------------------------------------------------

--
-- Table structure for table `tables`
--

CREATE TABLE `tables` (
  `tableNo` int NOT NULL,
  `numberofSeats` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tables`
--

INSERT INTO `tables` (`tableNo`, `numberofSeats`) VALUES
(1, 6),
(2, 6),
(3, 6),
(4, 4),
(5, 4),
(6, 4),
(7, 4),
(8, 2),
(9, 2),
(10, 2);

-- --------------------------------------------------------

--
-- Table structure for table `transactionmenus`
--

CREATE TABLE `transactionmenus` (
  `transactionId` int NOT NULL,
  `menuId` int NOT NULL,
  `qty` int DEFAULT NULL,
  `price` int NOT NULL,
  `subtotal` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transactionmenus`
--

INSERT INTO `transactionmenus` (`transactionId`, `menuId`, `qty`, `price`, `subtotal`) VALUES
(2, 3, 1, 4000, 4000),
(2, 8, 3, 2000, 6000);

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `id` int NOT NULL,
  `date` date DEFAULT NULL,
  `arrival_time` time DEFAULT NULL,
  `exit_time` time DEFAULT NULL,
  `staffId` int NOT NULL,
  `tableNo` int NOT NULL,
  `totalPrice` int NOT NULL DEFAULT '0',
  `status` varchar(25) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transactions`
--

INSERT INTO `transactions` (`id`, `date`, `arrival_time`, `exit_time`, `staffId`, `tableNo`, `totalPrice`, `status`) VALUES
(1, '2022-01-01', '21:22:05', '22:46:00', 2, 3, 0, 'Cancelled'),
(2, '2022-01-20', '22:29:00', NULL, 1, 8, 10000, 'Waiting for Order');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `username` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `picture` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `staffId` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`username`, `password`, `picture`, `staffId`) VALUES
('galih', '$2b$12$4RtFFapYe2psq0e0OCFnAu3s7yPRJ3dpMVjLbGufX/hhXTVNk.DWC', 'galih.png', 4);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category` (`category`);

--
-- Indexes for table `menucategories`
--
ALTER TABLE `menucategories`
  ADD PRIMARY KEY (`category`);

--
-- Indexes for table `staffs`
--
ALTER TABLE `staffs`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`status`);

--
-- Indexes for table `tables`
--
ALTER TABLE `tables`
  ADD PRIMARY KEY (`tableNo`);

--
-- Indexes for table `transactionmenus`
--
ALTER TABLE `transactionmenus`
  ADD PRIMARY KEY (`transactionId`,`menuId`),
  ADD KEY `menuId` (`menuId`);

--
-- Indexes for table `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `staffId` (`staffId`),
  ADD KEY `tableNo` (`tableNo`),
  ADD KEY `status` (`status`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`),
  ADD KEY `staffId` (`staffId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `menu`
--
ALTER TABLE `menu`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `staffs`
--
ALTER TABLE `staffs`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transactions`
--
ALTER TABLE `transactions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `menu`
--
ALTER TABLE `menu`
  ADD CONSTRAINT `menu_ibfk_1` FOREIGN KEY (`category`) REFERENCES `menucategories` (`category`),
  ADD CONSTRAINT `menu_ibfk_2` FOREIGN KEY (`category`) REFERENCES `menucategories` (`category`) ON UPDATE CASCADE;

--
-- Constraints for table `transactionmenus`
--
ALTER TABLE `transactionmenus`
  ADD CONSTRAINT `transactionmenus_ibfk_2` FOREIGN KEY (`menuId`) REFERENCES `menu` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `transactionmenus_ibfk_3` FOREIGN KEY (`transactionId`) REFERENCES `transactions` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `transactions`
--
ALTER TABLE `transactions`
  ADD CONSTRAINT `transactions_ibfk_2` FOREIGN KEY (`tableNo`) REFERENCES `tables` (`tableNo`) ON UPDATE CASCADE,
  ADD CONSTRAINT `transactions_ibfk_3` FOREIGN KEY (`status`) REFERENCES `status` (`status`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `transactions_ibfk_4` FOREIGN KEY (`staffId`) REFERENCES `staffs` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`staffId`) REFERENCES `staffs` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
