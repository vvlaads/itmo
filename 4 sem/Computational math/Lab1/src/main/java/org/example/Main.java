package org.example;

import java.io.File;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        InputModule inputModule = new InputModule();
        OutputModule outputModule = new OutputModule();
        FileManager fileManager = new FileManager();
        Validator validator = new Validator();

        InputMode mode = inputModule.chooseMode();

        while (mode.equals(InputMode.ERROR)) {
            mode = inputModule.chooseMode();
        }

        if (mode.equals(InputMode.FILE)) {
            String filename = inputModule.chooseFile();
            File file = fileManager.getFileByPath(filename);
            while (!fileManager.fileIsValid(file)) {
                System.err.println("Невозможно прочитать файл: " + file.getAbsolutePath());
                filename = inputModule.chooseFile();
                file = fileManager.getFileByPath(filename);
            }
            Scanner fileScanner = fileManager.getFileScanner(file);
            while (fileScanner == null) {
                System.err.println("Ошибка чтения, введите повторно путь к файлу");
                while (!fileManager.fileIsValid(file)) {
                    System.err.println("Невозможно прочитать файл: " + file.getAbsolutePath());
                    filename = inputModule.chooseFile();
                    file = fileManager.getFileByPath(filename);
                }
                fileScanner = fileManager.getFileScanner(file);
            }
            inputModule.setScanner(fileScanner);
        }

        try {
            String nLine = inputModule.inputN(mode);
            while (!validator.validateN(nLine)) {
                System.err.println("Некорректное значение n");
                if (!mode.equals(InputMode.TEXT)) {
                    System.exit(1);
                }
                nLine = inputModule.inputN(mode);
            }
            int n = Integer.parseInt(nLine);


            String epsilonLine = inputModule.inputEpsilon(mode);
            while (!validator.validateEpsilon(epsilonLine)) {
                System.err.println("Некорректное значение epsilon");
                if (!mode.equals(InputMode.TEXT)) {
                    System.exit(1);
                }
                epsilonLine = inputModule.inputEpsilon(mode);
            }
            double epsilon = Double.parseDouble(epsilonLine);


            String MLine = inputModule.inputM(mode);
            while (!validator.validateM(MLine)) {
                System.err.println("Некорректное значение M");
                if (!mode.equals(InputMode.TEXT)) {
                    System.exit(1);
                }
                MLine = inputModule.inputM(mode);
            }
            int M = Integer.parseInt(MLine);


            List<String> matrixLines = inputModule.inputMatrix(mode, n);
            while (!validator.validateMatrix(matrixLines, n)) {
                System.err.println("Некорректная матрица");
                if (!mode.equals(InputMode.TEXT)) {
                    System.exit(1);
                }
                matrixLines = inputModule.inputMatrix(mode, n);
            }
            double[][] matrix = new double[n][n];
            double[] bValues = new double[n];
            for (int i = 0; i < n; i++) {
                String[] line = matrixLines.get(i).split(" ");
                for (int j = 0; j < n; j++) {
                    matrix[i][j] = Double.parseDouble(line[j]);
                }
                bValues[i] = Double.parseDouble(line[n]);
            }


            String vectorLine = inputModule.inputVector(mode);
            while (!validator.validateVector(vectorLine, n)) {
                System.err.println("Некорректный вектор начального приближения");
                if (!mode.equals(InputMode.TEXT)) {
                    System.exit(1);
                }
                vectorLine = inputModule.inputVector(mode);
            }
            String[] vectorComponents = vectorLine.split(" ");
            double[] vector = new double[n];
            for (int i = 0; i < n; i++) {
                vector[i] = Double.parseDouble(vectorComponents[i]);
            }

            System.out.println("Введенная матрица:");
            outputModule.printMatrix(matrix, n);

            GaussSeidelMethod method = new GaussSeidelMethod(n, epsilon, M, matrix, bValues, vector);

            method.calculate();

            System.out.println("Отсортированная матрица:");
            outputModule.printMatrix(method.getMatrix(), n);

            System.out.println("Норма матрицы: " + method.getNorm());

            System.out.println("Нормализованная матрица:");
            outputModule.printMatrix(method.getNormal(), method.getN());

            System.out.println("Вектор неизвестных:");
            double[] vec = method.getVector();
            outputModule.printVector(vec, n);

            System.out.println("Количество итераций: " + method.getIterationCount());

            System.out.println("Вектор погрешностей:");
            double[] deltaVec = method.getDeltaVector();
            outputModule.printVector(deltaVec, n);

        } catch (NoSuchElementException e) {
            System.err.println("Ошибка ввода данных");
            System.exit(1);
        } catch (RuntimeException e) {
            System.exit(1);
        } finally {
            inputModule.close();
        }
    }
}
