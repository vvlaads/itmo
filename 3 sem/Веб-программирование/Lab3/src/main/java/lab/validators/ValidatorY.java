package lab.validators;


import jakarta.faces.application.FacesMessage;
import jakarta.faces.component.UIComponent;
import jakarta.faces.context.FacesContext;
import jakarta.faces.validator.Validator;
import jakarta.faces.validator.ValidatorException;

public class ValidatorY implements Validator {

    @Override
    public void validate(FacesContext context, UIComponent component, Object value) throws ValidatorException {
        if (value != null) {
            String correctValue = (String) value;
            correctValue = correctValue.replace(",", ".");
            if (correctValue.isEmpty()) {
                throw new ValidatorException(new FacesMessage("Не введено значение"));
            }
            try {
                double doubleValue = Double.parseDouble(correctValue);
                if (doubleValue < -3 || doubleValue > 5) {
                    throw new ValidatorException(new FacesMessage("Введите значение от -3 до 5"));
                }
            } catch (NumberFormatException e) {
                throw new ValidatorException(new FacesMessage("Введите число"));
            }
        }
    }
}
