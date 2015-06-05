-- phpMyAdmin SQL Dump
-- version 3.4.10.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 02, 2015 at 08:25 PM
-- Server version: 5.5.31
-- PHP Version: 5.3.10-1ubuntu3.11

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `taimi.ca`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=107 ;

--
-- Dumping data for table `auth_permission`
--



-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `auth_user`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `cmsplugin_file`
--

CREATE TABLE IF NOT EXISTS `cmsplugin_file` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `file` varchar(100) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  UNIQUE KEY `cmsplugin_ptr_id` (`cmsplugin_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cmsplugin_file`
--


-- --------------------------------------------------------

--
-- Table structure for table `cmsplugin_picture`
--

CREATE TABLE IF NOT EXISTS `cmsplugin_picture` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `url` varchar(255) DEFAULT NULL,
  `page_link_id` int(11) DEFAULT NULL,
  `alt` varchar(255) DEFAULT NULL,
  `longdesc` varchar(255) DEFAULT NULL,
  `float` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`cmsplugin_ptr_id`),
  KEY `cmsplugin_picture_37c07cc5` (`page_link_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cmsplugin_picture`
--

-- --------------------------------------------------------

--
-- Table structure for table `cmsplugin_testimoniesplugin`
--

CREATE TABLE IF NOT EXISTS `cmsplugin_testimoniesplugin` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `section` varchar(200) NOT NULL,
  PRIMARY KEY (`cmsplugin_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cmsplugin_testimoniesplugin`
--
-- --------------------------------------------------------

--
-- Table structure for table `cmsplugin_text`
--

CREATE TABLE IF NOT EXISTS `cmsplugin_text` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `body` longtext NOT NULL,
  PRIMARY KEY (`cmsplugin_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cmsplugin_text`
--


-- --------------------------------------------------------

--
-- Table structure for table `cmsplugin_video`
--

CREATE TABLE IF NOT EXISTS `cmsplugin_video` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `movie` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `auto_play` tinyint(1) NOT NULL,
  `loop` tinyint(1) NOT NULL,
  `bgcolor` varchar(6) NOT NULL,
  `fullscreen` tinyint(1) NOT NULL,
  `width` smallint(5) unsigned NOT NULL,
  `movie_url` varchar(255) DEFAULT NULL,
  `buttonhighlightcolor` varchar(6) NOT NULL DEFAULT 'FFFFFF',
  `auto_hide` tinyint(1) NOT NULL DEFAULT '1',
  `seekbarcolor` varchar(6) NOT NULL DEFAULT '13ABEC',
  `buttonoutcolor` varchar(6) NOT NULL DEFAULT '333333',
  `textcolor` varchar(6) NOT NULL DEFAULT 'FFFFFF',
  `seekbarbgcolor` varchar(6) NOT NULL DEFAULT '333333',
  `loadingbarcolor` varchar(6) NOT NULL DEFAULT '828282',
  `buttonovercolor` varchar(6) NOT NULL DEFAULT '000000',
  `height` smallint(5) unsigned NOT NULL,
  PRIMARY KEY (`cmsplugin_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `cms_cmsplugin`
--

CREATE TABLE IF NOT EXISTS `cms_cmsplugin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `placeholder_id` int(11) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `position` smallint(5) unsigned DEFAULT NULL,
  `language` varchar(15) NOT NULL,
  `plugin_type` varchar(50) NOT NULL,
  `creation_date` datetime NOT NULL,
  `changed_date` datetime NOT NULL,
  `level` int(10) unsigned NOT NULL,
  `lft` int(10) unsigned NOT NULL,
  `rght` int(10) unsigned NOT NULL,
  `tree_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cms_cmsplugin_c1ca2850` (`placeholder_id`),
  KEY `cms_cmsplugin_63f17a16` (`parent_id`),
  KEY `cms_cmsplugin_8a7ac9ab` (`language`),
  KEY `cms_cmsplugin_ad070cd0` (`plugin_type`),
  KEY `cms_cmsplugin_2a8f42e8` (`level`),
  KEY `cms_cmsplugin_42b06ff6` (`lft`),
  KEY `cms_cmsplugin_91543e5a` (`rght`),
  KEY `cms_cmsplugin_efd07f28` (`tree_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=289 ;

--
-- Dumping data for table `cms_cmsplugin`
--

-- --------------------------------------------------------

--
-- Table structure for table `cms_extended_pagedesc`
--

CREATE TABLE IF NOT EXISTS `cms_extended_pagedesc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` int(11) NOT NULL,
  `description` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `page_id` (`page_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `cms_extended_pagedesc`
--

-- --------------------------------------------------------

--
-- Table structure for table `cms_globalpagepermission`
--

CREATE TABLE IF NOT EXISTS `cms_globalpagepermission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `can_change` tinyint(1) NOT NULL,
  `can_add` tinyint(1) NOT NULL,
  `can_delete` tinyint(1) NOT NULL,
  `can_change_advanced_settings` tinyint(1) NOT NULL,
  `can_publish` tinyint(1) NOT NULL,
  `can_change_permissions` tinyint(1) NOT NULL,
  `can_move_page` tinyint(1) NOT NULL,
  `can_moderate` tinyint(1) NOT NULL,
  `can_view` tinyint(1) NOT NULL,
  `can_recover_page` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cms_globalpagepermission_fbfc09f1` (`user_id`),
  KEY `cms_globalpagepermission_bda51c3c` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `cms_globalpagepermission_sites`
--

CREATE TABLE IF NOT EXISTS `cms_globalpagepermission_sites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `globalpagepermission_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `globalpagepermission_id` (`globalpagepermission_id`,`site_id`),
  KEY `cms_globalpagepermission_sites_f5debdc1` (`globalpagepermission_id`),
  KEY `cms_globalpagepermission_sites_6223029` (`site_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `cms_page`
--

CREATE TABLE IF NOT EXISTS `cms_page` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_by` varchar(70) NOT NULL,
  `changed_by` varchar(70) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `creation_date` datetime NOT NULL,
  `changed_date` datetime NOT NULL,
  `publication_date` datetime DEFAULT NULL,
  `publication_end_date` datetime DEFAULT NULL,
  `in_navigation` tinyint(1) NOT NULL,
  `soft_root` tinyint(1) NOT NULL,
  `reverse_id` varchar(40) DEFAULT NULL,
  `navigation_extenders` varchar(80) DEFAULT NULL,
  `published` tinyint(1) NOT NULL,
  `template` varchar(100) NOT NULL,
  `site_id` int(11) NOT NULL,
  `moderator_state` smallint(6) NOT NULL,
  `level` int(10) unsigned NOT NULL,
  `lft` int(10) unsigned NOT NULL,
  `rght` int(10) unsigned NOT NULL,
  `tree_id` int(10) unsigned NOT NULL,
  `login_required` tinyint(1) NOT NULL,
  `limit_visibility_in_menu` smallint(6) DEFAULT NULL,
  `publisher_is_draft` tinyint(1) NOT NULL,
  `publisher_public_id` int(11) DEFAULT NULL,
  `publisher_state` smallint(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `publisher_public_id` (`publisher_public_id`),
  KEY `cms_page_63f17a16` (`parent_id`),
  KEY `cms_page_ee664462` (`publication_date`),
  KEY `cms_page_a221fe64` (`publication_end_date`),
  KEY `cms_page_3c0ea264` (`in_navigation`),
  KEY `cms_page_baa27763` (`soft_root`),
  KEY `cms_page_b56116b` (`reverse_id`),
  KEY `cms_page_d98c6d14` (`navigation_extenders`),
  KEY `cms_page_6223029` (`site_id`),
  KEY `cms_page_2a8f42e8` (`level`),
  KEY `cms_page_42b06ff6` (`lft`),
  KEY `cms_page_91543e5a` (`rght`),
  KEY `cms_page_efd07f28` (`tree_id`),
  KEY `cms_page_c909672f` (`limit_visibility_in_menu`),
  KEY `cms_page_16d2d3fa` (`publisher_is_draft`),
  KEY `cms_page_a0014f5a` (`publisher_state`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=28 ;


-- --------------------------------------------------------

--
-- Table structure for table `cms_pagemoderator`
--

CREATE TABLE IF NOT EXISTS `cms_pagemoderator` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `moderate_page` tinyint(1) NOT NULL,
  `moderate_children` tinyint(1) NOT NULL,
  `moderate_descendants` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cms_pagemoderator_32d04bc7` (`page_id`),
  KEY `cms_pagemoderator_fbfc09f1` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;
--
-- Dumping data for table `cms_page`
--
CREATE TABLE IF NOT EXISTS `cms_pagemoderatorstate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `created` datetime NOT NULL,
  `action` varchar(3) DEFAULT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cms_pagemoderatorstate_32d04bc7` (`page_id`),
  KEY `cms_pagemoderatorstate_fbfc09f1` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `cms_pagepermission`
--

CREATE TABLE IF NOT EXISTS `cms_pagepermission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `can_change` tinyint(1) NOT NULL,
  `can_add` tinyint(1) NOT NULL,
  `can_delete` tinyint(1) NOT NULL,
  `can_change_advanced_settings` tinyint(1) NOT NULL,
  `can_publish` tinyint(1) NOT NULL,
  `can_change_permissions` tinyint(1) NOT NULL,
  `can_move_page` tinyint(1) NOT NULL,
  `can_moderate` tinyint(1) NOT NULL,
  `can_view` tinyint(1) NOT NULL,
  `grant_on` int(11) NOT NULL,
  `page_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cms_pagepermission_fbfc09f1` (`user_id`),
  KEY `cms_pagepermission_bda51c3c` (`group_id`),
  KEY `cms_pagepermission_32d04bc7` (`page_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `cms_pageuser`
--

CREATE TABLE IF NOT EXISTS `cms_pageuser` (
  `user_ptr_id` int(11) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  PRIMARY KEY (`user_ptr_id`),
  KEY `cms_pageuser_b5de30be` (`created_by_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `cms_pageusergroup`
--

CREATE TABLE IF NOT EXISTS `cms_pageusergroup` (
  `group_ptr_id` int(11) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  PRIMARY KEY (`group_ptr_id`),
  KEY `cms_pageusergroup_b5de30be` (`created_by_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `cms_page_placeholders`
--

CREATE TABLE IF NOT EXISTS `cms_page_placeholders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` int(11) NOT NULL,
  `placeholder_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `page_id` (`page_id`,`placeholder_id`),
  KEY `cms_page_placeholders_32d04bc7` (`page_id`),
  KEY `cms_page_placeholders_c1ca2850` (`placeholder_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=34 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
CREATE TABLE IF NOT EXISTS `cms_placeholder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `slot` varchar(50) NOT NULL,
  `default_width` smallint(5) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cms_placeholder_400badfd` (`slot`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=34 ;

CREATE TABLE IF NOT EXISTS `cms_redirects_cmsredirect` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` int(11) DEFAULT NULL,
  `site_id` int(11) NOT NULL,
  `old_path` varchar(200) NOT NULL,
  `new_path` varchar(200) NOT NULL,
  `response_code` varchar(3) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cms_redirects_cmsredirect_site_id_532e5a8b_uniq` (`site_id`,`old_path`),
  KEY `cms_redirects_cmsredirect_32d04bc7` (`page_id`),
  KEY `cms_redirects_cmsredirect_6223029` (`site_id`),
  KEY `cms_redirects_cmsredirect_516c23f0` (`old_path`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

CREATE TABLE IF NOT EXISTS `cms_title` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `language` varchar(15) NOT NULL,
  `title` varchar(255) NOT NULL,
  `menu_title` varchar(255) DEFAULT NULL,
  `slug` varchar(255) NOT NULL,
  `path` varchar(255) NOT NULL,
  `has_url_overwrite` tinyint(1) NOT NULL,
  `application_urls` varchar(200) DEFAULT NULL,
  `redirect` varchar(255) DEFAULT NULL,
  `meta_description` longtext,
  `meta_keywords` varchar(255) DEFAULT NULL,
  `page_title` varchar(255) DEFAULT NULL,
  `page_id` int(11) NOT NULL,
  `creation_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `language` (`language`,`page_id`),
  KEY `cms_title_8a7ac9ab` (`language`),
  KEY `cms_title_a951d5d6` (`slug`),
  KEY `cms_title_6a8a34e2` (`path`),
  KEY `cms_title_c269b1d2` (`has_url_overwrite`),
  KEY `cms_title_23b1fc68` (`application_urls`),
  KEY `cms_title_32d04bc7` (`page_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=95 ;

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_fbfc09f1` (`user_id`),
  KEY `django_admin_log_e4470c6e` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=809 ;

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=37 ;

CREATE TABLE IF NOT EXISTS `django_redirect` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `site_id` int(11) NOT NULL,
  `old_path` varchar(200) NOT NULL,
  `new_path` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `site_id` (`site_id`,`old_path`),
  KEY `django_redirect_6223029` (`site_id`),
  KEY `django_redirect_516c23f0` (`old_path`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;


CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

CREATE TABLE IF NOT EXISTS `menus_cachekey` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `language` varchar(255) NOT NULL,
  `site` int(10) unsigned NOT NULL,
  `key` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=342 ;

CREATE TABLE IF NOT EXISTS `nouvelles_nouvelle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_created` date NOT NULL,
  `titre` varchar(150) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `description` longtext NOT NULL,
  `language` varchar(2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `produits_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `associated_page_id` int(11) NOT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  `description` text,
  `image2` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `produits_category_57390c4d` (`associated_page_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

CREATE TABLE IF NOT EXISTS `produits_categorytranslation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `language_code` varchar(15) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `description` longtext,
  `master_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `language_code` (`language_code`,`master_id`),
  KEY `produits_categorytranslation_11e09408` (`language_code`),
  KEY `produits_categorytranslation_64d805fc` (`master_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=21 ;

CREATE TABLE IF NOT EXISTS `produits_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `part_no` varchar(30) NOT NULL,
  `a` varchar(30) DEFAULT '',
  `b` varchar(30) DEFAULT '',
  `p1` varchar(30) DEFAULT '',
  `p2` varchar(30) DEFAULT '',
  `p3` varchar(30) DEFAULT NULL,
  `p4` varchar(30) DEFAULT NULL,
  `h1` varchar(30) DEFAULT '',
  `h2` varchar(30) DEFAULT '',
  `seal_kit` varchar(30) DEFAULT '',
  `subcategory_id` int(11) NOT NULL,
  `c` varchar(30) DEFAULT '',
  `ports` varchar(150) DEFAULT NULL,
  `weight` varchar(150) DEFAULT NULL,
  `online_video` varchar(250) DEFAULT NULL,
  `image` varchar(45) DEFAULT NULL,
  `d` varchar(30) DEFAULT NULL,
  `reference` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `produits_product_6ec4c7cb` (`subcategory_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=247 ;

CREATE TABLE IF NOT EXISTS `produits_subcategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `category_id` int(11) NOT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `image` varchar(45) DEFAULT NULL,
  `order` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `produits_subcategory_42dc49bc` (`category_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=61 ;

CREATE TABLE IF NOT EXISTS `produits_subcategorytranslation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `language_code` varchar(15) NOT NULL,
  `titre` varchar(255) DEFAULT NULL,
  `description` longtext,
  `master_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `language_code` (`language_code`,`master_id`),
  KEY `produits_subcategorytranslation_11e09408` (`language_code`),
  KEY `produits_subcategorytranslation_64d805fc` (`master_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=59 ;

CREATE TABLE IF NOT EXISTS `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=59 ;

CREATE TABLE IF NOT EXISTS `testimonies_testimonies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `nom` varchar(150) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `section` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

CREATE TABLE IF NOT EXISTS `testimonies_testimoniestranslation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `language_code` varchar(15) NOT NULL,
  `description` longtext,
  `poste` varchar(150) DEFAULT NULL,
  `master_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `language_code` (`language_code`,`master_id`),
  KEY `testimonies_testimoniestranslation_11e09408` (`language_code`),
  KEY `testimonies_testimoniestranslation_64d805fc` (`master_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=33 ;


CREATE TABLE IF NOT EXISTS `thumbnail_kvstore` (
  `key` varchar(200) NOT NULL,
  `value` longtext NOT NULL,
  PRIMARY KEY (`key`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
