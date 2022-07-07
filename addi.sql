-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema addi
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `addi` DEFAULT CHARACTER SET utf8 ;
USE `addi` ;

-- -----------------------------------------------------
-- Table `addi`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `addi`.`usuario` (
  `cedula` VARCHAR(10) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `pass` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`cedula`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `addi`.`citamedica`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `addi`.`citamedica` (
  `idCitasMedicas` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreMedico` VARCHAR(40) NOT NULL,
  `especialidad` VARCHAR(20) NOT NULL,
  `ubicacion` VARCHAR(100) NULL DEFAULT NULL,
  `notas` VARCHAR(200) NULL DEFAULT NULL,
  `fecha` DATE NOT NULL,
  `hora` TIME NOT NULL,
  `cedula` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`idCitasMedicas`),
  INDEX `fk_citamedica_usuario1_idx` (`cedula` ASC),
  CONSTRAINT `fk_citamedica_usuario1`
    FOREIGN KEY (`cedula`)
    REFERENCES `addi`.`usuario` (`cedula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `addi`.`citaslaboratorio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `addi`.`citaslaboratorio` (
  `idCitasLaboratorio` INT(11) NOT NULL AUTO_INCREMENT,
  `tipoExamen` VARCHAR(30) NOT NULL,
  `laboratorio` VARCHAR(30) NULL DEFAULT NULL,
  `ubicacion` VARCHAR(60) NULL DEFAULT NULL,
  `notas` VARCHAR(200) NULL DEFAULT NULL,
  `fecha` DATE NOT NULL,
  `hora` TIME NOT NULL,
  `cedula` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`idCitasLaboratorio`),
  INDEX `fk_citaslaboratorio_usuario1_idx` (`cedula` ASC),
  CONSTRAINT `fk_citaslaboratorio_usuario1`
    FOREIGN KEY (`cedula`)
    REFERENCES `addi`.`usuario` (`cedula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `addi`.`tipomedicamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `addi`.`tipomedicamento` (
  `idtipomedicamento` INT(11) NOT NULL AUTO_INCREMENT,
  `tipoMedicamento` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idtipomedicamento`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `addi`.`medicamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `addi`.`medicamento` (
  `idMedicamentos` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(15) NOT NULL,
  `dosis` VARCHAR(40) NOT NULL,
  `veces_dia` INT(11) NOT NULL,
  `frecuencia` VARCHAR(45) NOT NULL,
  `fecha_desde` DATE NOT NULL,
  `fecha_hasta` DATE NULL DEFAULT NULL,
  `idtipomedicamento` INT(11) NOT NULL,
  `cedula` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`idMedicamentos`),
  INDEX `fk_medicamento_tipomedicamento1_idx` (`idtipomedicamento` ASC),
  INDEX `fk_medicamento_usuario1_idx` (`cedula` ASC),
  CONSTRAINT `fk_medicamento_tipomedicamento1`
    FOREIGN KEY (`idtipomedicamento`)
    REFERENCES `addi`.`tipomedicamento` (`idtipomedicamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_medicamento_usuario1`
    FOREIGN KEY (`cedula`)
    REFERENCES `addi`.`usuario` (`cedula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `addi`.`confirmaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `addi`.`confirmaciones` (
  `idConfirmaciones` INT(11) NOT NULL AUTO_INCREMENT,
  `horaProgramada` TIME NOT NULL,
  `horaConfirmacion` TIME NOT NULL,
  `cedula` VARCHAR(10) NOT NULL,
  `idMedicamentos` INT(11) NOT NULL,
  PRIMARY KEY (`idConfirmaciones`),
  INDEX `fk_Confirmaciones_Usuario1_idx` (`cedula` ASC),
  INDEX `fk_confirmaciones_medicamento1_idx` (`idMedicamentos` ASC),
  CONSTRAINT `fk_Confirmaciones_Usuario1`
    FOREIGN KEY (`cedula`)
    REFERENCES `addi`.`usuario` (`cedula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_confirmaciones_medicamento1`
    FOREIGN KEY (`idMedicamentos`)
    REFERENCES `addi`.`medicamento` (`idMedicamentos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `addi`.`recordatoriomedicamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `addi`.`recordatoriomedicamento` (
  `idRecordatorio` INT(11) NOT NULL AUTO_INCREMENT,
  `hora` TIME NOT NULL,
  `medicamento_idMedicamentos` INT(11) NOT NULL,
  PRIMARY KEY (`idRecordatorio`),
  INDEX `fk_recordatoriomedicamento_medicamento1_idx` (`medicamento_idMedicamentos` ASC),
  CONSTRAINT `fk_recordatoriomedicamento_medicamento1`
    FOREIGN KEY (`medicamento_idMedicamentos`)
    REFERENCES `addi`.`medicamento` (`idMedicamentos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


INSERT INTO `addi`.`tipomedicamento` (tipoMedicamento)
  VALUES  ('Pastilla'),
          ('Capsula'),
          ('Jarabe'),
          ('Inyección'),
          ('Suero'),
          ('Otro');
