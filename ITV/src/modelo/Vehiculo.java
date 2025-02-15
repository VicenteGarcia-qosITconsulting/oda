package modelo;

import excepciones.DniException;
import excepciones.MatriculaException;

public class Vehiculo {

    private String nombre;
    private String apellidos;
    private String dni;
    private String matricula;
    private String identificador;

    public Vehiculo() {
    }

    public Vehiculo(String nombre, String apellidos, String dni, String matricula)
            throws DniException, MatriculaException {
        this.setNombre(nombre);
        this.setApellidos(apellidos);
        this.setDni(dni);
        this.setMatricula(matricula);
        this.setIdentificador(identificador);
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }

    public void setDni(String dni) throws DniException {
        comprobarDni(dni);
        this.dni = dni;

    }

    private void comprobarDni(String dni) throws DniException {
        String checks = "TRWAGMYFPDXBNJZSQVHLCKE";

        if (dni.length() != 9) {
            throw new DniException();
        }

        int numDniSinLetra = Integer.parseInt(dni.substring(0, 8));
        char letraDni = dni.charAt(8);
        char supuestaLetra = checks.charAt(numDniSinLetra % 23);

        if (supuestaLetra != letraDni) {
            throw new DniException();
        }
    }

    public void setMatricula(String matricula) throws MatriculaException {
        comprobarMatricula(matricula);
        this.matricula = matricula;
    }

    private void comprobarMatricula(String matricula) throws MatriculaException {

        if (matricula.length() != 7) {
            throw new MatriculaException();
        }

        String parteNumerica = matricula.substring(0, 4);
        String parteLetras = matricula.substring(4, 7);

        for (int i = 0; i < parteNumerica.length(); i++) {
            if (!Character.isDigit(parteNumerica.charAt(i))) {
                throw new MatriculaException();
            }
        }

        for (int i = 0; i < parteLetras.length(); i++) {
            if (!Character.isLetter(parteLetras.charAt(i))) {
                throw new MatriculaException();
            }
        }
        matricula = matricula.toUpperCase();
    }

    public void setIdentificador(String identificador) {
        this.identificador = generaIdentificador(identificador, dni, apellidos, nombre);
    }

    private String generaIdentificador(String identificador, String dni, String apellidos, String nombre) {
        String[] arrayApellidos = apellidos.split(" ");

        String letraNombre = nombre.substring(0, 1);

        String letraApellido = apellidos.substring(0, 1);
        letraApellido += arrayApellidos[1].charAt(0);

        String numerosDni = dni.substring(5, 8);

        identificador = letraNombre + letraApellido + numerosDni;
        identificador = identificador.toUpperCase();
        return identificador;
    }

    public String getNombre() {
        return nombre;
    }

    public String getApellidos() {
        return apellidos;
    }

    public String getDni() {
        return dni;
    }

    public String getMatricula() {
        return matricula;
    }

    public String getIdentificador() {
        return identificador;
    }

    @Override
    public String toString() {
        return "Vehiculo [nombre=" + nombre + ", apellidos=" + apellidos + ", dni=" + dni + ", matricula=" + matricula
                + ", identificador=" + identificador + "]";
    }

}
