package modelo;

public class DatosVehiculos {

    private Vehiculo vehiculo;
    private long entrada;
    private long salida;
    private long tiempoEspera;

    public DatosVehiculos(Vehiculo vehiculo) {
        this.setVehiculo(vehiculo);
        this.setEntrada(Reloj.ahora());
    }

    public void setVehiculo(Vehiculo vehiculo) {
        this.vehiculo = vehiculo;
    }

    public void setEntrada(long entrada) {
        this.entrada = entrada;
    }

    public void setTiempoEspera(long tiempoEspera) {
        this.tiempoEspera = tiempoEspera;
    }

    public Vehiculo getVehiculo() {
        return vehiculo;
    }

    public long getEntrada() {
        return entrada;
    }

    public long getSalida() {
        return salida;
    }
    public void calcularTiempoEspera(){
        this.tiempoEspera=this.getSalida()-this.getEntrada();
    }
    public long getTiempoEspera() {
        return tiempoEspera/1000;
    }

    public void atiende(){
        this.salida=Reloj.ahora();
        calcularTiempoEspera();
    }
    @Override
    public String toString() {
        return "DatosVehiculos [vehiculo=" + vehiculo + ", entrada=" + entrada + ", salida=" + salida
                + ", tiempoEspera=" + tiempoEspera + "]";
    }

}
