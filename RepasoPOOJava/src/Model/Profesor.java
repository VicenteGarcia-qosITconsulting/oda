package Model;

public class Profesor extends Persona implements Trabajador {
    private String especialidad;

    public Profesor(String nombre, int edad, String especialidad) {
        super(nombre, edad);
        this.especialidad = especialidad;
    }

    public String getEspecialidad() { return especialidad; }
    public void setEspecialidad(String especialidad) { this.especialidad = especialidad; }

    @Override
    public void trabajar() {
        System.out.println(getNombre() + " está enseñando " + especialidad);
    }

    @Override
    public void mostrarInformacion() {
        super.mostrarInformacion();
        System.out.println("Especialidad: " + especialidad);
    }
}
