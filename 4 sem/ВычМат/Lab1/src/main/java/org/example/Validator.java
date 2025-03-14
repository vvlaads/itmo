package org.example;

import java.util.List;

public class Validator {

    public boolean validateN(String n) {
        int value;
        try {
            value = Integer.parseInt(n);
        } catch (NumberFormatException e) {
            return false;
        }
        if (value > 20) return false;
        return value > 0;
    }

    public boolean validateEpsilon(String epsilon) {
        double value;
        try {
            value = Double.parseDouble(epsilon);
        } catch (NumberFormatException e) {
            return false;
        }
        return value >= 0;
    }

    public boolean validateM(String M) {
        int value;
        try {
            value = Integer.parseInt(M);
        } catch (NumberFormatException e) {
            return false;
        }
        return value >= 0;
    }

    public boolean validateMatrix(List<String> matrix, int n) {
        for (String s : matrix) {
            if (!validateVector(s, n + 1)) return false;
        }
        return true;
    }

    public boolean validateVector(String vector, int n) {
        String[] components = vector.split(" ");
        if (components.length != n) return false;
        for (int i = 0; i < n; i++) {
            try {
                Double.parseDouble(components[i]);
            } catch (NumberFormatException e) {
                return false;
            }
        }
        return true;
    }
}
