/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package org.xulescode.jsf;

import javax.faces.bean.ManagedBean;
import javax.faces.bean.SessionScoped;
import javax.faces.context.FacesContext;
import javax.servlet.http.HttpSession;


/**
 *
 * @author Orlando Castilla
 */
@ManagedBean
@SessionScoped
public class UserManagedBean {

    /**
     * Creates a new instance of UserManagedBean
     */
    private String code;

    public UserManagedBean() {
        code = "XULES-CODE";
        System.out.println("Validation code (Código de validación): " + code);

    }

    private String user;
    private String nickName;
    private String email;
    private String validationCode;

    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }

    public String getNickName() {
        return nickName;
    }

    public void setNickName(String nickName) {
        this.nickName = nickName;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getValidationCode() {
        return validationCode;
    }

    public void setValidationCode(String validationCode) {
        this.validationCode = validationCode;
    }
    

    
    public String getValidation() {
        if ((validationCode != null) && (validationCode.compareTo(code) == 0)) {
            // The validationCode is OK then we show the user data in validation.xhtml
            // El código validationCode es correcto entonces mostramos los datos en validation.xhtm
            FacesContext context = FacesContext.getCurrentInstance();
            HttpSession session = (HttpSession) context.getExternalContext().getSession(false);
            session.invalidate();
            return "<p>User accepted:</p>"
                    + "<ul>"
                    + " <li>User: " + getUser() + " </li>"
                    + " <li>Nick name: " + getNickName() + " </li>"
                    + " <li>Email: " + getEmail() + " </li>"
                    + "</ul>";
        } else {
            return "<p>Sorry, " + validationCode + " isn't valid.</p>"
                    + "<p>Try again...</p>";
        }
    }

}
