// Console Quiz Program
// Purpose: Present multiple-choice questions, validate user input, score the quiz, and report results.
// Author: Dante Green
// Date: 2025-09-13

import java.util.*;

// Simple data model to represent a question
class Question {
    String text;
    String[] choices;    // length should be 4: A, B, C, D
    int correctIndex;    // 0 for A, 1 for B, 2 for C, 3 for D
    String explanation;  // optional feedback shown after answering

    Question(String text, String[] choices, int correctIndex, String explanation) {
        this.text = text;
        this.choices = choices;
        this.correctIndex = correctIndex;
        this.explanation = explanation;
    }
}

public class QuizApp {
    public static void main(String[] args) {
        // Create a list of questions
        List<Question> questions = new ArrayList<>();

        questions.add(new Question(
            "What is 2 + 2?",
            new String[] {"3", "4", "5", "22"},
            1,
            "2 + 2 equals 4."
        ));

        questions.add(new Question(
            "Which Java keyword indicates inheritance?",
            new String[] {"extends", "implements", "import", "package"},
            0,
            "'extends' is used for class inheritance. 'implements' is for interfaces."
        ));

        questions.add(new Question(
            "What is the index of the first element in a Java array?",
            new String[] {"1", "0", "-1", "Depends"},
            1,
            "Java arrays are zero-indexed, so the first element is at index 0."
        ));

        questions.add(new Question(
            "Which type is used to store true/false values in Java?",
            new String[] {"int", "String", "boolean", "double"},
            2,
            "The 'boolean' type holds true or false."
        ));

        questions.add(new Question(
            "Which class is commonly used for console input in Java?",
            new String[] {"Scanner", "Reader", "Console", "Buffer"},
            0,
            "Scanner (java.util.Scanner) is commonly used for simple console input."
        ));

        // Scanner for user input
        Scanner scanner = new Scanner(System.in);

        int score = 0;
        int qNumber = 1;

        System.out.println("=== Java Console Quiz ===");
        for (Question q : questions) {
            System.out.println();
            System.out.println("Q" + qNumber + ": " + q.text);
            char label = 'A';
            for (String choice : q.choices) {
                System.out.println("  " + label + ") " + choice);
                label++;
            }

            // Read a valid answer (A-D)
            int answerIndex = readAnswerIndex(scanner);

            // Check correctness
            if (answerIndex == q.correctIndex) {
                System.out.println("Correct!");
                score++;
            } else {
                char correctLetter = (char) ('A' + q.correctIndex);
                System.out.println("Incorrect. Correct answer: " + correctLetter + ") " + q.choices[q.correctIndex]);
            }

            // Optional explanation
            if (q.explanation != null && !q.explanation.isEmpty()) {
                System.out.println("Note: " + q.explanation);
            }

            qNumber++;
        }

        // Final results
        int total = questions.size();
        double percentage = (score * 100.0) / total;

        System.out.println();
        System.out.println("=== Results ===");
        System.out.println("Score: " + score + " / " + total);
        System.out.printf("Percentage: %.2f%%%n", percentage);

        if (percentage == 100.0) {
            System.out.println("Great job! Perfect score!");
        } else if (percentage >= 80.0) {
            System.out.println("Nice work! You're doing well.");
        } else if (percentage >= 50.0) {
            System.out.println("Not bad. Review the explanations and try again.");
        } else {
            System.out.println("Keep practicing! You'll improve quickly.");
        }

        // scanner.close();  // Optional: avoid closing System.in in some environments
    }

    // Reads and validates user input (A-D). Keeps prompting until valid.
    private static int readAnswerIndex(Scanner scanner) {
        while (true) {
            System.out.print("Enter your choice (A, B, C, or D): ");
            String input = scanner.nextLine().trim();

            if (input.isEmpty()) {
                System.out.println("Input cannot be empty. Please enter A, B, C, or D.");
                continue;
            }

            char ch = Character.toUpperCase(input.charAt(0));
            if (ch >= 'A' && ch <= 'D') {
                return ch - 'A'; // map A-D to 0-3
            } else {
                System.out.println("Invalid choice. Please enter A, B, C, or D.");
            }
        }
    }
}
