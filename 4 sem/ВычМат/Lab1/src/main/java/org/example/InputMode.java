package org.example;

public enum InputMode {
    TEXT("Ввод из консоли"),
    FILE("Ввод данных из файла"),
    ERROR("Ошибка");

    private final String title;

    InputMode(String title) {
        this.title = title;
    }

    public String getTitle() {
        return title;
    }
}
