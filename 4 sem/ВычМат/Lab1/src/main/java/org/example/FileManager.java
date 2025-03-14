package org.example;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class FileManager {

    public File getFileByPath(String path) {
        return new File(path);
    }

    public boolean fileIsValid(File file) {
        return file.exists() && file.isFile() && file.canRead();
    }

    public Scanner getFileScanner(File file) {
        Scanner scanner;
        try {
            scanner = new Scanner(file);
        } catch (FileNotFoundException e) {
            return null;
        }
        return scanner;
    }
}
