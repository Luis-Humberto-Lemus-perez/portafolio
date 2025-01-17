<?php
    class Vehiculos_model{
        private $db;
        private $vehiculos;
        public function __construct(){
            $this->db = Conectar::conexion();
            $this->vehiculos = array();
        }
        public function get_vehiculos(){
            $sql = "SELECT * FROM vehiculos";
            $resultado = $this->db->query($sql);
            while($row = $resultado->fetch_assoc()){
                $this->vehiculos[] = $row;
            }
            return $this->vehiculos;
        }
        public function insertar($placa, $marca, $modelo, $anio, $color){
            $sql = "INSERT INTO vehiculos (placa, marca, modelo, anio, color) VALUES ('$placa', '$marca', '$modelo', '$anio', '$color')";
            $resultado = $this->db->query($sql);
        }
        public function editar($id, $placa, $marca, $modelo, $anio, $color){
            $sql = "UPDATE vehiculos SET placa='$placa', marca='$marca', modelo='$modelo', anio='$anio', color='$color' WHERE id='$id'";
            $resultado = $this->db->query($sql);
        }
        public function eliminar($id){
            $sql = "DELETE FROM vehiculos WHERE id='$id'";
            $resultado = $this->db->query($sql);
        }
        public function get_vehiculo($id){
            $sql = "SELECT * FROM vehiculos WHERE id='$id' LIMIT 1";
            $resultado = $this->db->query($sql);
            $row = $resultado->fetch_assoc();
            return $row;
        }
    }
?>