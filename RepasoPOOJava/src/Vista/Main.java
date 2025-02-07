package Vista;

import Model.Curso;
import Model.Estudiante;
import Model.Profesor;

public class Main {
    public static void main(String[] args) {
        Profesor prof1 = new Profesor("Dr. García", 45, "Matemáticas");
        Profesor prof2 = new Profesor("Dra. López", 50, "Física");

        Estudiante est1 = new Estudiante("Juan", 20, "Ingeniería");
        Estudiante est2 = new Estudiante("Ana", 22, "Medicina");
        Estudiante est3 = new Estudiante("Carlos", 21, "Derecho");

        Curso curso1 = new Curso("Álgebra Lineal", prof1);
        Curso curso2 = new Curso("Mecánica Clásica", prof2);

        curso1.matricularEstudiante(est1);
        curso1.matricularEstudiante(est2);
        curso2.matricularEstudiante(est3);

        curso1.mostrarProfesor();
        curso1.mostrarEstudiantes();
        curso2.mostrarProfesor();
        curso2.mostrarEstudiantes();

        prof1.trabajar();
        prof2.trabajar();
    }
}
