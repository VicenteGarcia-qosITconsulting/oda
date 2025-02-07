package Model;

import java.util.ArrayList;
import java.util.List;

public class Curso {
    private String nombreCurso;
    private Profesor profesor;
    private List<Estudiante> estudiantes = new ArrayList<>();

    public Curso(String nombreCurso, Profesor profesor) {
        this.nombreCurso = nombreCurso;
        this.profesor = profesor;
    }

    public void matricularEstudiante(Estudiante estudiante) {
        estudiantes.add(estudiante);
        System.out.println(estudiante.getNombre() + " ha sido matriculado en " + nombreCurso);
    }

    public void mostrarEstudiantes() {
        System.out.println("Estudiantes en " + nombreCurso + ":");
        for (Estudiante e : estudiantes) e.mostrarInformacion();
    }

    public void mostrarProfesor() {
        System.out.println("Profesor del curso: ");
        profesor.mostrarInformacion();
    }
}