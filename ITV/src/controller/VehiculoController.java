package controller;

import java.util.LinkedList;
import java.util.Queue;

import modelo.DatosVehiculos;
import modelo.Vehiculo;

public class VehiculoController {
    private Queue<DatosVehiculos> colaEspera;
    private Queue<DatosVehiculos> colaAtendidos;

    public VehiculoController() {
        this.colaEspera = new LinkedList<DatosVehiculos>();
        this.colaAtendidos = new LinkedList<DatosVehiculos>();
    }

    public Queue<DatosVehiculos> getColaEspera() {
        return colaEspera;
    }

    public Queue<DatosVehiculos> getColaAtendidos() {
        return colaAtendidos;
    }

    public void nuevoVehiculo(Vehiculo vehiculo) {
        DatosVehiculos dv1 = new DatosVehiculos(vehiculo);
        this.colaEspera.add(dv1);
    }

    public Vehiculo llamarVehiculo() {
        DatosVehiculos dv1 = this.colaEspera.poll();
        this.colaAtendidos.add(dv1);
        dv1.atiende();

        return dv1.getVehiculo();
    }

    public void timepoEspera() {
        System.out.println("Vehiculo");
        System.out.println("*********************");
        long timepoEspera = 0;
    
        if (colaAtendidos.isEmpty()) {
            System.out.println("No hay vehículos atendidos. No se puede calcular la media de espera.");
            return;
        }
    
        for (DatosVehiculos datosVehiculos : colaAtendidos) {
            System.out.println("Nombre: " + datosVehiculos.getVehiculo().getNombre() + " | Apellidos: "
                    + datosVehiculos.getVehiculo().getApellidos() + " | Dni: "
                    + datosVehiculos.getVehiculo().getDni() + " | Matricula: "
                    + datosVehiculos.getVehiculo().getMatricula() + " | Identificador: "
                    + datosVehiculos.getVehiculo().getIdentificador());
    
            timepoEspera += datosVehiculos.getTiempoEspera();
        }
    
        System.out.println("Media de espera: " + (timepoEspera / colaAtendidos.size()));
    }
}
