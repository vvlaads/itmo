package org.example;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class InputModule {
    private Scanner scanner;

    public InputMode chooseMode() {
        InputMode mode;
        System.out.println("Выберите один из режимов:");
        System.out.println("1. " + InputMode.TEXT.getTitle());
        System.out.println("2. " + InputMode.FILE.getTitle());

        String line = scanner.nextLine();
        if (line.equals("1")) {
            mode = InputMode.TEXT;
        } else if (line.equals("2")) {
            mode = InputMode.FILE;
        } else {
            System.err.println("Неверно введен режим");
            mode = InputMode.ERROR;
        }
        return mode;
    }

    public String inputN(InputMode mode) {
        if (mode.equals(InputMode.TEXT)) {
            System.out.println("Введите порядок матрицы n:");
        }
        return scanner.nextLine();
    }

    public String inputEpsilon(InputMode mode) {
        if (mode.equals(InputMode.TEXT)) {
            System.out.println("Введите погрешность вычислений epsilon:");
        }
        return scanner.nextLine();
    }

    public String inputM(InputMode mode) {
        if (mode.equals(InputMode.TEXT)) {
            System.out.println("Введите максимально допустимое число итераций M:");
        }
        return scanner.nextLine();
    }

    public List<String> inputMatrix(InputMode mode, int n) {
        if (mode.equals(InputMode.TEXT)) {
            System.out.println("Введите n строк в формате:");
            System.out.println("a_i1 a_i2 ... a_in b_i");
        }
        List<String> lines = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            lines.add(scanner.nextLine());
        }
        return lines;
    }

    public String inputVector(InputMode mode) {
        if (mode.equals(InputMode.TEXT)) {
            System.out.println("Введите вектор начального приближения в формате:");
            System.out.println("x_1 x_2 ... x_n");
        }
        return scanner.nextLine();
    }

    public String chooseFile() {
        System.out.println("Введите путь к файлу:");
        return scanner.nextLine();
    }

    public void close() {
        this.scanner.close();
    }

    public InputModule() {
        this.scanner = new Scanner(System.in);
    }

    public Scanner getScanner() {
        return scanner;
    }

    public void setScanner(Scanner scanner) {
        this.scanner = scanner;
    }
}
