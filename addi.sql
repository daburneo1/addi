-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema addi
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema addi
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `addi` DEFAULT CHARACTER SET utf8 ;
USE `addi` ;

-- -----------------------------------------------------
-- Table `addi`.`citamedica`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `addi`.`citamedica` (
  `idCitasMedicas` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreMedico` VARCHAR(40) NOT NULL,
  `especialidad` VARCHAR(20) NOT NULL,
  `ubicacion` VARCHAR(100) NULL DEFAULT NULL,
  `notas` VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (`idCitasMedicas`))
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
  PRIMARY KEY (`idCitasLaboratorio`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


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
-- Table `addi`.`confirmaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `addi`.`confirmaciones` (
  `idConfirmaciones` INT(11) NOT NULL AUTO_INCREMENT,
  `medicamento` VARCHAR(30) NOT NULL,
  `horaProgramada` TIME NOT NULL,
  `horaConfirmacion` TIME NOT NULL,
  `cedulaUsuario` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`idConfirmaciones`),
  INDEX `fk_Confirmaciones_Usuario1_idx` (`cedulaUsuario` ASC),
  CONSTRAINT `fk_Confirmaciones_Usuario1`
    FOREIGN KEY (`cedulaUsuario`)
    REFERENCES `addi`.`usuario` (`cedula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `addi`.`tipomedicamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `addi`.`tipomedicamento` (
  `idtipomedicamento` INT NOT NULL AUTO_INCREMENT,
  `tipoMedicamento` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idtipomedicamento`))
ENGINE = InnoDB;

INSERT INTO `addi`.`tipomedicamento` (tipoMedicamento)
  VALUES  ('Pastilla'),
          ('Capsula'),
          ('Inyección'),
          ('Suero'),
          ('Otro');
-- -----------------------------------------------------
-- Table `addi`.`medicamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `addi`.`medicamento` (
  `idMedicamentos` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(15) NOT NULL,
  `dosis` VARCHAR(40) NOT NULL,
  `frecuencia` VARCHAR(45) NOT NULL,
  `fecha_desde` DATE NOT NULL,
  `fecha_hasta` DATE NULL,
  `idtipomedicamento` INT NOT NULL,
  PRIMARY KEY (`idMedicamentos`),
  INDEX `fk_medicamento_tipomedicamento1_idx` (`idtipomedicamento` ASC),
  CONSTRAINT `fk_medicamento_tipomedicamento1`
    FOREIGN KEY (`idtipomedicamento`)
    REFERENCES `addi`.`tipomedicamento` (`idtipomedicamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `addi`.`recordatoriocitamedica`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `addi`.`recordatoriocitamedica` (
  `idRecordatorioCitaMedica` INT(11) NOT NULL AUTO_INCREMENT,
  `hora` DATETIME NOT NULL,
  `idCitasMedicas` INT(11) NOT NULL,
  `cedulaUsuario` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`idRecordatorioCitaMedica`),
  INDEX `fk_RecordatorioCitaMedica_CitaMedica1_idx` (`idCitasMedicas` ASC),
  INDEX `fk_RecordatorioCitaMedica_Usuario1_idx` (`cedulaUsuario` ASC),
  CONSTRAINT `fk_RecordatorioCitaMedica_CitaMedica1`
    FOREIGN KEY (`idCitasMedicas`)
    REFERENCES `addi`.`citamedica` (`idCitasMedicas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_RecordatorioCitaMedica_Usuario1`
    FOREIGN KEY (`cedulaUsuario`)
    REFERENCES `addi`.`usuario` (`cedula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `addi`.`recordatoriocitaslaboratorio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `addi`.`recordatoriocitaslaboratorio` (
  `idRecordatorioCitasLaboratorio` INT(11) NOT NULL AUTO_INCREMENT,
  `hora` DATETIME NOT NULL,
  `idCitasLaboratorio` INT(11) NOT NULL,
  `cedulaUsuario` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`idRecordatorioCitasLaboratorio`),
  INDEX `fk_RecordatorioCitasLaboratorio_CitasLaboratorio1_idx` (`idCitasLaboratorio` ASC),
  INDEX `fk_RecordatorioCitasLaboratorio_Usuario1_idx` (`cedulaUsuario` ASC),
  CONSTRAINT `fk_RecordatorioCitasLaboratorio_CitasLaboratorio1`
    FOREIGN KEY (`idCitasLaboratorio`)
    REFERENCES `addi`.`citaslaboratorio` (`idCitasLaboratorio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_RecordatorioCitasLaboratorio_Usuario1`
    FOREIGN KEY (`cedulaUsuario`)
    REFERENCES `addi`.`usuario` (`cedula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `addi`.`recordatoriomedicamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `addi`.`recordatoriomedicamento` (
  `idRecordatorio` INT(11) NOT NULL AUTO_INCREMENT,
  `hora` DATETIME NOT NULL,
  `idMedicamentos` INT(11) NOT NULL,
  `cedulaUsuario` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`idRecordatorio`),
  INDEX `fk_Recordatorio_Medicamentos_idx` (`idMedicamentos` ASC),
  INDEX `fk_RecordatorioMedicamento_Usuario1_idx` (`cedulaUsuario` ASC),
  CONSTRAINT `fk_RecordatorioMedicamento_Usuario1`
    FOREIGN KEY (`cedulaUsuario`)
    REFERENCES `addi`.`usuario` (`cedula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Recordatorio_Medicamentos`
    FOREIGN KEY (`idMedicamentos`)
    REFERENCES `addi`.`medicamento` (`idMedicamentos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;