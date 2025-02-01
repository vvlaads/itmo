package lab.validators;


import jakarta.faces.application.FacesMessage;
import jakarta.faces.component.UIComponent;
import jakarta.faces.context.FacesContext;
import jakarta.faces.validator.Validator;
import jakarta.faces.validator.ValidatorException;

public class ValidatorX implements Validator {

    @Override
    public void validate(FacesContext context, UIComponent component, Object value) throws ValidatorException {
        if (value == null || value.toString().isEmpty()) {
            throw new ValidatorException(new FacesMessage("Выбор обязателен"));
        }
        try {
            String correctValue = (String) value;
            correctValue = correctValue.replace(",", ".");
            double doubleX = Double.parseDouble(correctValue);
            if (doubleX < -5 || doubleX > 3) {
                throw new ValidatorException(new FacesMessage("X должен быть от -5 до 3"));
            }
        } catch (NumberFormatException e) {
            throw new ValidatorException(new FacesMessage("X должен быть числом"));
        }
    }
}
