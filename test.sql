/*
 Navicat Premium Data Transfer

 Source Server         : MAMP localhost
 Source Server Type    : MySQL
 Source Server Version : 50638
 Source Host           : localhost:8889
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 50638
 File Encoding         : 65001

 Date: 19/08/2018 12:55:12
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- Database creation
-- create database test_pymysql DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
-- USE test_pymysql;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) COLLATE utf8_bin NOT NULL,
  `password` varchar(255) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

SET FOREIGN_KEY_CHECKS = 1;
