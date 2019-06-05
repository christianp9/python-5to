package beans;

import javax.inject.Named;
import javax.enterprise.context.SessionScoped;
import java.io.Serializable;

@Named(value = "calcuBeans")
@SessionScoped
public class calcuBeans implements Serializable {

    String display = "0";
    float total = 0;
    float a = 0;
    float b = 0;
    String operacion = "nada";

    public String getDisplay() {
        return display;
    }

    public void setDisplay(String display) {
        this.display = display;
    }

    public void boton1() {
        ponDisplay("1");
    }

    public void boton2() {
        ponDisplay("2");
    }

    public void boton3() {
        ponDisplay("3");
    }

    public void sumar() {
        a = obtenDisplay();

        display = "+";
        operacion = "sumar";

    }

    public void igual() {
        b = obtenDisplay();

        switch (operacion) {
            case "sumar":
                total = a + b;
                display = "" + total;
                break;
            case "restar":
                //bla bla
                break;
        }
    }

    public void limpiar() {
        display = "0";
        total = 0;
        a = 0;
        b = 0;
        operacion = "nada";
    }

    /**
     * Obtiene en float el numero del display usando un propio try-catch por
     * seguridad.
     *
     * @return el numero del display.
     */
    private float obtenDisplay() {

        float num = -1; //para identificar posibles errores

        if (!display.equals("+")) {
            try {
                num = Float.valueOf(display);
            } catch (NumberFormatException e) {
                System.out.println("Error convirtiendo string a float: " + e.getMessage());
            }
        }

        return num;
    }

    private void ponDisplay(String numero) {
        if (display.equals("0.0") || display.equals("0") || display.equals("+") || display.equals("-")) {
            display = numero;
        } else {
            display += numero;
        }
    }

}
