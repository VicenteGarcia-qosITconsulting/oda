package excepciones;

public class DniException extends Exception {
    public DniException(){
        super("Introduce un dni correcto");
    }
}
