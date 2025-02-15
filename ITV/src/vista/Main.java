package vista;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.Buffer;
import java.util.Random;
import controller.VehiculoController;
import excepciones.DniException;
import excepciones.MatriculaException;
import modelo.Vehiculo;

public class Main {
    public static void main(String[] args) throws InterruptedException, IOException {

        try {
            VehiculoController vc = new VehiculoController();
            File f;
            FileReader fr;
            BufferedReader br;
            f = new File("itv.txt");

            if (!f.exists()) {
                System.out.println("creando fichero");
                f.createNewFile();
            }

            fr = new FileReader(f);
            br = new BufferedReader(fr);

            String lineas = "";

            while ((lineas = br.readLine()) != null) {

                String[] datoSplit = lineas.split(",");
                Vehiculo v1 = new Vehiculo(datoSplit[0], datoSplit[1], datoSplit[2], datoSplit[3]);
                vc.nuevoVehiculo(v1);
                lineas = br.readLine();
            }

            Random rd = new Random();

            Thread.sleep(1000);

            while (vc.getColaEspera().size() > 0) {

                System.out.println("Siguiente: " + vc.llamarVehiculo().getIdentificador());

                Thread.sleep((rd.nextInt(10) * 1000));
            }

            vc.timepoEspera();

        } catch (DniException | MatriculaException e) {
            e.getMessage();
        }
    }

}
