package Model;

public class Direccion {
    private String calle, ciudad, codigoPostal;

    public Direccion(String calle, String ciudad, String codigoPostal) {
        this.calle = calle;
        this.ciudad = ciudad;
        this.codigoPostal = codigoPostal;
    }

    public String getDireccionCompleta() {
        return calle + ", " + ciudad + " - " + codigoPostal;
    }
}
