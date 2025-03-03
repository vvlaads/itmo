package org.example;

public class OutputModule {
    public void printMatrix(double[][] matrix, int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public void printVector(double[] vector, int n) {
        for (int i = 0; i < n; i++) {
            System.out.print(vector[i] + " ");
        }
        System.out.println();
    }
}
