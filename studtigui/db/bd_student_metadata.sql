
--
-- Index pour les tables déchargées
--

--
-- Index pour la table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`matricule`),
  ADD UNIQUE KEY `primaryKey` (`matricule`),
  ADD UNIQUE KEY `primaryIndex` (`matricule`),
  ADD UNIQUE KEY `matricule` (`matricule`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `students`
--
ALTER TABLE `students`
  MODIFY `matricule` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Métadonnées
--
USE `phpmyadmin`;

--
-- Métadonnées pour la table students
--

--
-- Métadonnées pour la base de données bd_student
--
