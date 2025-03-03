package org.example;

import java.util.HashSet;

public class GaussSeidelMethod {
    private int n;
    private double epsilon;
    private int M;
    private double[][] matrix;
    private double[][] normal;

    private double[] bValues;
    private double[] vector;

    private int iterationCount;

    private double[] deltaVector;

    public void calculate() {
        boolean sorted = sortMatrix();
        boolean diag = true;

        for (int i = 0; i < n; i++) {
            double row = 0;
            double main = Math.abs(matrix[i][i]);
            for (int j = 0; j < n; j++) {
                row += Math.abs(matrix[i][j]);
            }

            if (main <= row - main) {
                diag = false;
                break;
            }
        }
        if (!diag) {
            System.out.println("Невозможно достигнуть диагонального преобладания");
        } else {
            System.out.println("Достигнуто диагональное преобладание");
        }

        for (int k = 1; k <= M; k++) {
            iterationCount = k;
            double[] nextVector = new double[n];
            for (int i = 0; i < n; i++) {
                if (matrix[i][i] == 0) {
                    System.err.println("Диагональный элемент равен нулю");
                    throw new RuntimeException();
                }
                nextVector[i] = (bValues[i] - sumOnCurrentIteration(i, nextVector) - sumOnLastIteration(i))
                        / (matrix[i][i]);
            }

            boolean ready = true;
            for (int i = 0; i < n; i++) {
                double delta = Math.abs(nextVector[i] - vector[i]);
                if (delta > epsilon) ready = false;
                deltaVector[i] = delta;
            }
            vector = nextVector;
            if (ready) return;
        }
    }

    public void normalMatrix() {
        normal = new double[n][n];
        for (int i = 0; i < n; i++) {
            double main = Math.abs(matrix[i][i]);
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    normal[i][j] = -matrix[i][j] / main;
                }
            }
        }
    }


    private double sumOnCurrentIteration(int i, double[] nextVector) {
        double result = 0;
        for (int j = 0; j < i; j++) {
            result += matrix[i][j] * nextVector[j];
        }
        return result;
    }

    private double sumOnLastIteration(int i) {
        double result = 0;
        for (int j = i + 1; j < n; j++) {
            result += matrix[i][j] * vector[j];
        }
        return result;
    }

    public boolean sortMatrix() {
        HashSet<Integer> indexes = new HashSet<>();
        double[][] sortedMatrix = new double[n][n];
        double[] sortedBValues = new double[n];
        double[] sortedVector = new double[n];
        for (int i = 0; i < n; i++) {
            double[] row = new double[n];
            double maxValue = -1;
            int index = 0;
            double sum = 0;
            for (int j = 0; j < n; j++) {
                row[j] = matrix[i][j];
                sum += Math.abs(row[j]);
                if (Math.abs(row[j]) > maxValue) {
                    maxValue = Math.abs(row[j]);
                    index = j;
                }
            }
            if (maxValue == -1 || maxValue >= sum || indexes.contains(index)) return false;
            indexes.add(index);
            sortedMatrix[index] = row;
            sortedBValues[index] = bValues[i];
            sortedVector[index] = vector[i];
        }
        setMatrix(sortedMatrix);
        setBValues(sortedBValues);
        setVector(sortedVector);
        return true;
    }

    public double getNorm() {
        normalMatrix();
        double result = 0;
        for (int i = 0; i < n; i++) {
            double rowSum = 0;
            for (int j = 0; j < n; j++) {
                rowSum += Math.abs(normal[i][j]);
            }
            if (rowSum > result) {
                result = rowSum;
            }
        }
        return result;
    }

    public GaussSeidelMethod(int n, double epsilon, int M, double[][] matrix, double[] bValues, double[] vector) {
        setN(n);
        setEpsilon(epsilon);
        setM(M);
        setMatrix(matrix);
        setBValues(bValues);
        setVector(vector);
        setIterationCount(0);
        setDeltaVector(vector);
    }

    public int getN() {
        return n;
    }

    public void setN(int n) {
        this.n = n;
    }

    public double getEpsilon() {
        return epsilon;
    }

    public void setEpsilon(double epsilon) {
        this.epsilon = epsilon;
    }

    public int getM() {
        return M;
    }

    public void setM(int m) {
        M = m;
    }

    public double[][] getMatrix() {
        return matrix;
    }

    public void setMatrix(double[][] matrix) {
        this.matrix = matrix;
    }

    public double[][] getNormal() {
        return normal;
    }

    public void setNormal(double[][] normal) {
        this.normal = normal;
    }

    public double[] getBValues() {
        return bValues;
    }

    public void setBValues(double[] bValues) {
        this.bValues = bValues;
    }

    public double[] getVector() {
        return vector;
    }

    public void setVector(double[] vector) {
        this.vector = vector;
    }

    public int getIterationCount() {
        return iterationCount;
    }

    public void setIterationCount(int iterationCount) {
        this.iterationCount = iterationCount;
    }

    public double[] getDeltaVector() {
        return deltaVector;
    }

    public void setDeltaVector(double[] deltaVector) {
        this.deltaVector = deltaVector;
    }
}
