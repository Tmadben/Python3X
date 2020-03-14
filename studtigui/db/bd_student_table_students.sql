
-- --------------------------------------------------------

--
-- Structure de la table `students`
--

DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
  `matricule` bigint(20) UNSIGNED NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `sexe` varchar(10) NOT NULL,
  `age` int(11) NOT NULL,
  `nationality` varchar(100) NOT NULL,
  `classe` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `students`
--

INSERT INTO `students` (`matricule`, `firstname`, `lastname`, `sexe`, `age`, `nationality`, `classe`) VALUES(1, 'Mamadou Ben', 'TRAORE', 'Masculin', 25, 'France', 'IC RESEAUX');
INSERT INTO `students` (`matricule`, `firstname`, `lastname`, `sexe`, `age`, `nationality`, `classe`) VALUES(2, 'Loukou Thiam', 'KOFFI', 'Masculin', 45, 'France', 'IC RESEAUX');
INSERT INTO `students` (`matricule`, `firstname`, `lastname`, `sexe`, `age`, `nationality`, `classe`) VALUES(3, 'HIEN', 'Claudine', 'Feminin', 40, 'France', 'IC Finance');
INSERT INTO `students` (`matricule`, `firstname`, `lastname`, `sexe`, `age`, `nationality`, `classe`) VALUES(4, 'Jean', 'Christophe Poulet', 'Masculin', 60, 'Mali', 'IT RESEAUX');
