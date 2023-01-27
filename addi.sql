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
-- Table `addi`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `addi`.`usuario` (
  `idUsuario` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idUsuario`))
ENGINE = InnoDB;


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
  `idUsuario` INT NOT NULL,
  PRIMARY KEY (`idCitasMedicas`),
  INDEX `fk_citamedica_Usuario1_idx` (`idUsuario` ASC),
  CONSTRAINT `fk_citamedica_Usuario1`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `addi`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 2
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
  `idUsuario` INT NOT NULL,
  PRIMARY KEY (`idCitasLaboratorio`),
  INDEX `fk_citaslaboratorio_Usuario1_idx` (`idUsuario` ASC),
  CONSTRAINT `fk_citaslaboratorio_Usuario1`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `addi`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `addi`.`medicamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `addi`.`medicamento` (
  `idMedicamento` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(15) NOT NULL,
  `dosis` VARCHAR(40) NOT NULL,
  `veces_dia` INT(11) NOT NULL,
  `frecuencia` VARCHAR(200) NULL DEFAULT NULL,
  `fecha_desde` DATE NOT NULL,
  `fecha_hasta` DATE NULL DEFAULT NULL,
  `idUsuario` INT NOT NULL,
  PRIMARY KEY (`idMedicamento`),
  INDEX `fk_medicamento_Usuario1_idx` (`idUsuario` ASC),
  CONSTRAINT `fk_medicamento_Usuario1`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `addi`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `addi`.`recordatoriomedicamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `addi`.`recordatoriomedicamento` (
  `idRecordatorio` INT(11) NOT NULL AUTO_INCREMENT,
  `hora` TIME NOT NULL,
  `medicamento_idMedicamento` INT(11) NOT NULL,
  PRIMARY KEY (`idRecordatorio`),
  INDEX `fk_recordatoriomedicamento_medicamento1_idx` (`medicamento_idMedicamento` ASC),
  CONSTRAINT `fk_recordatoriomedicamento_medicamento1`
    FOREIGN KEY (`medicamento_idMedicamento`)
    REFERENCES `addi`.`medicamento` (`idMedicamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 10
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

